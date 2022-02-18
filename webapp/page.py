from abc import ABC, abstractmethod

class Page(ABC):
    
    @abstractmethod
    def server(self):
        pass