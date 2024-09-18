from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader, 
    StorageContext, 
    ServiceContext, 
    load_index_from_storage
)
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.readers.smart_pdf_loader import SmartPDFLoader
from llama_index.llms.openai import OpenAI
from llama_index.core import (download_loader, Settings)
import os

from lawabidingrag.LLMModels import OpenAILLMModel

llm = OpenAILLMModel("gpt-4o", "text-embedding-ada-002", './storage_mini')

llm.load_data("C:/Users/daver/Desktop/Rag/law/SmallInput")

# Add a loop to provide options for querying or closing
while True:
    print("Options:")
    print("1. Enter a query string")
    print("2. Close the program")
    choice = input("Choose an option (1 or 2): ")
    
    if choice == '1':
        query = input("Enter your query: ")
        resp = llm.query(query)
        print(resp)
    elif choice == '2':
        print("Closing the program.")
        break
    else:
        print("Invalid option. Please choose 1 or 2.")