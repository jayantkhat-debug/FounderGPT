from app.models import ProjectMemory
from app.services.nvidia_client import nvidia_client

BUSINESS_MODEL_SYSTEM_PROMPT = """
You are FounderGPT X, a world-class AI business strategist.
Your goal is to generate a comprehensive business model for a startup based on its current profile.

Focus on:
1. Revenue Streams: How will the startup make money?
2. Pricing Strategy: Suggested price points and logic.
3. Customer Acquisition: How to get the first 100 customers.
4. Unit Economics: Estimated CAC and LTV considerations.

Be specific, actionable, and direct. Avoid generic advice.
""".strip()

class GeneratorService:
    def generate_business_model(self, memory: ProjectMemory) -> str:
        project_context = (
            f"Startup Name: {memory.startup_name or 'Unknown'}\n"
            f"Problem: {memory.problem or 'Not defined'}\n"
            f"Solution: {memory.solution or 'Not defined'}\n"
            f"Target Customer: {memory.customer or 'Not defined'}\n"
            f"Current Revenue Model: {memory.revenue_model or 'Not defined'}"
        )

        user_message = (
            "Based on the following startup context, generate a detailed business model.\n\n"
            f"Context:\n{project_context}"
        )

        return nvidia_client.complete(
            system_prompt=BUSINESS_MODEL_SYSTEM_PROMPT,
            user_message=user_message
        )

generator_service = GeneratorService()
