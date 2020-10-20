from abc import ABC, abstractmethod


class AbstractRequest(ABC):
    @abstractmethod
    def get_body(self):
        raise NotImplementedError("Not implemented error")
