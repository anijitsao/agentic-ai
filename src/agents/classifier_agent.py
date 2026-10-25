from agents import Agent
from src.models import IntentCheck


def get_classifier_agent(instructions: str):
    classifier_agent = Agent(
        name="ClassifierAgent", instructions=instructions, output_type=IntentCheck
    )

    return classifier_agent
