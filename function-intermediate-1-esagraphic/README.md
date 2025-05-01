# Python-function-intermediate-1

**Task: 1**  
Define a function `describe_person(name, age, job="Unknown")` that takes three arguments, where `job` has a default value. Call this function using a mix of positional and keyword arguments.

Your result could look like:

```
describe_person("Sara", 30)
Output:
Name: Sara, Age: 30, Job: Unknown

describe_person("Timm", 25, "Engineer")
Output:
Name: Timm, Age: 25, Job: Engineer

describe_person(name="Charlie", age=22, job="Artist")
Output:
Name: Charlie, Age: 22, Job: Artist
```


**Task: 2**  
Write a function `sum_numbers(*args)` that accepts any number of positional arguments, all of which are expected to be numbers, and returns their sum. Test this function with varying numbers of arguments.

Your result could look like:

```
sum_numbers(1, 2, 3)  # Output: 6
sum_numbers(10, 20, 30, 40)  # Output: 100
sum_numbers()  # Output: 0
```

**Task: 3**  
Create a function `person_details(name, **kwargs)` that takes a mandatory `name` argument and any number of keyword arguments. The function should print the name and the additional details passed through `kwargs`.

Your result could look like:

```
person_details("Martin", age=30, job="Engineer")

Output:
Name: Martin
age: 30
job: Engineer

```


**Task: 4**  
Write a function `combine(*args, **kwargs)` that accepts both positional and keyword arguments. The function should print all positional arguments as a list and all keyword arguments as a dictionary.


Your result could look like:

```
combine(1, 2, 3, a=10, b=20, c=30)

Output:
Positional arguments (args): (1, 2, 3)
Keyword arguments (kwargs): {'a': 10, 'b': 20, 'c': 30}

```


**Task: 5**  
Create a function `calculate_area(length, width)` that calculates the area of a rectangle. Use argument unpacking to pass the values from a list and from a dictionary to this function.


Your result could look like:

```
dimensions_list = [5, 10]
Output: Area from list: 50

dimensions_dict = {'length': 5, 'width': 10}
Output: Area from dictionary: 50

```

**Task: 6**  
Define a function `order_food(main_course, *, drink="Water", dessert="Ice cream")` that takes one positional argument `main_course` and two keyword-only arguments `drink` and `dessert`. Call this function in different ways to see how keyword-only arguments work.

Your result could look like:

```
order_food("Pizza")
Output: Main Course: Pizza, Drink: Water, Dessert: Ice cream

order_food("Burger", drink="Cola", dessert="Cake")
Output: Main Course: Burger, Drink: Cola, Dessert: Cake

order_food("Pasta", dessert="Pudding")
Output: Main Course: Pasta, Drink: Water, Dessert: Pudding
```


**Task: 7**  
Create a function `update_settings(**kwargs)` where `kwargs` can have the keys `"theme"`, `"notifications"`, and `"language"`. Each of these keys should have a default value, and the function should return the updated settings as a dictionary.


Your result could look like:

```
update_settings(theme="dark")
Output: 
{'theme': 'dark', 'notifications': True, 'language': 'English'}


update_settings(notifications=False, language="Spanish")
Output:
{'theme': 'light', 'notifications': False, 'language': 'Spanish'}
```


**Task: 8**  
Write a function `profile(name, age, *skills, location="Unknown", **additional_info)` that demonstrates the use of positional arguments, default keyword arguments, `*args`, and `**kwargs` together. The function should print out a profile summary for a person, including their name, age, skills, location, and any additional information provided.

Your result could look like:

```
profile("Maxim", 35, "C++", "SQL")

Output:
Name: Maxim
Age: 35
Skills: C++, SQL
Location: Unknown


profile("Simona", 28, "Python", "Java", location="New York", hobby="Painting", job="Developer")

Output:
Name: Simona
Age: 28
Skills: Python, Java
Location: New York
hobby: Painting
job: Developer
```
