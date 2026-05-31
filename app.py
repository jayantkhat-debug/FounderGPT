import streamlit as st

st.set_page_config(
    page_title="FounderGPT",
    layout="wide"
)

st.title("🚀 FounderGPT")
st.markdown("""
### Build, Plan, and Launch Your Startup

FounderGPT helps entrepreneurs:
- 💡 Generate startup ideas
- 💰 Create business models
- 📈 Build marketing plans
- 🎤 Prepare investor pitches
- 📄 Generate business plans
""")
st.subheader("Your AI Startup Co-Founder")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tools", "5")

with col2:
    st.metric("Startup Stages", "Idea → Funding")

with col3:
    st.metric("Version", "V1")

# Sidebar
st.sidebar.header("Startup Information")

startup_name = st.sidebar.text_input("Startup Name")
industry = st.sidebar.selectbox(
    "Industry",
    [
        "AI",
        "Education",
        "Healthcare",
        "Finance",
        "E-commerce",
        "Real Estate",
        "Travel",
        "Other"
    ]
)

budget = st.sidebar.selectbox(
    "Budget",
    [
        "Under $1,000",
        "$1,000 - $10,000",
        "$10,000 - $50,000",
        "$50,000+"
    ]
)

country = st.sidebar.text_input("Country")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💡 Idea Lab",
    "💰 Business Model",
    "📈 Marketing",
    "🎤 Investor Pitch",
    "📄 Business Plan"
])

with tab1:
    st.header("Startup Idea Lab")

    if st.button("Generate Startup Idea"):

        idea = f"""
        Startup Name: {startup_name if startup_name else 'Future Startup'}

        Industry: {industry}

        Suggested Idea:
        Build a platform in the {industry} industry that helps people save time using automation and AI.

        Target Customers:
        Small businesses, freelancers, and professionals.

        Unique Selling Point:
        Easy to use, affordable, and AI-powered.
        """

        st.success("Startup Idea Generated!")
        st.write(idea)

with tab2:
    st.header("Business Model")

    if st.button("Generate Business Model"):

        model = f"""
        💰 Revenue Streams

        1. Monthly Subscription
        - Basic Plan
        - Premium Plan

        2. Enterprise Services
        - Custom solutions
        - Consulting packages

        3. Advertising Partnerships
        - Sponsored placements
        - Brand collaborations

        📈 Pricing Strategy

        Budget Level: {budget}

        Suggested Launch Price:
        $9.99 - $29.99 per month

        🎯 Customer Acquisition

        - Social media marketing
        - Influencer partnerships
        - Referral programs
        - Content marketing
        """

        st.success("Business Model Generated!")
        st.write(model)

with tab3:
    st.header("Marketing Plan")

    if st.button("Generate Marketing Plan"):

        marketing = f"""
        📈 Marketing Strategy for {startup_name if startup_name else "Your Startup"}

        🎯 Target Market
        - Customers in {country if country else "your target country"}
        - Industry: {industry}

        📱 Social Media Strategy
        - 3 Instagram posts per week
        - 2 TikTok videos per week
        - Daily Stories

        🎥 Content Ideas
        - Behind-the-scenes content
        - Customer success stories
        - Industry tips and tricks
        - Product demonstrations

        🚀 Launch Plan
        Week 1:
        - Create social media pages
        - Launch landing page

        Week 2:
        - Run giveaway campaign
        - Collaborate with influencers

        Week 3:
        - Start paid advertising
        - Collect customer feedback

        Week 4:
        - Optimize marketing campaigns
        - Launch referral program
        """

        st.success("Marketing Plan Generated!")
        st.write(marketing)

with tab4:
    st.header("Investor Pitch")

    if st.button("Generate Investor Pitch"):

        pitch = f"""
🎤 ELEVATOR PITCH

{startup_name if startup_name else "Our Startup"} is a company in the {industry} sector focused on helping customers solve everyday problems faster and more efficiently.

❗ Problem
Many people waste time and money because existing solutions are complicated or outdated.

✅ Solution
Our platform provides a simple, scalable, and technology-driven solution.

🎯 Target Market
Customers in {country if country else "global markets"} looking for better digital experiences.

💰 Business Model
Subscription plans, premium services, and strategic partnerships.

📈 Growth Strategy
Social media marketing, referrals, influencer collaborations, and partnerships.

🚀 Why Invest?
Strong market demand, scalable model, and opportunity for rapid growth.
"""

        st.success("Investor Pitch Generated!")
        st.write(pitch)

with tab5:
    st.header("Business Plan")

    if st.button("Generate Business Plan"):

        plan = f"""
📄 BUSINESS PLAN

Startup Name:
{startup_name if startup_name else "Your Startup"}

Industry:
{industry}

Country:
{country if country else "Target Market"}

━━━━━━━━━━━━━━━━━━

1. Executive Summary

Our startup aims to provide innovative solutions in the {industry} industry.

━━━━━━━━━━━━━━━━━━

2. Problem

Customers often face inefficiencies, high costs, or poor user experiences.

━━━━━━━━━━━━━━━━━━

3. Solution

We offer a simple, technology-driven platform that saves time and improves results.

━━━━━━━━━━━━━━━━━━

4. Target Customers

• Individuals
• Professionals
• Small Businesses
• Enterprise Clients

━━━━━━━━━━━━━━━━━━

5. Revenue Model

• Subscription Plans
• Premium Features
• Consulting Services
• Strategic Partnerships

━━━━━━━━━━━━━━━━━━

6. Marketing Strategy

• Instagram Marketing
• TikTok Content
• Influencer Partnerships
• Referral Programs

━━━━━━━━━━━━━━━━━━

7. Growth Roadmap

Month 1:
Launch MVP

Month 3:
Acquire First Customers

Month 6:
Scale Marketing

Month 12:
Expand Internationally

━━━━━━━━━━━━━━━━━━

8. Funding Requirement

Budget Selected:
{budget}

Funds will be used for product development, marketing, and growth.
"""

        st.success("Business Plan Generated!")
        st.write(plan)
        st.markdown("---")
st.caption("FounderGPT • Built by Jayant")