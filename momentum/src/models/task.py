class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __repr__(self):
        return f"Task(title={self.title}, description={self.description}, completed={self.completed})"