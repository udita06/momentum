def save_tasks(tasks):
    import json
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def load_tasks():
    import json
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []