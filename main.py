from connection import config
from agents import Agent , Runner , ModelSettings 

async def expo(user_question):
    agent = Agent(
        name = "chemico",
        instructions = "you are a helpful agent for chemical engineers of NED university in every aspect . Guide user in every question in chemical engineering way.",
        model_settings = ModelSettings(
                top_p=0.5,
                presence_penalty=1.5,
            )
    )

    results = await Runner.run(
        agent,
        input = str(user_question),
        run_config = config
    )

    return results.final_output