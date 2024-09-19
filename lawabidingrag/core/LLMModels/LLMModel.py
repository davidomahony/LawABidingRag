from abc import ABC, abstractmethod

class LLMModel(ABC):
    @abstractmethod
    def load_data(self, path: str) -> None:
        pass

    @abstractmethod
    def query(self, query: str) -> str:
        pass