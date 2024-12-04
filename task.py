from typing import Dict, Union


class Task:
    """Представляет задачу с различными аттрибутами."""

    def __init__(self,
                 id: int,
                 title: str,
                 description: str,
                 category: str,
                 due_date: str,
                 priority: str,
                 status: str) -> None:
        """Инициализирует задачу с указанными аттрибутами."""
        self.id: int = id
        self.title: str = title
        self.description: str = description
        self.category: str = category
        self.due_date: str = due_date
        self.priority: str = priority
        self.status: str = status

    def to_dict(self) -> Dict[str, Union[int, str]]:
        """Конвертирует задачу в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }
