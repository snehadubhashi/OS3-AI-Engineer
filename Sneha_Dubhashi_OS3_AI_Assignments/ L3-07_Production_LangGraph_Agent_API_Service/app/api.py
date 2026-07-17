import time

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.agent import get_agent
from app.logger import logger
from app.models import ChatRequest, ChatResponse
from app.streaming import stream_chat

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):

    logger.info(f"Request Received: {request.message}")

    start = time.time()

    try:

        agent = await get_agent()

        result = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": request.message
                    }
                ]
            }
        )

        execution_time = round(time.time() - start, 2)

        logger.info(f"Execution Completed in {execution_time} sec")

        return ChatResponse(
            response=result["messages"][-1].content
        )

    except Exception as e:

        logger.exception("Agent Execution Failed")

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Agent execution failed",
                "error": str(e)
            }
        )


@router.post("/stream")
async def stream(request: ChatRequest):

    return await stream_chat(request.message)