import streamlit as st
def founder_profile():
    st.title("👤 Founder Profile")
    st.session_state["founder_name"] = st.text_input(
        "Founder Name",
        st.session_state.get("founder_name", "")
    )
    st.session_state["startup_name"] = st.text_input(
        "Startup Name",
        st.session_state.get("startup_name", "")
    )
    st.session_state["industry"] = st.selectbox(
        "Industry",
        [
            "AI",
            "SaaS",
            "FinTech",
            "HealthTech",
            "EdTech",
            "Gaming",
            "Marketplace"
        ]
    )
    st.session_state["budget"] = st.selectbox(
        "Budget",
        [
            "< $1k",
            "$1k-$10k",
            "$10k-$50k",
            "$50k+"
        ]
    )
    st.success("Profile Saved ✅")