import streamlit as st
import random

def show():

    st.title(
    f"🚀 Welcome {st.session_state.get('founder_name','Founder')}"
)
    st.info(f"""
Startup:
{st.session_state.get("startup_name","Not Set")}

Industry:
{st.session_state.get("industry","Unknown")}

Budget:
{st.session_state.get("budget","Unknown")}
""")
    
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Founder Score", random.randint(70, 99))

    with c2:
        st.metric("Startup Score", random.randint(65, 98))

    with c3:
        st.metric("Runway", f"{random.randint(6,24)} Months")

    with c4:
        st.metric("Burn Rate", f"${random.randint(1000,15000)}")

    st.markdown("---")

    st.subheader("Today's Mission")

    st.checkbox("Talk to 5 users")
    st.checkbox("Ship MVP")
    st.checkbox("Contact investor")
    st.checkbox("Improve landing page")
if st.button("Complete Daily Mission"):

    st.session_state.xp += 20

    if st.session_state.xp >= 100:

        st.session_state.level += 1
        st.session_state.xp = 0

    st.success("🎉 +20 XP Earned!")