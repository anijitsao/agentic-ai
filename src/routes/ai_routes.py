from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from src.agents.history_agent import create_history_agent
from src.utils.ollama_client_util import ollama_client

router = APIRouter(tags=["egentic-ai"])


@router.get("/question/")
async def main(req: Request, query: str = "what is python?"):
    try:
        # print("result: ", result.text)

        async def stream():
            # Streaming the response to save time
            agent = await create_history_agent(req.app.state.ollama_client)

            result = await agent.run(
                query,
                stream=True,
            )
            async for chunk in result:
                if chunk.text:
                    # print(chunk.text, end="", flush=True)
                    yield f"{chunk.text}"

        return StreamingResponse(stream(), media_type="text/event-stream")
    except Exception as e:
        print("error occcurred", e)
