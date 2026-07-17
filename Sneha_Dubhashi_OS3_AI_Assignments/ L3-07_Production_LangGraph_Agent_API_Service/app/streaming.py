import asyncio

from sse_starlette.sse import EventSourceResponse

from app.agent import get_agent


async def generate(message: str):

    agent = await get_agent()

    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ]
        }
    )

    response = result["messages"][-1].content

    for word in response.split():

        yield {
            "event": "message",
            "data": word + " "
        }

        await asyncio.sleep(0.02)

    yield {
        "event": "end",
        "data": "[DONE]"
    }


async def stream_chat(message: str):

    return EventSourceResponse(generate(message))