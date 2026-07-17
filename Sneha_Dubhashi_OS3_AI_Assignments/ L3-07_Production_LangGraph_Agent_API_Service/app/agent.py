import os

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


async def get_agent():

    client = MultiServerMCPClient(
        {
            "calculator": {
                "transport": "stdio",
                "command": "python",
                "args": [
                    os.path.abspath("app/mcp_server.py")
                ]
            }
        }
    )

    tools = await client.get_tools()

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    agent = create_agent(
        model=llm,
        tools=tools
    )

    return agent