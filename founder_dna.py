elif page == "🧬 Founder DNA":

    st.title("🧬 Founder DNA")

    if "leadership" not in st.session_state:

        st.session_state.leadership = random.randint(60,100)
        st.session_state.creativity = random.randint(60,100)
        st.session_state.execution = random.randint(60,100)
        st.session_state.sales = random.randint(40,100)

    st.write("Leadership")
    st.progress(st.session_state.leadership)

    st.write("Creativity")
    st.progress(st.session_state.creativity)

    st.write("Execution")
    st.progress(st.session_state.execution)

    st.write("Sales")
    st.progress(st.session_state.sales)

    st.success(
        "This DNA is unique to your founder profile."
    )