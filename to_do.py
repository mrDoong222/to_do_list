print('Welcome! What would you like To-Do?')

to_do_list = []
def update():
    while len(to_do_list) < 20:
        message = input('Would you like to add, remove, update, or exit?')
        if message.lower().strip() == 'add':
            print('What would you like to add?')
            add_message = input()
            to_do_list.append(add_message)
            print('Your current to-do list: ' + str(', '.join(to_do_list)))
        elif message.lower().strip() == 'remove':
            print('What would you like to remove?')
            remove_message = input()
            to_do_list.remove(remove_message)
            print('Your current to-do list: ' + str(', '.join(to_do_list))) 
        elif message.lower().strip() == 'update':
            print('What would you like to update?')
            update_message = input()
            index = to_do_list.index(update_message)
            print('Update to what?')
            new_message = input()
            to_do_list[index] = new_message
            print('Your current to-do list: ' + str(', '.join(to_do_list))) 
        elif message.lower().strip() == 'exit':
            print('goodbye')
            break
        else: 
            print('Error, plese try again')
update()