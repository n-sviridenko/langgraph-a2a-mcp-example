from typing_extensions import TypedDict, Literal
from contextlib import asynccontextmanager

from langgraph.graph import StateGraph, END
from my_agent.utils.nodes import make_call_model, should_continue
from my_agent.utils.state import AgentState
from my_agent.utils.tools import get_tavily_mcp_tools
from langgraph.prebuilt import ToolNode

# Configuration schema
class GraphConfig(TypedDict):
    model_name: Literal["anthropic", "openai"]


@asynccontextmanager
async def create_graph():
    # Load MCP tools and configure the graph
    async with get_tavily_mcp_tools() as tools:
        # Define a new graph
        workflow = StateGraph(AgentState, config_schema=GraphConfig)

        # Define the two nodes we will cycle between
        workflow.add_node("agent", make_call_model(tools))
        workflow.add_node("action", ToolNode(tools))

        # Set the entrypoint as `agent`
        # This means that this node is the first one called
        workflow.set_entry_point("agent")

        # We now add a conditional edge
        workflow.add_conditional_edges(
            # First, we define the start node. We use `agent`.
            # This means these are the edges taken after the `agent` node is called.
            "agent",
            # Next, we pass in the function that will determine which node is called next.
            should_continue,
            # Finally we pass in a mapping.
            # The keys are strings, and the values are other nodes.
            # END is a special node marking that the graph should finish.
            # What will happen is we will call `should_continue`, and then the output of that
            # will be matched against the keys in this mapping.
            # Based on which one it matches, that node will then be called.
            {
                # If `tools`, then we call the tool node.
                "continue": "action",
                # Otherwise we finish.
                "end": END,
            },
        )

        # We now add a normal edge from `tools` to `agent`.
        # This means that after `tools` is called, `agent` node is called next.
        workflow.add_edge("action", "agent")

        # Finally, we compile it!
        # This compiles it into a LangChain Runnable,
        # meaning you can use it as you would any other runnable
        graph = workflow.compile()
        
        yield graph
