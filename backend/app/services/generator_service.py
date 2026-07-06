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

    def generate_financial_model(self, memory: ProjectMemory) -> str:
        project_context = (
            f"Startup Name: {memory.startup_name or 'Unknown'}\n"
            f"Problem: {memory.problem or 'Not defined'}\n"
            f"Solution: {memory.solution or 'Not defined'}\n"
            f"Target Customer: {memory.customer or 'Not defined'}\n"
            f"Revenue Model: {memory.revenue_model or 'Not defined'}"
        )

        prompt = """
You are FounderGPT X, a CFO-level AI strategist.
Generate a high-level financial model outline for this startup.

Include:
1. Startup Costs: Initial investment needed to launch.
2. Variable & Fixed Costs: Monthly burn estimate.
3. Revenue Projections: Year 1 monthly targets.
4. Break-even Analysis: How many customers/sales are needed to reach break-even.
5. Key Metrics: CAC targets, LTV expectations.

Be realistic, data-driven, and specific to the industry.
""".strip()

        user_message = (
            "Generate a realistic financial model for the following startup.\n\n"
            f"Context:\n{project_context}"
        )

        return nvidia_client.complete(system_prompt=prompt, user_message=user_message)

    def generate_business_plan(self, memory: ProjectMemory) -> str:
        project_context = (
            f"Startup Name: {memory.startup_name or 'Unknown'}\n"
            f"Problem: {memory.problem or 'Not defined'}\n"
            f"Solution: {memory.solution or 'Not defined'}\n"
            f"Target Customer: {memory.customer or 'Not defined'}\n"
            f"Revenue Model: {memory.revenue_model or 'Not defined'}\n"
            f"Pricing/Financials: {memory.pricing or 'Not defined'}"
        )

        prompt = """
You are FounderGPT X, an expert startup consultant.
Generate a comprehensive, professional Business Plan for this startup.

Structure the plan with these sections:
1. Executive Summary
2. Problem Statement & Market Pain
3. Solution & Product Value Proposition
4. Market Analysis & Opportunity
5. Business Model & Revenue Strategy
6. Go-to-Market & Marketing Plan
7. Operational Roadmap (Next 12 Months)
8. Financial Highlights & Funding Requirement

Be extremely thorough, specific, and professional. Use markdown formatting.
""".strip()

        user_message = (
            "Generate a complete Business Plan based on this startup context.\n\n"
            f"Context:\n{project_context}"
        )

        return nvidia_client.complete(system_prompt=prompt, user_message=user_message)

    def generate_web3_strategy(self, memory: ProjectMemory) -> str:
        project_context = (
            f"Startup Name: {memory.startup_name or 'Unknown'}\n"
            f"Problem: {memory.problem or 'Not defined'}\n"
            f"Solution: {memory.solution or 'Not defined'}"
        )

        prompt = """
You are FounderGPT X, a Web3 & Crypto strategist.
Generate a strategy for integrating Web3 or Crypto into this business to create new value or revenue.

Include:
1. Tokenomics: How a token could be used (if applicable).
2. Decentralized Benefits: Why decentralization matters here.
3. Crypto Revenue Streams: How to earn through crypto (staking, fees, etc.).
4. Technical Requirements: Smart contract or chain considerations.
5. Risks: Regulatory and market risks specific to crypto.

Be specific and focus on sustainable value, not hype.
""".strip()

        user_message = (
            "Generate a Web3 and Crypto strategy for the following startup.\n\n"
            f"Context:\n{project_context}"
        )

        return nvidia_client.complete(system_prompt=prompt, user_message=user_message)

    def generate_pitch_deck(self, memory: ProjectMemory) -> str:
        project_context = (
            f"Startup Name: {memory.startup_name or 'Unknown'}\n"
            f"Problem: {memory.problem or 'Not defined'}\n"
            f"Solution: {memory.solution or 'Not defined'}\n"
            f"Target Customer: {memory.customer or 'Not defined'}\n"
            f"Revenue Model: {memory.revenue_model or 'Not defined'}"
        )

        prompt = """
You are FounderGPT X, a specialist in venture capital and startup storytelling.
Generate a compelling 10-12 slide Pitch Deck outline for this startup.

For each slide, provide:
- Slide Title
- Key Message (The "So What?")
- Recommended Visuals/Data Points
- Talking Points for the Founder

Slides should include:
1. Vision & Value Prop
2. The Problem
3. The Solution
4. Market Opportunity (TAM/SAM/SOM)
5. Product/Technology
6. Revenue Model
7. Traction & Roadmap
8. Competitive Landscape
9. The Team (Generic placeholders)
10. The Ask (Funding requirements)

Be punchy, persuasive, and focus on the narrative.
""".strip()

        user_message = (
            "Generate a high-conversion pitch deck outline for the following startup.\n\n"
            f"Context:\n{project_context}"
        )

        return nvidia_client.complete(system_prompt=prompt, user_message=user_message)

generator_service = GeneratorService()
