# Python Basic OOP

## Exercise 1
Let's create a class called `Point`. It should have the attributes `x` and `y` that represent the horizontal and vertical axis of the point.

The class should have a method `move(x,y)` that moves the Pointer to the respective axies. The `reset()` should reset the Point to `0,0`.

We should also have a method called `calc_distance(other)` that takes in another Point object and calculate the distance between them using this formula

$$ \sqrt{(x_1 - x_0)^2 + (y_1 - y_0)^2}$$

Provide your solution in the `point.py` file

## Exercise 2
Let's build
- Stack
- Queue

### Stack

Remember, our stack follows the `Last in First out` LIFO.

A stack should implement the following interfaces 
- is_empty -> returns a boolean indicating if our stack is empty or not
- size     -> returns how many items we have in the stack
- peek     -> tell us what the top element is in our stack
- pop      -> remove and return the top element in our stack
- push     -> add element in our stack

**NB**: Let's use a list as the underlying storage.

Complete the code from the `stack.py` file

### Queue

Remember, our queue follows the `First in First out` FIFO

It shall have the following interfaces:
- `enqueue(e)`: Add an item 'e' to the end of the queue, Q.
- `dequeue()`: Remove and return the element at the front of the queue, Q. Raise an exception if empty
- `peek()`: Return a reference to the element at the front of the queue, Q.
- `is_empty()`: Return True if queue is empty or False otherwise.
- `size()`: Return the size of the queue

**NB**: Let's use a [deque](https://docs.python.org/3/library/collections.html#collections.deque) as the underlying storage.

Complete the code from the `queue.py` file

## Exercise 3
Stacks can be used for solving many problems, like reversing a string, balancing equations and so on.

Complete the code from the `reverse_str.py` file