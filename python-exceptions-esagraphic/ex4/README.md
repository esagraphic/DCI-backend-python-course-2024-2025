### Mini Project - Inventory System

We have an inventory system where we sell items online.

**NB**: Code is available in the `inventory.py` file.

## InventorySystem
The inventory system defines a class `InventorySystem` that has the following

- `__stock`: Private attribute that holds a list of items
- `purchase()`: A method used to purchase items from the stock
- `add_item()`: A method used to add items to the stock
- `get_item()`: A method used to get items from the stock

## Item
An `Item` that can be added to the stock is a class with the following attributes

- `name`: str
- `category`: Enum
- `price`: Decimal
- `in_stock`: int
    
#### Errors
Here are the custom exceptions that are raised
- `OutOfStock`: When we are out of stock
- `PaymentError`: When the amount the user provides to purchase an item is not sufficient.
- `InvalidItemTypeError`: When we try to add an invalid item into the stock

## Ex1 Custom Exceptions
Let's start by defining all our custom extensions.

- Define the `OutOfStock` extension to inherit the `ValueError` exception. 
    - It's body should have just the `pass` statement
- Define the `PaymentError` exception to inherit the `ValueError` exception. 
    - The exeption should define a `__init__` method that takes in two arguments `amount`(amount the user wants to purchase the item with) and `item_price`(actual price of the item).
    - In the body of the `__init__`;
        - call the `__init__` of the parent class and pass to it the argument `f'Payment of ${amount} failed'`
        - initialize the object with `amount` and `item_price`
    - Create the method `overage` that returns the difference of the `amount` by the user and the item's actual price `item_price`
- Define the `InvalidItemTypeError` exception to inherit the `TypeError` exception
    - It's body should have just the `pass` statement.

## Ex2 Raise and handle exceptions
You have the items `Iphone`, `TV` ,`Macbook`

```python
# Category
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
```

- Complete the `InventorySystem` class in `inventory.py`
- Complete the `TODO` at the end of the `inventory.py` file.


### Run
When you run the `inventory.py` file, you should be able to see an output like this
```bash
==========  Welcome to BuyAll  ==========
----------  All Items  ----------
# PHONE
1: Iphone 15 -> 3 in stock -> $5000/item
# TV
2: Smart TV LG -> 3 in stock -> $3000/item
# LAPTOP
3: Macbook pro -> 1 in stock -> $9000/item
```

Also, you will have a request to `Select an item to purchase: `. 

**NB**: Interact with the program and make sure it works as expected.

