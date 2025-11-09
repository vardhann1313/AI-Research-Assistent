# Inbuilt imports
from fastapi import APIRouter

# Custom imports
from app.Agents.agentManager import agent_manager

# Router object
AgentRouter = APIRouter()

# Health check API route
@AgentRouter.get("/health_check")
async def check():
    return {
        "active_agents": len(agent_manager._agents),
        "max_agents": agent_manager.MAX_AGENTS
    }

