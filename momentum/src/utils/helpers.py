def format_task(task):
    return f"{task['title']} - {'✔️' if task['completed'] else '❌'}"

def calculate_progress(tasks):
    if not tasks:
        return 0
    completed_tasks = sum(1 for task in tasks if task['completed'])
    return (completed_tasks / len(tasks)) * 100

def load_tasks_from_storage(storage):
    return storage.load_tasks()

def save_tasks_to_storage(storage, tasks):
    storage.save_tasks(tasks)

def validate_task_data(task_data):
    if not task_data.get('title'):
        raise ValueError("Task title is required.")
    return True