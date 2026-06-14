import streamlit as st
from services.gemini_service import generate_qa_artifacts

st.set_page_config(
    page_title="QA-Genius AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 QA-Genius AI")
st.subheader("AI-Powered Test Design & Automation Assistant")

framework = st.selectbox(
    "Select Automation Framework",
    ["Playwright", "Cypress", "Selenium"]
)

requirement = st.text_area(
    "Paste User Story / Requirement",
    height=250
)

if st.button("Generate QA Artifacts"):

    if requirement.strip():

        with st.spinner("Generating QA Artifacts..."):

            result = generate_qa_artifacts(
                requirement,
                framework
            )

        st.markdown(result)

    else:
        st.warning("Please enter a requirement.")