# progress_tracker.py

import streamlit as st

class ProgressTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_progress(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        return completed_tasks / total_tasks if total_tasks > 0 else 0

    def display_progress(self):
        progress = self.get_progress()
        st.progress(progress)
        st.write(f"Completed: {int(progress * 100)}%")