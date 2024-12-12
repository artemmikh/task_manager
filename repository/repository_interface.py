from abc import ABC, abstractmethod
from typing import List
from models.task import Task


class AbstractTaskRepository(ABC):
    @abstractmethod
    def load_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def save_tasks(self, tasks: List[Task]) -> None:
        pass
