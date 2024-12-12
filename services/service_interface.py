from abc import ABC, abstractmethod
from typing import Optional


class AbstractTaskManager(ABC):
    @abstractmethod
    def add_task(self, **criteria) -> None:
        pass

    @abstractmethod
    def list_task(self, all: Optional[bool] = False,
                  **criteria: Optional[str]) -> None:
        pass

    @abstractmethod
    def remove_task(self, **criteria: Optional[str]) -> None:
        pass

    @abstractmethod
    def search_task(self, **criteria: Optional[str]) -> None:
        pass

    @abstractmethod
    def edit_task(self, **criteria: Optional[str]) -> None:
        pass
