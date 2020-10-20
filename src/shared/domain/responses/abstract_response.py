from abc import ABC, abstractmethod


class AbstractResponse(ABC):
    @abstractmethod
    def get_response(self):
        raise NotImplementedError("Not implemented yet")
