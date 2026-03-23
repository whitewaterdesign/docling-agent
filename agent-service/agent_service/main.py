from agno.os.app import AgentOS
from agno.os.interfaces.agui import AGUI

from app.agents.document_agent import document_agent

agent_os = AgentOS(
    agents=[document_agent],
    interfaces=[AGUI(agent=document_agent)],
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve("agent_service.main:app", host="0.0.0.0", port=7777, reload=True)
