# Strategy Pattern

> `Strategy` is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

At times, the term `family of algorithms` in strategy pattern means `different implementation of the same algorithm`. This is why in Python,
The `sorted` function and `sort` methods are themselves a great example of Strategy pattern. They have the named parameter `key` that accepts a function that implements the sorting strategies. For example
- You want to sort by keys or values of a dictionary
- You want to sort in descending or ascending order
- You want to sort by a computed value.

## Task 1
Complete the TODOs in the `src/sort_strategy.py` file, 

## Task 2
Run the `src/main.py` file and make sure you have the following output

```bash
{'a': 4, 'e': 2, 'f': 1}
{'f': 1, 'e': 2, 'a': 4}
[6, 5, 4, 3, 2, 1]
[(2, 1), (1, 2), (5, 3)]
```




