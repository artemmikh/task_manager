from dataclasses import dataclass, asdict


@dataclass
class Task:
    """Представляет задачу с различными аттрибутами."""
    id: int
    title: str
    description: str = "Нет описания"
    category: str = "Общая"
    due_date: str = "Не указана"
    priority: str = "Низкий"
    status: str = "Новая"

    def to_dict(self) -> dict:
        """Преобразует объект Task в словарь."""
        return asdict(self)
