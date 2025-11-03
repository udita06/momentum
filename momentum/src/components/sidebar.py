from streamlit import sidebar

def display_sidebar():
    sidebar.title("Momentum App")
    sidebar.header("Settings")
    
    # User preferences
    theme = sidebar.selectbox("Select Theme", ["Light", "Dark"])
    sidebar.write(f"Current Theme: {theme}")
    
    # Navigation options
    page = sidebar.radio("Go to", ["To-Do List", "Focus Sounds", "Progress Tracker"])
    sidebar.write(f"Selected Page: {page}")
    
    return theme, page

def show_sidebar_options():
    theme, page = display_sidebar()
    return theme, page