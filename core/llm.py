from core.local_llm import LocalLLM
import os

class LLM:
    def __init__(self, provider="local"):
        if provider == "local":
            self.engine = LocalLLM(
                model_path="models/mistral-7b-instruct.gguf"
            )
        else:
            self.engine = None

    def generate(self, prompt):
        return self.engine.generate(prompt)
