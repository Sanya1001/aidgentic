from typing import Annotated, Any
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from typing import Annotated
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    ToolMessage,
)
from typing import List, TypedDict, Literal
# import runnable
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import operator
from typing import Annotated, Sequence, Dict
from langchain_core.runnables.base import RunnableSequence
from langchain_core.messages import AIMessage
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.pydantic_v1 import BaseModel, Field
from enum import Enum
from agents.tools import(
    read_database,
    get_ngos_for_region,

)


# This defines the object that is passed between each node
# in the graph. We will create different nodes for each agent and tool
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    sender: str
    briefing: str = ""

# Define a type alias for the NGO name using Literal and the values from the RegisteredNGOs enum
NGOName = Literal[
    "Red Cross US",
    "Red Cross Canada",
   "United Nations Children's Fund",
    "World Food Program",
    "California Fire Foundation",
]

class NGO(TypedDict):
    name: NGOName  # Use the type alias here
    region: str
    date: str
    resources: str
class NGOList(BaseModel):
    '''
    Required output structure for the ngo_agent
    '''
    ngo_list: List[NGO] = Field(description="List of NGOs. Each NGO should have a name, region, date, and requested resources from this NGO for the situation at hand")
    title: str = Field(description="Title of the briefing.")
    body: str = Field(description="Body of the briefing.")
def create_agent(llm, tools, system_prompt: str):
    """Create an agent."""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant."
                "Your task is {system_prompt}."
            ),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    prompt = prompt.partial(system_prompt=system_prompt)
   # prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools])) 
    if isinstance(llm, RunnableSequence):
        return prompt
    return prompt | llm.bind_tools(tools) 
def reporter_agent(state, agent, name):
    '''
    This tool reads the database json and summarizes the reports.
    '''
    
    reports_list = read_database()
    usr_msg = ', '.join([f"{k}: {v}" for report in reports_list for k, v in report.items()])
    msg = [HumanMessage(content=usr_msg, name=name)]
    state.update({"messages": msg, 'agent_scratchpad': []})
    result = agent.invoke(state)
    # We convert the agent output into a format that is suitable to append to the global state
    result = HumanMessage(**result.dict(exclude={"type", "name"}), name=name)
    print('regional reporting agent returning')
    ret= {
        "messages": [result],
        # Since we have a strict workflow, we can
        # track the sender so we know who to pass to next.
        "sender": name,
    }
    state.update(ret)
    return ret
    


def resource_agent(state, agent, name):
    '''
    This is resource agent
    '''
    print('agent', name, 'called')
    state['agent_scratchpad'] = []
    result = agent.invoke(state)
    # We convert the agent output into a format that is suitable to append to the global state
    state['agent_scratchpad'].append(result.content)
    state['sender'] = name
    result = AIMessage(**result.dict(exclude={"type", "name"}), name=name)
    ret = {
        'messages': state['messages'] + [result],
        'sender': name,
        'briefing': result.content
    }
    state.update(ret)
    return ret

def ngo_agent(state, agent, name):
    '''
    This is resource agent
    '''
    print('agent', name, 'called')
    ngos_list = get_ngos_for_region(region='CA')
    usr_msg = ', '.join([f"{k}: {v}" for ngo in ngos_list for k, v in ngo.items()])
    msg = [HumanMessage(content=usr_msg, name=name)]
    state['messages'] = state['messages'] + msg 
    state['agent_scratchpad'] = state.get('agent_scratchpad', [])
    result = agent.invoke(state)

    # We convert the agent output into a format that is suitable to append to the global state
    result = AIMessage(**result.dict(exclude={"type", "name"}), name=name)
    print('ngo_agent returning')
    ret= {
        "messages": [result],
        # Since we have a strict workflow, we can
        # track the sender so we know who to pass to next.
        "sender": name,
    }
    state.update(ret)
    return ret
