from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def generate_qa_artifacts(requirement, framework):

    prompt = f"""
You are a Senior QA Automation Architect.

Analyze the following requirement and generate:

1. Positive Test Cases
2. Negative Test Cases
3. Edge Cases
4. Security Test Cases
5. API Test Scenarios
6. Automation Script using {framework}

Requirement:
{requirement}

Format the response in Markdown with clear headings.

For automation scripts:
- If Playwright selected, generate Playwright code.
- If Cypress selected, generate Cypress code.
- If Selenium selected, generate Python Selenium code.

Keep the automation script production-ready and well commented.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text