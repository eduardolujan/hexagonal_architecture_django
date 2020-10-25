from abc import ABC, abstractmethod


class Request(ABC):
    @abstractmethod
    def get_body(self):
        raise NotImplementedError("Not implemented error")
