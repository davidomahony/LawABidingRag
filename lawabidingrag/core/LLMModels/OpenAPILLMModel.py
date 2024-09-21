from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader, 
    StorageContext, 
    load_index_from_storage
)
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
import os

from .LLMModel import LLMModel  # Updated import statement

import os

class OpenAILLMModel(LLMModel):
    def __init__(self, model_name: str, text_model: str, persist_dir: str):
        self.model_name = model_name
        self.persist_dir = persist_dir
        self.documents = None
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
        self.embed_model = OpenAIEmbedding(
            api_key=api_key,
            model_name=text_model
        )
        # Set the global settings
        Settings.llm = OpenAI(model=model_name, temperature=0.1)
        Settings.embed_model = OpenAIEmbedding(model=text_model, embed_batch_size=100)
        Settings.node_parser = SemanticSplitterNodeParser(embed_model=self.embed_model, chunk_size=512, chunk_overlap=20)
        self.embed_model = OpenAIEmbedding(api_key=api_key, model_name=self.model_name)
        self.query_engine = None

    def load_data(self, path: str) -> None:
        self.documents =  SimpleDirectoryReader(path).load_data()
        print("Documents loaded successfully")
        vector_index = VectorStoreIndex.from_documents(self.documents, show_progress=True)
        vector_index.storage_context.persist(persist_dir=self.persist_dir)
        storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
        # Load the index from storage
        index = load_index_from_storage(storage_context)
        # Create the query engine
        self.query_engine = index.as_query_engine()
        print("Data loaded successfully")

    def query(self, query: str) -> str:
        self.load_data('C:/Users/daver/Desktop/Rag/law/SmallInput')
        ## Foails just below here for now
        response = self.query_engine.query(query)
        return response
