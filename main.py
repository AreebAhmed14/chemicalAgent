
from dotenv import load_dotenv
from agents import AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig , Agent , Runner , ModelSettings 
import os

load_dotenv()

gemini_api_key = os.getenv("gemini_key")

if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

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