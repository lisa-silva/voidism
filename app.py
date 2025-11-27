import streamlit as st
from datetime import datetime

st.set_page_config(page_title="VOIDISM", page_icon="🕳️", layout="centered")

st.title("🕳️ VOIDISM")
st.caption("Scream into the void. Nothing ever escapes. Nothing ever reaches them.")

if "log" not in st.session_state:
    st.session_state.log = []

with st.sidebar:
    st.header("The Rules")
    st.write("• Never reaches your ex")
    st.write("• Never reaches anyone")
    st.write("• Drunk? Use this")
    st.write("• Sober? Read it")
    st.write("• Healed? Burn it")

msg = st.text_area("Say the thing you must never send:", height=180, placeholder="Let it rip…")

col1, col2 = st.columns(2)
with col1:
    if st.button("→ VOID", use_container_width=True):
        if msg.strip():
            st.session_state.log.append({
                "time": datetime.now(),
                "text": msg
            })
            st.success("Swallowed by the void. You stayed strong.")
            st.experimental_rerun()
        else:
            st.warning("Say something first.")
with col2:
    if st.button("🔥 Burn Everything", use_container_width=True):
        if st.checkbox("I’m sure – delete forever"):
            st.session_state.log = []
            st.balloons()
            st.success("Ashes. You’re free.")

if st.session_state.log:
    st.divider()
    st.subheader("📜 Your Void Timeline")
    for entry in reversed(st.session_state.log):
        with st.expander(f"{entry['time'].strftime('%b %d • %I:%M %p')}"):
            st.write(entry["text"])
else:
    st.info("The void is empty… for now.")
