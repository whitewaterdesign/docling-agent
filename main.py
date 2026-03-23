from agno.agent import Agent
from agno.models.openai import OpenAIChat

from app.agents.tools.documents import DocumentsTool
from app.core.config import settings

agent = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=settings.openai_api_key),
    tools=[DocumentsTool()],
    instructions=[
        "You are a document conversion assistant.",
        "Use the documents tools to convert files to the requested format.",
        "Supported output formats: markdown, JSON, HTML, text, doctags.",
    ],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    agent.cli_app(stream=False)