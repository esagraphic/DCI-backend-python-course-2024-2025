from stack import Stack


def reverse_string(my_string: str) -> str:
    rev_stack = Stack()

    # TODO: your code goes here
    for char in my_string:
      rev_stack.push(char)
    final_rev=""
    while not rev_stack.is_empty():
        final_rev+-rev_stack.pop()
    return final_rev


if __name__ == "__main__":
    print(reverse_string("hello"))  # olleh


