import streamlit as st
from components.todo import Todo
from components.progress_tracker import ProgressTracker
from components.sidebar import display_sidebar
from services.gemini_client import GeminiClient

def main():
    st.title("Momentum App")

    # Initialize sidebar
    theme, page = display_sidebar()

    # Initialize components
    todo = Todo()
    progress_tracker = ProgressTracker()

    # Display components
    st.header("To-Do List")
    todo.display()

    st.header("Progress Tracker")
    progress_tracker.display_progress()

    # Gemini API integration removed; focus on To-Do List and Progress Tracker only

if __name__ == "__main__":
    main()