from fastapi import APIRouter
from solar_recommender.app.agents.super_agent import super_agent

router = APIRouter()

@router.post("/chat")
async def handle_chat(message: dict):
    """
    This endpoint will handle the user's chat messages.
    It will receive a message, pass it to the Super-Agent,
    and return the agent's response.
    """
    user_message = message.get("message", "")

    # Pass the message to the Super-Agent
    agent_response = super_agent.process(user_message)

    return {"response": agent_response}
