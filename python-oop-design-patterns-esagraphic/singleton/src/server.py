from singleton  import MetaSingleton

class Server(metaclass=MetaSingleton):
    def __init__(self):
        self.__memory = []  # list that should hold memories
        self.__memory_count = 0  # to track the number of memories added

    def add_memory(self):
        """Append 'memory #' to the list.

        Ensure # increments each time a memory is added.

        Example:
        server.add_memory() -> ['memory 1']
        server.add_memory() -> ['memory 1', 'memory 2']
        """
        self.__memory_count += 1  # Increment memory count
        self.__memory.append(f'memory {self.__memory_count}')  # Add new memory

    def remove_memory(self):
        """Remove the last memory in the list.

        First check if the list is empty.
        If empty, print a message like 'No memory available to be removed'.
        """
        if not self.__memory:  # Check if the memory list is empty
            print('No memory available to be removed')
        else:
            self.__memory.pop()  # Remove the last memory

    @property
    def memory(self):
        """Return the current list of memories."""
        return self.__memory

if __name__ == "__main__":
    server_1 = Server()
    server_1.add_memory()
    print(server_1.memory)  # ['memory 1']
    server_1.add_memory()
    print(server_1.memory)  # ['memory 1', 'memory 2']
    server_1.add_memory()
    print(server_1.memory)  # ['memory 1', 'memory 2', 'memory 3']

    server_2 = Server()
    server_2.add_memory()
    print(server_2.memory)  # ['memory 1', 'memory 2', 'memory 3', 'memory 4']
    server_1.remove_memory()
    print(server_1.memory)  # ['memory 1', 'memory 2', 'memory 3']
    print(server_2.memory)  # ['memory 1', 'memory 2', 'memory 3']
