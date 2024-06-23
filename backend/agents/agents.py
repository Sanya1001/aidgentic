from typing import Annotated
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    ToolMessage,
)
from typing import List
# import runnable
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import operator
from typing import Annotated, Sequence, TypedDict
from langchain_core.runnables.base import RunnableSequence
from langchain_core.messages import AIMessage
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.pydantic_v1 import BaseModel, Field

from tools import (
    read_database,
    get_ngos_for_region,

)


# This defines the object that is passed between each node
# in the graph. We will create different nodes for each agent and tool
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    sender: str
    briefing: str = ""

class NGOList(BaseModel):
    ngo_list: List[dict] = Field([], description="List of NGOs who cover the given region and have applicable resources.")

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
    print('aggregator_agent returning')
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
    state.update({"messages": msg, 'agent_scratchpad': []})
    result = agent.invoke(state)

    # We convert the agent output into a format that is suitable to append to the global state
    #result = HumanMessage(**result.dict(exclude={"type", "name"}), name=name)
    print('ngo_agent returning')
    ret= {
        "messages": [result],
        # Since we have a strict workflow, we can
        # track the sender so we know who to pass to next.
        "sender": name,
    }
    state.update(ret)
    return ret
