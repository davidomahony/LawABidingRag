from abc import ABC, abstractmethod
from llama_index.embeddings.openai import OpenAIEmbedding
import os

class LLMModel(ABC):
    @abstractmethod
    def load_data(self, path: str) -> None:
        pass

    @abstractmethod
    def query(self, query: str) -> str:
        pass