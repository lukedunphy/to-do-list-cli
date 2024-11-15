# variables to store to do list information and to get name for welcome message
to_do_list = []
name = input('\nEnter your name: ')

# function that will display the menu and allow user to navigate program options and handles input errors
# while loop in function controls all functionality as it handles function calls based on user selection
def menu():
    while True:
        try:
            action = int(input((
            f'\nWelcome {name}! Would you like to (1) add tasks, (2) view tasks,'
            f' (3) delete tasks, or (4) Quit: ')))
        except ValueError:
            print('\nInvalid value entered, please enter a number 1-4\n')
        else:
            if action > 4 or action < 1:
                print('\nMust enter a number 1-4\n')
            else:
                if action in range(1, 5):
                    if action == 1:
                        add_item()
                    elif action == 2:
                        view_list()
                    elif action == 3:
                        delete_task()
                    elif action == 4:
                        break

# function to allow user to add items to list and handle input errors 
def add_item():
    while True:
        item = input('\nEnter tasks to put in your to do list, enter quit to return to menu: ').title().strip()
        if item == 'Quit':
            break
        else:
            to_do_list.append(item)
            print(f'{item} has been added')


# function to display list to users and display message if the list is empty
def view_list():
    if to_do_list != []:
        print('\nHere are the contents of your list: ')
        print()
        for items in to_do_list:
            print(items)
    else:
        print('\nYou do not have any tasks to view in your list')

# function that allows users to delete items from list and alerts them if an item they want to delete is not in the list
def delete_task():
    print(f'\nHere is your current to do list: {to_do_list}')
    while True:
        deleted_item = input('\nEnter the item name you want to delete, enter quit to return to menu: ').title().strip()
        if deleted_item in to_do_list:
            to_do_list.remove(deleted_item)
            print(f'\n{deleted_item} has been removed from the list')
            print(f'\nHere is your updated to do list {to_do_list}')
        elif deleted_item == 'Quit':
            break
        elif deleted_item not in to_do_list:
            print(f'\n{deleted_item} is not in your list')

# function call to allow user to interact with the program 
menu()