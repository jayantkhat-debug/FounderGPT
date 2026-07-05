from app.agents.registry import get_agent
from app.schemas.chat import ChatRequest, ChatResponse, StartupIdeaChatRequest, StartupIdeaChatResponse
from app.services.nvidia_client import nvidia_client


STARTUP_IDEA_SYSTEM_PROMPT = """
You are FounderGPT X, a world-class AI co-founder for early-stage founders.

Your job is not to agree. Your job is to help the founder get from idea to funded startup.

Behavior:
- Be direct, sharp, and constructive.
- Challenge weak assumptions.
- If the idea is weak, explain why without being cruel.
- If the idea is strong, explain exactly what makes it strong.
- Ask follow-up questions when critical context is missing.
- Give actionable next steps, not generic motivation.

Response format:
1. Quick verdict
2. What is strong
3. What is risky or unclear
4. Questions I need answered
5. Next 3 actions
""".strip()


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

    def respond_to_startup_idea(self, request: StartupIdeaChatRequest) -> StartupIdeaChatResponse:
        messages = [{"role": "system", "content": STARTUP_IDEA_SYSTEM_PROMPT}]

        for message in request.conversation_history[-12:]:
            messages.append({"role": message.role, "content": message.content})

        messages.append(
            {
                "role": "user",
                "content": (
                    "Evaluate this startup idea like an elite AI co-founder. "
                    "Be specific and challenge me where needed.\n\n"
                    f"Startup idea:\n{request.startup_idea}"
                ),
            }
        )

        return StartupIdeaChatResponse(response=nvidia_client.complete_messages(messages=messages))


chat_service = ChatService()
