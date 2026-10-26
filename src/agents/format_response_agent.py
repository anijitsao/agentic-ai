from agents import Agent


def get_format_response_agent(response_format):
    format_agent = Agent(
        name="FormatResponseAgent",
        instructions="""You are an agent who can
        - Format response to a JSON output like below,
        {
        "data": {
                    "prompt": "<user prompt>",
                    "response": "<your detailed answers>"
                }
        }
        - Output ONLY raw JSON. Do not include markdown code blocks or conversational text.
        - Do NOT use any markdown formatting (such as **, *, #, or bullet points).
        - Do NOT include newline characters (\\n); keep all text strings on a single line or continuous plain text.
        """,
        # Groq doesn't work output_type while using with Input Guardrails
        # output_type=response_format,
    )
    return format_agent
