class TaskStore:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, name):
        if not isinstance(task_id, int):
            raise ValueError("task_id must be an integer")

        if not isinstance(name, str):
            raise ValueError("name must be a string")

        if not name.strip():
            raise ValueError("name cannot be empty")

        self.tasks[task_id] = {
            "id": task_id,
            "name": name,
            "done": False
        }

    def get_task(self, task_id):
        if not isinstance(task_id, int):
            raise ValueError("task_id must be an integer")

        return self.tasks.get(task_id)

    def mark_done(self, task_id):
        if not isinstance(task_id, int):
            raise ValueError("task_id must be an integer")

        if task_id in self.tasks:
            self.tasks[task_id]["done"] = True
            return True

        return False


print("USING OPTIMIZED VERSION")
