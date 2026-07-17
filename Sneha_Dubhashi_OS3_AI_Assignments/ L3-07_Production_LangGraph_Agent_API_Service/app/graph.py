from langgraph.graph import StateGraph
from langchain_ollama import ChatOllama

from app.state import AgentState
from app.config import OLLAMA_MODEL

llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0
)


def chatbot(state: AgentState):

    response = llm.invoke(state["input"])

    return {
        "output": response.content
    }


builder = StateGraph(AgentState)

builder.add_node("chatbot", chatbot)

builder.set_entry_point("chatbot")

builder.set_finish_point("chatbot")

graph = builder.compile()