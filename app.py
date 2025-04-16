import streamlit as st
from utils.load_sample_data import load_sample_resolution
from utils.draft_tools import check_my_draft, rewrite_with_precedent

st.set_page_config(page_title="BlueLines – UNSC Agent", layout="wide")

st.title("🔵 BlueLines – UNSC Drafting Assistant")
st.markdown("Built by **Aperture Futures**")

tab1, tab2 = st.tabs(["🧠 Prompt Lab", "📄 Check My Draft"])

with tab1:
    prompt = st.text_area("Enter your Council drafting prompt here:")
    if st.button("Run Prompt"):
        st.markdown(f"**[Sample output placeholder]** for: {prompt}")
        st.markdown("*(In production, this will fetch precedent-matched clauses and generate full text.)*")

with tab2:
    draft = st.text_area("Paste your draft paragraph:")
    if st.button("Check for Precedent"):
        st.markdown(check_my_draft(draft))
    if st.button("Rewrite for Precedent Match"):
        st.markdown(rewrite_with_precedent(draft))
