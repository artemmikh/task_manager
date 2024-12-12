from abc import ABC, abstractmethod


class AbstractCommandDispatcher(ABC):
    @abstractmethod
    def dispatch(self, args) -> None:
        pass
