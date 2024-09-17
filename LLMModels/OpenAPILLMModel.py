from abc import ABC, abstractmethod
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.readers.simple_directory_reader import SimpleDirectoryReader
from LLMModel import LLMModel  # Updated import statement
import os

class OpenAILLMModel(LLMModel):
    def __init__(self, api_key: str, model_name: str, persist_dir: str):
        self.api_key = api_key
        self.model_name = model_name
        self.persist_dir = persist_dir
        self.documents = None
        self.embed_model = OpenAIEmbedding(api_key=self.api_key, model_name=self.model_name)

    def load_data(self, path: str) -> None:
        self.documents = SimpleDirectoryReader(path).load_data()

    def query(self, query: str) -> str:
        # Implement the query logic using self.documents and self.embed_model
        # This is a placeholder implementation
        return "Query result for: " + query

# Usage example
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

model = OpenAILLMModel(api_key=api_key, model_name="text-embedding-ada-002", persist_dir="./storage_mini")
model.load_data("C:/Users/daver/Desktop/Rag/law/NotAsSmall")
result = model.query("Example query")
print(result)