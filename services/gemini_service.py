from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_test_cases(requirement):

    prompt = f"""
    You are a Senior QA Engineer.

    Generate:
    1. Positive Test Cases
    2. Negative Test Cases
    3. Edge Cases
    4. Security Test Cases

    Requirement:

    {requirement}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def generate_playwright_script(requirement, framework):

    prompt = f"""
    You are a Senior QA Automation Engineer.

    Generate a production-ready {framework} automation script.

    Requirement:

    {requirement}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

def analyze_failure(log):

    prompt = f"""
    You are a Senior QA Automation Architect.

    Analyze this test failure log.

    Provide:

    1. Root Cause
    2. Confidence %
    3. Suggested Fix
    4. Jira Bug Summary

    Log:

    {log}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text