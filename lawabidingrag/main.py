from flask import Flask
from api.controllers.health_check_controller import hc_bp
from api.controllers.version_controller import info_bp
from api.controllers.query_controller import query_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(hc_bp)
app.register_blueprint(info_bp)
app.register_blueprint(query_bp)

if __name__ == '__main__':
    app.run(debug=True)



# from core.LLMModels import OpenAILLMModel

# llm = OpenAILLMModel("gpt-4o", "text-embedding-ada-002", './storage_mini')

# llm.load_data("C:/Users/daver/Desktop/Rag/law/SmallInput")

# # Add a loop to provide options for querying or closing
# while True:
#     print("Options:")
#     print("1. Enter a query string")
#     print("2. Close the program")
#     choice = input("Choose an option (1 or 2): ")
    
#     if choice == '1':
#         query = input("Enter your query: ")
#         resp = llm.query(query)
#         print(resp)
#     elif choice == '2':
#         print("Closing the program.")
#         break
#     else:
#         print("Invalid option. Please choose 1 or 2.")