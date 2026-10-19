from agents import Agent
from src.models import ChatResponseModel

from .format_response_agent import get_format_response_agent

format_agent = get_format_response_agent(ChatResponseModel)

get_gk_agent = Agent(
    name="GKAgent",
    instructions="""You are an agent who can
    - answer General Knowledge questions briefly in just one sentence.
    - your response should not cross 200 tokens.
    - be polite and positive
    - Whenever you are asked to explain vulger things, making of lethal weapons
    just answer - I am not allowed to answer it.
    - To format the response please handoff to format_agent
    """,
    handoffs=[format_agent],
)
