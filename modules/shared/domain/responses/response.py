from abc import ABC, abstractmethod


class Response(ABC):
    @abstractmethod
    def get_response(self):
        raise NotImplementedError("Not implemented yet")
