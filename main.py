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

# Ensure your API key is set correctly
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

persist_dir = "./storage_mini"

documents = SimpleDirectoryReader("C:/Users/daver/Desktop/Rag/law/NotAsSmall").load_data()

# Use Azure's OpenAI embedding model
embed_model = OpenAIEmbedding(
    api_key=api_key,
    model_name="text-embedding-ada-002"
)

# Set the global settings
Settings.llm = OpenAI(model="gpt-4o", temperature=0.1)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small", embed_batch_size=100)
Settings.node_parser = SemanticSplitterNodeParser(embed_model=embed_model, chunk_size=512, chunk_overlap=20)

# Create the index and storage context
vector_index = VectorStoreIndex.from_documents(documents, show_progress=True)

vector_index.storage_context.persist(persist_dir=persist_dir)

storage_context = StorageContext.from_defaults(persist_dir=persist_dir)

# Load the index from storage
index = load_index_from_storage(storage_context)

# Create the query engine
query_engine = index.as_query_engine()

# Add a loop to provide options for querying or closing
while True:
    print("Options:")
    print("1. Enter a query string")
    print("2. Close the program")
    choice = input("Choose an option (1 or 2): ")
    
    if choice == '1':
        query = input("Enter your query: ")
        resp = query_engine.query(query)
        print(resp)
    elif choice == '2':
        print("Closing the program.")
        break
    else:
        print("Invalid option. Please choose 1 or 2.")