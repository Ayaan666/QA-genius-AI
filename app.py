import streamlit as st
from services.gemini_service import (
    generate_test_cases,
    generate_playwright_script,
    analyze_failure
)

st.title("QA-Genius AI")

requirement = st.text_area("Enter Requirement")

framework = st.selectbox(
    "Automation Framework",
    ["Playwright", "Cypress", "Selenium"]
)

if st.button("Generate Test Cases"):
    output = generate_test_cases(requirement)
    st.write(output)

if st.button("Generate Automation Script"):
    script = generate_playwright_script(requirement, framework)
    st.code(script, language="typescript")

    st.divider()

st.subheader("AI Failure Analysis")

failure_log = st.text_area(
    "Paste Failure Log",
    height=200
)

if st.button("Analyze Failure"):
    analysis = analyze_failure(failure_log)
    st.write(analysis)