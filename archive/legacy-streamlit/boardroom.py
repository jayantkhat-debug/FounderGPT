import streamlit as st

def show():

    st.title("🏛️ AI Boardroom")

    idea=st.text_area(
        "Describe your startup"
    )

    if st.button("Start Meeting"):

        c1,c2=st.columns(2)

        with c1:

            st.info(
                "👨‍💼 CEO\n\nLaunch quickly and validate."
            )

            st.info(
                "💻 CTO\n\nBuild only MVP."
            )

        with c2:

            st.warning(
                "💰 Investor\n\nNeed stronger traction."
            )

            st.error(
                "⚔️ Competitor\n\nI'd attack your pricing."
            )