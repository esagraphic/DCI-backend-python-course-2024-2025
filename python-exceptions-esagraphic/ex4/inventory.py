from decimal import Decimal

# Ex1: Custom Exceptions
class OutOfStock:
    # TODO: Change this to a custom exception base on the instructions
    pass

class PaymentError:
    # TODO: Change this to a custom exception base on the instructions
    pass

class InvalidItemTypeError:
    # TODO: Change this to a custom exception base on the instructions
    pass

# Items
#### Category
from enum import Enum

class ItemCategoryEnum(str, Enum):
    PHONE='PH'
    TV='TV'
    LAPTOP='LT'

## ItemBase
class ItemBase:
    def __init__(self, name: str, category: ItemCategoryEnum, in_stock: int, price: Decimal) -> None:
        self.name = name
        self.category = category
        self.in_stock = in_stock
        self.price = price


# Specific items

class Iphone(ItemBase):
    pass

class TV(ItemBase):
    pass

class Macbook(ItemBase):
    pass

# Inventory System

class InventorySystem:
    def __init__(self, *items: ItemBase) -> None:
        # TODO: Assign all items to __stock as a list
        self.__stock: list[ItemBase] = # TODO; Your code goes here
            
    def add_item(self, item: ItemBase):
        # TODO: Add item to the stock
        
        # INSTRUCTIONS: 
        # - If the item is not an instance of `ItemBase`, raise the InvalidItemTypeError with a nice message
        # - If the item already exist in the stock, just increment that item's `in_stock` value in the stock
        # - Else add the item to the stock
        pass
            
    def get_item(self, index: int) -> ItemBase:
        # TODO: Return an item from the stock at the specified index
        
        # INSTRUCTIONS:
        # - If the stock is empty, raise the `OutOfStockError` with a nice message
        # - Else, return the item from the stock at that index
        pass
    
    def display(self):
        print('-'*10, ' All Items ', '-'*10)
        count = 1
        for category in ItemCategoryEnum:
            print(f'# {category.name}')
            for item in self.__stock:
                if item.category.value == category.value:
                    print(f'{count}: {item.name} -> {item.in_stock}')
                    count += 1
                    
    def purchase(self, item: ItemBase, amount: Decimal) -> str:
        # TODO: Purchase an item with the amount.
        
        # INSTRUCTIONS:
        # - If the amount is lesser than the actual price of the item, raise PaymentError with the appropriate arguments
        # - Else, decrement the `in_stock` value of the item by 1 in the stock,  and send the user a nice message to inform them about a successful purchase.
        pass

if __name__ =='__main__':
    # Create our Items
    iphone_15 = Iphone('Iphone 15', ItemCategoryEnum.PHONE, 2, 5000)
    macbook_pro = Macbook('Macbook pro', ItemCategoryEnum.LAPTOP, 1, 9000)
    smart_tv_LG = TV('Smart TV LG', ItemCategoryEnum.TV, 3, 3000)

    print('='*10, ' Welcome to BuyAll ', '='*10)

    inventory_system = InventorySystem(iphone_15, smart_tv_LG,macbook_pro)
    # Add one more iphone_15
    inventory_system.add_item(iphone_15)

    while True:
        # show menu
        inventory_system.display()
        try:
            choice = int(input('Select an item to purchase: '))
            item = inventory_system.get_item(choice-1)
            amount = int(input('Enter the amount: '))
            inventory_system.purchase(item, amount)

        # TODO: Handle all exceptions that may be raised.
        

