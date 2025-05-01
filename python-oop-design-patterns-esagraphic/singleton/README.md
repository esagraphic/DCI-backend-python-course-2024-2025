# Singleton Pattern

### Cloud Hosting Service
You are running a cloud hosting service that provides servers to developers to run their applications.

You want to make sure only one server is available for each client's account. So, no matter how many times the client tries to instantiate a new server, no new server will be created, but the old one that was created already will be delivered to the client.

**NB**: In class, you saw several ways by which you can create a Singleton class, but for this exercise, it is recommended to use the Metaclass solution.

#### Exercise 1: Create the Singleton metaclass
Modify the code in the `src/singleton.py` file.

#### Exercise 2: Create the Server class
**NB**: Modify the `Server` class in `src/server.py`.
##### Step 1:
We want the server class to use `MetaSingleton` you completed in exercise 1 so that it is now a singleton class.

Modify the `Server` class to use the `MetaSingleton` class.

Then run the test 

```python
# Open a terminal where the 'src' folder is found and run
python test.py
```
And make sure everything runs without errors.

##### Step 2:

Complete the `Server` class by providing implementation to it's various methods so that when you run with `python -m src.server`, you have results as bellow;

```bash
python -m src.server
# output
['memory 1']
['memory 1', 'memory 2']
['memory 1', 'memory 2', 'memory 3']
['memory 1', 'memory 2', 'memory 3', 'memory 4']
['memory 1', 'memory 2', 'memory 3']
['memory 1', 'memory 2', 'memory 3']
```


