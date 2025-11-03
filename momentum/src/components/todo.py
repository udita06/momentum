import streamlit as st

class Todo:
    def __init__(self):
        if 'tasks' not in st.session_state:
            st.session_state['tasks'] = []

    def display(self):
        st.subheader("Your Tasks")
        tasks = st.session_state['tasks']
        for task in tasks:
            checked = st.checkbox(task['title'], value=task['completed'], key=f"task_{task['id']}")
            task['completed'] = checked
        new_task = st.text_input("Add a new task", key="new_task")
        if st.button("Add Task"):
            self.add_task(new_task)
            st.experimental_rerun()

    def add_task(self, title):
        if title:
            tasks = st.session_state['tasks']
            new_task = {
                'id': len(tasks) + 1,
                'title': title,
                'completed': False
            }
            tasks.append(new_task)

    def remove_task(self, task_id):
        tasks = st.session_state['tasks']
        st.session_state['tasks'] = [task for task in tasks if task['id'] != task_id]