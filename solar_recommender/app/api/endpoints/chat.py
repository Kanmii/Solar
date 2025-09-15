from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
async def handle_chat(message: dict):
    """
    This endpoint will handle the user's chat messages.
    It will receive a message, pass it to the Super-Agent,
    and return the agent's response.
    """
    # TODO: Get user message from the request
    user_message = message.get("message", "")

    # TODO: Pass the message to the Super-Agent
    # agent_response = super_agent.process(user_message)

    # For now, return a dummy response
    agent_response = f"You said: {user_message}"

    return {"response": agent_response}
