import os
from configparser import ConfigParser

class LLM:
    def __init__(self, provider="openai"):
        self.provider = provider

    def generate(self, prompt):
        if self.provider == "openai":
            return self.openai_call(prompt)
        else:
            return self.local_call(prompt)

    def openai_call(self, prompt):
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def local_call(self, prompt):
        # Placeholder for llama.cpp / GPT4All
        return f"[LOCAL MODEL RESPONSE] {prompt}"
