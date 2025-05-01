

from data import warehouse1, warehouse2

def list_items_by_warehouse():
    for warehouse_name, warehouse in [('warehouse1', warehouse1), ('warehouse2', warehouse2)]:
        print(f"Items in {warehouse_name}:")
        for index , item in enumerate(warehouse , start=1):
            print(f"{index}. {item}")



def search_item(item_name):
    quantities = {'warehouse1': 0, 'warehouse2': 0}

    quantities['warehouse1'] = warehouse1.count(item_name)
    quantities['warehouse2'] = warehouse2.count(item_name)

    for warehouse_name, quantity in quantities.items():
        if quantity > 0:
            print(f"Amount available: {quantity}")
            print(f"Location: {warehouse_name.capitalize()}")  # Capitalize the warehouse name for better readability
            ask_permmision = input('Would you like to order this item?(y/n):- ')
            if ask_permmision == 'y':
                number_of_order = int(input('How many would you like?'))
                if number_of_order >= quantity:
                    print('**************************************************')
                    print(f'There are not this many available. The maximum amount that can be ordered is {quantity}')
                    print('**************************************************')
                    max_order_permission = input('Would you like to order the maximum available?(y/n)')
                    if max_order_permission =='y':
                        print(f'{quantity} Almost new router have been ordered.')
                        break
                if number_of_order < quantity:
                    print(f'{number_of_order} Almost new router have been ordered. ')
                    break
                else:
                    break

                
            else:
                break
        else:
            print(f"Item '{item_name}' not found in {warehouse_name}.")



# YOUR CODE STARTS HERE

# Get the user name
user_name = input('What is your user name?')


# Greet the user
print(f'Hello, {user_name}')
# Show the menu and ask to pick a choice
print('What would you like to do?')
operations = {
    '1': 'List items by warehouse',
    '2': 'Search an item and place an order',
    '3': 'Quit'
}
print_operations = lambda ops: print("\n".join([f"{key}. {value}" for key, value in ops.items()]))

print_operations(operations)
input_text = input('Type the number of the operation: ')


try:
    selected_item = int(input_text)
    if selected_item == 1:
      list_items_by_warehouse()
    elif selected_item == 2:
        # Placeholder for the search and order function
        search_text = input('What is the name of the item?')
        search_item(search_text.strip())
    elif selected_item == 3:
        pass
        
        
    
except ValueError:
    print("**************************************************")
    print(f'{input_text} is not a valid operation.')
    print("**************************************************")


# Execute the operation based on the user's choice


# Thank the user for the visit
print(f'Thank you for your visit, {user_name}!')