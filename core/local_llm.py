from llama_cpp import Llama

class LocalLLM:
    def __init__(self, model_path, n_ctx=4096):
        self.llm = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_threads=8
        )

    def generate(self, prompt):
        output = self.llm(
            f"<s>[INST]{prompt}[/INST]",
            max_tokens=512,
            temperature=0.7
        )
        return output["choices"][0]["text"]
