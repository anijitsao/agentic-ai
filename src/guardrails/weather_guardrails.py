from agents.decorators import input_guardrail

from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
)


@input_guardrail
async def classify_input_guardrails(
    ctx: RunContextWrapper[dict], agent: Agent, input
) -> GuardrailFunctionOutput:

    # 1. Dynamically extract the pre-built classifier agent from runtime context
    classifier_agent = ctx.context.get("classifier_agent")

    if not classifier_agent:
        raise ValueError(
            "Missing 'classifier_agent' inside the runtime execution context."
        )
    result = await Runner.run(classifier_agent, input=input, context=ctx.context)
    intent = result.final_output

    return GuardrailFunctionOutput(
        output_info=intent.reasoning,
        tripwire_triggered=not intent.is_information_related,
    )
