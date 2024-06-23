import os
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    ToolMessage,
)
from langgraph.graph import END, StateGraph
import functools
from langchain_core.messages import BaseMessage, HumanMessage
from typing import List, Tuple, Literal
from langgraph.prebuilt import ToolNode
from langchain_anthropic import ChatAnthropic
from agents.tools import (
    search_disaster_knowledge_base,
    get_ngos_for_region,
    ngo_output_to_list
)
from agents.agents import (
    create_agent,
    reporter_agent,
    resource_agent,
    ngo_agent,
    AgentState,
    NGOList
)
from agents.prompts import PROMPTS
class MAGraph():
    def __init__(self, model='claude-3-opus-20240229'):
        self.model = model
        self._create_agents()
        self._create_graph()
    def _create_agents(self):
        llm = ChatAnthropic(model=self.model,
            api_key = os.environ['ANTHROPIC_API_KEY'])
        # Research agent and node
        regional_reporter = create_agent(
            llm,
            tools=[],#[read_database],
            system_prompt=PROMPTS['regional_reporter']
        )
        reporter_node = functools.partial(reporter_agent, agent=regional_reporter, name="regional_reporter")

        # chart_generator
        resource_requestor = create_agent(
            llm,
            [search_disaster_knowledge_base],
            system_prompt=PROMPTS['resource_requestor']
        )
        resource_requestor_node = functools.partial(resource_agent, agent=resource_requestor, name="resource_requestor")

        ngollm = llm.with_structured_output(NGOList)
        ngo_router = create_agent(
            ngollm,
            tools=[],#[get_ngos_for_region],
            system_prompt=PROMPTS['ngo_router']
        )
        ngo_router_node = functools.partial(ngo_agent, agent=ngo_router, name="ngo_router")
        tools = [search_disaster_knowledge_base]
        tool_node = ToolNode(tools)

        self.region_reporter_agent = regional_reporter
        self.resource_requesto_agent = resource_requestor
        self.ngo_router_agent = ngo_router

        self.reporter_node = reporter_node
        self.resource_requestor_node = resource_requestor_node
        self.ngo_router_node = ngo_router_node
        self.tool_node = tool_node
    def _create_graph(self):
        workflow = StateGraph(AgentState)
        workflow.add_node("regional_reporter", self.reporter_node)
        workflow.add_node("resource_requestor", self.resource_requestor_node)
        workflow.add_node("ngo_router", self.ngo_router_node)
        workflow.add_node("call_tool", self.tool_node)

        workflow.add_edge('regional_reporter', 'resource_requestor')
        workflow.add_conditional_edges(
            "resource_requestor",
            self.router,
            {"continue": "ngo_router", 
            "call_tool": "call_tool",},
        )

        workflow.add_conditional_edges(
            "call_tool",
            lambda x: x["sender"],
            {
                "resource_requestor": "resource_requestor",
            },
        )


        workflow.add_edge('ngo_router', END)
        workflow.set_entry_point("regional_reporter")
        self.graph = workflow.compile()
    def router(self,state) -> Literal["call_tool", "__end__", "continue"]:
        # This is the router
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            # The previous agent is invoking a tool
            return "call_tool"
        return "continue"
    def invoke(self):
        briefing = None
        ngo_output = None
        for state in self.graph.stream({"messages": [HumanMessage(content="", name=""),],
                                        'agent_scratchpad':[]},
                                        {"recursion_limit": 20},):
            #print(state)
            if state.get('resource_requestor', None):
                briefing = state['resource_requestor']['messages'][-1].content
            if state.get('ngo_router', None):
                ngo_output = state['ngo_router']['messages'][-1].messages[-1].content
            
        briefing = briefing.split('<result>')[-1].strip('</result>')
        ngo_output = ngo_output_to_list(ngo_output)
        print("Briefing:", briefing)
        print("NGO Output:", ngo_output)
        return {'report': briefing, 'ngos': ngo_output}


if __name__ == "__main__":
    ma = MAGraph()
    ma.invoke()
            


                
