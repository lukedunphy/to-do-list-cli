# global variables and welcome message
to_do_list = []
name = input('Enter your name: ').title().strip()
print(f'\nWelcome {name}!')


# function is called when user enters 1 in menu
def add_list():
    """
    Prompts user to enter items to append to their to do list.
    Loop stops when user enters 'quit'.
    """
    while True:
        list_items = input("Enter items that you want to add to your list, " +
                           "enter 'Quit' to return to menu: \n").title().strip()
        if list_items != 'Quit':
            to_do_list.append(list_items)
        else:
            break
    return to_do_list
    

# function is called when user enters 2 in menu
def view_list():
    """
    Loops through all items in user's list and prints each item in terminal.
    Checks if list is empty and alerts user if it is.
    """
    if to_do_list != []:
        print(f"{name}'s To Do List:")
        print('-' * 15)
        for item in to_do_list:
            print(f'- {item}')
        print('-' * 15)
    else:
        print('Your to do list is empty.') 


# function is called when user enters 3 in menu
def delete_from_list():
    """
    Allows user to enter an item they want to delete from list.
    User may enter as many items as they want and can exit by entering 'quit'.
    """
    while True:
        if not to_do_list:
            print('Your list is empty.')
            break
        deleted_item = input('Enter item you want to delete from list, enter ' 
                            + '"Quit" to return to menu: ' ).title().strip()
        if deleted_item == 'Quit':
            break
        elif deleted_item in to_do_list:
            to_do_list.remove(deleted_item)
        else:
            print(f'{deleted_item} is not in your list.')


def menu():
    """
    Displays menu to user and allows them to select what part of program they
    want to interact with.
    Controls functionality of program and allows user to exit the program by
    entering the integer '4'
    """
    while True:
        try:
            print("\nPlease select an option:")
            print("1. Add to-do list")
            print("2. View list")
            print("3. Delete from list")
            print("4. Quit program")
            selection = int(input("\nEnter a number (1-4): "))
        except ValueError:
            print('Invalid value entered, enter a number 1-4: ')
        else:
            if selection == 1:
                add_list()
            if selection == 2:
                view_list()
            if selection == 3:
                delete_from_list()
            if selection == 4:
                break

# call menu() to start program after getting users name and displaying
# welcome message
menu()