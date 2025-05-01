
from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def is_empty(self):
        # TODO: Replace 'pass' with your code
        if not self._data:
            return True
        else:
            return False

    @property
    def size(self):
        # TODO: Replace 'pass' with your code
        return len(self._data)

    def enqueue(self, item):
        # TODO: Replace 'pass' with your code
        #  self._data.append(item) # deque([0, 1, 2, 3, 4])
        self._data.appendleft(item) # deque([4, 3, 2, 1, 0])

    def peek(self):
        """Return the item at the front of the queue without removing it. Raise an exception if empty."""
        if not self._data:
            raise Exception("The queue is empty")
        return self._data[0]
    
    def dequeue(self):
        # TODO: Replace 'pass' with your code
     if not self._data:
         raise Exception("The queue is empty")  # Raise an exception
       
     return self._data.popleft()

    def __str__(self) -> str:
        return str(self._data)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    print("Size of Queue: ", q.size)
    print("Peek the Queue: ", q.peek())
    print("Pop from Queue: ", q.dequeue())
    print("Peek the Queue: ", q.peek())
    print("Size of Queue: ", q.size)
    print("Pop from Queue: ", q.dequeue())
    print("Size of Queue: ", q.size)
    try:
        print("Peek the Queue: ", q.peek())  
    except Exception as e:
        print(e)  # Output: The queue is empty

