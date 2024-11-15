# To-Do List Application

## Project Description
This is a simple command-line interface (CLI) application that allows users to manage a to-do list. It is built using Python and includes functions for adding tasks, viewing tasks, and deleting tasks. The application ensures user-friendly interaction through prompts and handles invalid inputs.

### Why Python Was Used
Python was chosen for this project because of its simplicity and efficiency in building CLI applications. Its built-in data structures, such as lists, are ideal for handling a to-do list. Additionally, Python’s exception handling capabilities allow robust error management.

### Challenges Faced
Some challenges included:
- Implementing proper input validation to ensure smooth user interaction.
- Handling edge cases, such as deleting a task that doesn’t exist or attempting to view tasks in an empty list.

## How to Install and Run the Project
1. Ensure that Python 3.6 or higher is installed on your system.
2. Clone this repository or download the `to_do_list.py` file.
3. Open a terminal and navigate to the directory containing `to_do_list.py`.
4. Run the application using the following command:
   ```bash
   python to_do_list.py

## How to Use the Project
1. Upon starting the application, you will be prompted to enter your name.

2. The main menu will then display the following options:
   - (1) Add to-do list
   - (2) View list
   - (3) Delete from list
   - (4) Quit program

3. Enter the corresponding number to interact with the program:
   - (1) Add to-do list: Add tasks to your list.
   - (2) View list: View all tasks in your list.
   - (3) Delete from list: Remove specific tasks.
   - (4) Quit program: Exit the application.

4. Follow the prompts for each option:
   - Adding Tasks: Enter the tasks you want to add. Type "Quit" to return to the menu.
   - Viewing Tasks: Displays all tasks in the list or informs you if the list is empty.
   - Deleting Tasks: Enter the name of the task to delete. Type "Quit" to return to the menu.
   
5. Use option (4) to quit the program when you're done.