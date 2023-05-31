# Todo List App

This is a simple Todo List application built with Python and Tkinter. It allows you to add tasks, delete tasks, and persist tasks between sessions.

This application is based on the YouTube tutorial ["Build a To-Do List App with Python | GUI Tkinter Project"](https://www.youtube.com/watch?v=T60cEaVYMJE&t=149s) by Parvat Computer Technology. 

## File Structure

- `main.py`: This is the main Python script that runs the application.
- `Image/`: This directory contains the images used in the application.

## How to Run

1. Ensure you have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).
2. Clone this repository to your local machine.
3. Navigate to the directory containing the `main.py` file in your terminal.
4. Run the command `python main.py` to start the application.

## Application Features

- **Add Task**: You can add a new task by typing it into the entry field and clicking the "ADD" button. The task will appear in the list below.
- **Delete Task**: You can delete a task by selecting it in the list and clicking the "Delete" button.
- **Persistence**: The tasks are stored in a file named `tasklist.txt`. This allows the tasks to persist between different sessions of the application. If the `tasklist.txt` file does not exist, the application will create it.

## Application Interface

The application has a simple and intuitive interface. It includes a top bar with an application icon and a heading. The main part of the application contains an entry field for adding tasks and a listbox for displaying the tasks. There is also a "Delete" button at the bottom for deleting tasks.

## Dependencies

This application uses the Tkinter library for the GUI. Tkinter comes pre-installed with Python, so you don't need to install it separately.

## Contributing

Feel free to fork this repository and make changes. If you have any ideas or suggestions, please open an issue or make a pull request.

## License

This project is licensed under the terms of the MIT license.
