# app/analyzer.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_contract(text):
    prompt = f"""
You are a legal AI assistant. Analyze the following contract text and return a structured JSON object with:
- summary: a short overview in plain English
- clauses: list important clauses like termination, payment, liability, confidentiality with a short explanation each.

Contract Text:
{text[:3000]}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
