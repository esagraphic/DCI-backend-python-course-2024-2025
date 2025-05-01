
from datetime import datetime

from data import stock



def list_items_by_warehouse():
    warehouses = {}

    # Group items by warehouse
    for item in stock:
        warehouse_id = item['warehouse']
        if warehouse_id not in warehouses:
            warehouses[warehouse_id] = []
        warehouses[warehouse_id].append(item)

    # Dictionary to hold total counts
    total_counts = {}

    # Display items and total count in each warehouse
    for warehouse_id, items in warehouses.items():
        print(f"Items in Warehouse {warehouse_id}:")
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item['category']} - {item['state']}")
        total_count = len(items)
        total_counts[warehouse_id] = total_count

    # Print the total items count for all warehouses at the end
    print("Total items in all warehouses:")
    for warehouse_id, count in total_counts.items():
        print(f"Total items in Warehouse {warehouse_id}: {count}")
        
        

def list_by_category():
    # Dictionary to group items by category and count them
    category_counts = {}
    # Dictionary to store items by category
    category_items = {}

    # Populate the dictionaries with counts and items
    for item in stock:
        category_name = item['category']
        if category_name not in category_counts:
            category_counts[category_name] = 0
            category_items[category_name] = []
        category_counts[category_name] += 1
        category_items[category_name].append(item)

    # Print the results sorted by category name
    sorted_categories = sorted(category_counts.items())
    for index, (category_name, count) in enumerate(sorted_categories, start=1):
        print(f"{index}. {category_name} ({count})")

    # Ask the user to select a category
    try:
        selected_index = int(input('Type the number of the category to browse: '))
        if 1 <= selected_index <= len(sorted_categories):
            selected_category = sorted_categories[selected_index - 1][0]
            print(f"\nList of {selected_category}s available:")
            for item in category_items[selected_category]:
                state = item['state']
                warehouse = f"Warehouse {item['warehouse']}"
                print(f"{state} {selected_category}, {warehouse}")
        else:
            print("Invalid category number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def search_item(search_text):
    # Split the input text into state and category
    parts = search_text.split()
    if len(parts) < 2:
        print("Please provide both state and category separated by a space.")
        return
    
    # Assuming the last part is the category and all preceding parts form the state
    category_name = parts[-1]
    state_name = " ".join(parts[:-1])

    # Initialize dictionary to store quantities and dates by warehouse
    quantities = {}

    # Current date for calculating days in stock
    current_date = datetime.now()

    # Search for the item and calculate days in stock
    for item in stock:
        if state_name.lower() in item['state'].lower() and category_name.lower() in item['category'].lower():
            warehouse_key = f"warehouse{item['warehouse']}"
            # Calculate days in stock
            stock_date = datetime.strptime(item['date_of_stock'], '%Y-%m-%d %H:%M:%S')
            days_in_stock = (current_date - stock_date).days
            if warehouse_key not in quantities:
                quantities[warehouse_key] = []
            quantities[warehouse_key].append(days_in_stock)

    # Print results
    if quantities:
        print(f"Location:")
        max_availability = {}
        for warehouse_name, days_list in quantities.items():
            # Print each item's days in stock
            for days in days_list:
                print(f"- {warehouse_name.capitalize()} (in stock for {days} days)")
            # Determine maximum availability
            max_availability[warehouse_name] = len(days_list)

        # Summarize maximum availability
        max_warehouse = max(max_availability, key=max_availability.get)
        print(f"Maximum availability: {max_availability[max_warehouse]} in {max_warehouse.capitalize()}")

        # User decision to order
        ask_permission = input('Would you like to order this item? (y/n): ')
        if ask_permission.lower() == 'y':
            number_of_order = int(input('How many would you like? '))
            if number_of_order > max_availability[max_warehouse]:
                print('**************************************************')
                print(f'There are not this many available. The maximum amount that can be ordered is {max_availability[max_warehouse]}')
                print('**************************************************')
                max_order_permission = input('Would you like to order the maximum available? (y/n): ')
                if max_order_permission.lower() == 'y':
                    print(f'{max_availability[max_warehouse]} {state_name} {category_name} have been ordered.')
                else:
                    print(f'Order cancelled.')
            else:
                print(f'{number_of_order} {state_name} {category_name} have been ordered.')
        else:
            print('Order cancelled.')
    else:
        print(f"Item with state '{state_name}' and category '{category_name}' not found in any warehouse.")



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
    '3': 'Browse by category',
    '4': 'Quit'
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
        list_by_category()
    elif selected_item == 4:
        pass
        
    
except ValueError:
    print("**************************************************")
    print(f'{input_text} is not a valid operation.')
    print("**************************************************")


# Execute the operation based on the user's choice


# Thank the user for the visit
print(f'Thank you for your visit, {user_name}!')