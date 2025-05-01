class Stack:
    """
    This is reliable because it uses; append and pop which have O(1)
    """

    def __init__(self) -> None:
        self._data = []

    def push(self, item) -> None:
        """
        Add item to the top of the stack

        Args:
            item (obj):
                Any object that is to be added to the stack
        """
        # TODO: Replace 'pass' with your code

        self._data.insert(0,item)

    def peek(self) -> int:
        """
        Show the item at the top of the stack without removing it

        Raise:
            Exception is raised if the stack is empty
        """

        # TODO: Replace 'pass' with your code
        if not self._data:
            raise Exception("The stack is empty")  # Raise an exception
        
            
        return self._data[0]

    def is_empty(self) -> bool:
        """Return True if the stack is empty"""

        # TODO: Replace 'pass' with your code
        if not self._data:
            return True
        else:
            return False

    def size(self) -> int:
        """Return the size of the stack"""

        # TODO: Replace 'pass' with your code
        return len(self._data)

    def pop(self) -> int:
        """
        Remove and return the item at the top of the stack

        Raise:
            Exception is raised if the stack is empty

        """

        # TODO: Replace 'pass' with your code
        if not self._data:
             raise Exception("The stack is empty")  # Raise an exception
       
        return self._data.pop()


if __name__ == "__main__":
    s = Stack()
    print("Is empty? ", s.is_empty())
    print("Pushed 4")
    s.push(4)
    print("Peek top: ", s.peek())
    print("Pushed 5")
    s.push(5)
    print("Peek top: ", s.peek())
    print("Is empty? ", s.is_empty())
    print("Size is: ", s.size())
    print("Pop from top: ", s.pop())
    print("Size is: ", s.size())
    print("Peek top: ", s.peek())
    print("Pop from top: ", s.pop())
    print("Size is: ", s.size())
    print("Is empty? ", s.is_empty())
    
