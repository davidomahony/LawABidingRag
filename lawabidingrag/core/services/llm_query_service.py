from ..LLMModels.OpenAPILLMModel import OpenAILLMModel


class llm_query_service():
    def __init__(self, llm_type: str):
        if (llm_type == "OPENAI"):
            self.llm = OpenAILLMModel("gpt-4o", "text-embedding-ada-002", './storage_mini')

    def basic_query(self, query: str) -> str:
        ## i need some sort of validation here
        if (query == ""):
            return "Query cannot be empty"
        ## should check for names or pii stuff

        return self.llm.query(query)