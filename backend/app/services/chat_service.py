from app.agents.registry import get_agent
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.nvidia_client import nvidia_client


class ChatService:
    def respond(self, request: ChatRequest) -> ChatResponse:
        agent = get_agent(request.agent_key)
        prompt = (
            f"{agent.system_prompt}\n\n"
            f"Workflow: {request.workflow}\n"
            "Use this response structure: critical assessment, follow-up questions if needed, recommended next actions."
        )
        content = nvidia_client.complete(system_prompt=prompt, user_message=request.message)

        return ChatResponse(
            agent_key=agent.key,
            content=content,
            follow_up_questions=[],
            memory_updates=[],
            suggested_tasks=[],
        )


chat_service = ChatService()
