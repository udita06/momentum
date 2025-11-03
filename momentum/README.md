# momentum

## Overview
Momentum is a productivity application built with Python and Streamlit. It features a to-do list, focus sounds, a progress tracker, and integrates with the Gemini API to enhance user experience and productivity.

## Features
- **To-Do List**: Manage tasks efficiently by adding, removing, and tracking completion status.
- **Focus Sounds**: Play, pause, and stop various audio tracks to help maintain concentration while working.
- **Progress Tracker**: Visualize task completion and overall progress to stay motivated and organized.
- **Gemini API Integration**: Fetch data and interact with the Gemini API for enhanced functionality.

## Project Structure
```
momentum
├── src
│   ├── main.py                # Entry point of the Streamlit application
│   ├── components             # UI components for the application
│   │   ├── todo.py            # To-do list component
│   │   ├── focus_sounds.py     # Focus sounds management
│   │   ├── progress_tracker.py  # Progress tracking visualization
│   │   └── sidebar.py         # Sidebar navigation and settings
│   ├── services               # Services for API and audio management
│   │   ├── gemini_client.py   # Gemini API integration
│   │   ├── audio_manager.py    # Audio playback management
│   │   └── storage.py         # Data storage and retrieval
│   ├── models                 # Data models
│   │   └── task.py            # Task model definition
│   └── utils                  # Utility functions
│       └── helpers.py         # Helper functions for data manipulation
├── tests                      # Unit tests for the application
│   └── test_todo.py          # Tests for the to-do list component
├── requirements.txt           # Project dependencies
├── pyproject.toml             # Project configuration
├── .env.example               # Example environment variables
├── .streamlit                 # Streamlit configuration
│   └── config.toml           # Configuration settings for Streamlit
└── README.md                  # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/momentum.git
   ```
2. Navigate to the project directory:
   ```
   cd momentum
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
streamlit run src/main.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.