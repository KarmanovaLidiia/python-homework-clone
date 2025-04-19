class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_done = False  # задача по умолчанию не выполнена

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        status = "✔ Выполнено" if self.is_done else "⏳ Не выполнено"
        return f"{self.description} (до {self.deadline}) — {status}"


# Список задач
tasks = []

# Функции управления задачами
def add_task(description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

def show_pending_tasks():
    for task in tasks:
        if not task.is_done:
            print(task)

# Пример использования:
add_task("Сделать домашку по ООП", "2025-04-20")
add_task("Погладить кота", "2025-04-19")
tasks[0].mark_done()

print("\n📝 Актуальные задачи:")
show_pending_tasks()
