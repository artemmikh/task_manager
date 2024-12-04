# Task Manager

Task Manager — это консольное приложение для управления задачами. Вы можете
добавлять, редактировать, удалять и искать задачи, а также просматривать список
всех задач или задач по категориям.

## Основные функции

- Добавление новой задачи с различными атрибутами (название, описание,
  категория, срок выполнения, приоритет, статус).
- Удаление задач по ID или категории.
- Редактирование существующих задач.
- Поиск задач по ключевым словам, категориям или статусам.
- Просмотр всех задач или задач, отфильтрованных по категории.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/artemmikh/task_manager
   cd task-manager
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Для Windows: venv\Scripts\activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Использование

### Запуск программы

Для работы приложения используйте команду:

```bash
python main.py <команда> [аргументы]
```

### Команды

| Команда  | Описание                 | Аргументы                                                                                |
|----------|--------------------------|------------------------------------------------------------------------------------------|
| `add`    | Добавить новую задачу    | `--title`, `--description`, `--category`, `--due_date`, `--priority`, `--status`         |
| `list`   | Просмотреть список задач | `--all` (показать все задачи), `--category` (показать задачи по категории)               |
| `remove` | Удалить задачу           | `--id` (удалить по ID), `--category` (удалить все задачи в категории)                    |
| `search` | Искать задачи            | `--keyword` (по ключевым словам), `--category`, `--status`                               |
| `edit`   | Редактировать задачу     | `--id`, `--title`, `--description`, `--category`, `--due_date`, `--priority`, `--status` |

Пример:
(Чтобы передать аргументы с пробелами, их нужно заключать в кавычки)

```bash
python main.py add --title "Закончить проект" --description "Создание 
менеджера задач" 
--category Работа --due_date 2024-12-06 --priority высокий
--status "не выполнена"
```

### Формат данных

Программа использует JSON-файл (`tasks.json`) для хранения задач. Каждая задача
сохраняется в следующем формате:

```json
{
  "id": 1,
  "title": "Пример задачи",
  "description": "Описание задачи",
  "category": "Работа",
  "due_date": "2024-12-06",
  "priority": "высокий",
  "status": "не выполнена"
}
```

## Тестирование

Приложение покрыто тестами, написанными с использованием Pytest. Для запуска
тестов выполните:

```bash
pytest
```

## Требования

- Python 3.8+
- Зависимости указаны в `requirements.txt`.

## Структура проекта

```plaintext
task-manager/
│
├── main.py                 # Основной файл для запуска приложения
├── task_manager.py         # Логика управления задачами
├── configs.py              # Конфигурации и парсинг аргументов
├── tests/                  # Папка с тестами
│   ├── test_task_manager.py
│   ├── test_commands.py
│   └── ...
├── tasks.json              # База данных задач (автоматически создается)
├── requirements.txt        # Зависимости проекта
└── README.md               # Документация
```