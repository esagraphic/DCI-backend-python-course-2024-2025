# Python basics - Exceptions II

## Coding a calculator

### Context

In this exercise, your are given code for a program that is a basic calculator. User input is assumed to be a mathematical formula that consist of a number, an operator (at least + and -), and another number, **separated by white space** (e.g. 1 + 1). Here is the basic code for the calculator:

**NB**: Check code in `solution_calc.py`

An interaction could look like this if you run the `solution_calc.py` file.

```python
>>> 1 + 1
2.0
>>> 3.2 - 1.5
1.7000000000000002
>>> quit
```

### Task

Your task is to complete the function called `parse_input`,that splits user input using `str.split()`, and checks (using exceptions) whether the following list of things are valid (using try and except):

1. If the input does not consist of 3 elements, raise a `MathematicalError`, which is a **custom Exception**. **_(Hint: create a custom exception class)_**
2. Try to convert the first and third input to a float type(like so: float_value = float(str_value)). Catch any `ValueError`(built-in exception) that occurs, and instead raise a `MathematicalError` (custom exception).
3. If the second input is not '+' or '-' (or any other operator that you use), again raise a `MathematicalError`.

If the input is valid, perform the calculation and print out the result (as in the code above). The user is then prompted to provide new input, and so on, until the user types "quit".

### ```unittest```

In order to test your solution:

- *Run* the **test_calc.py** script and make sure all tests pass.
