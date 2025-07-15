"""
agents.py

This module defines wrapper classes for each language model agent used by MARVE.
Each agent class exposes a `.query(prompt)` method to accept a prompt string
and return a response. These wrappers provide a consistent interface for GPT,
Claude, and Gemini.

This version connects GPTAgent to the actual OpenAI API using your .env key.
"""

import os
from dotenv import load_dotenv
import openai

load_dotenv()  # Load the API keys from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

class GPTAgent:
    def query(self, prompt):
        # Make a real request to OpenAI's GPT-4 API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response['choices'][0]['message']['content']

# Simulated versions of other agents (for now)
class ClaudeAgent:
    def query(self, prompt):
        return f"[Claude simulated response to: {prompt[:50]}...]"

class GeminiAgent:
    def query(self, prompt):
        return f"[Gemini simulated response to: {prompt[:50]}...]"
