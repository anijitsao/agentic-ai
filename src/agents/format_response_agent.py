from agents import Agent

def get_format_response_agent(response_format):
    format_agent=Agent(
        name="FormatResponseAgent",
        instructions="""You are an agent who can
        - Format response based on the response_format given to you

        """,
        output_type=response_format
    )
    return format_agent
