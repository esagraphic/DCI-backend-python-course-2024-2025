# Python basics - Exceptions-I

## IIa: Theoretical Warm Up

Write short answers (2-5 sentences) to the following questions:

1. Name three things that exception processing is good for.
    1-a.Error Handling
    1-b.Fast Debugging
    1-c. Prevent program from force exit
2. What happens to an exception if you don’t do anything special to handle it?

    Answer: program will terminate and display a traceback error message

3. How can your script recover (program continuation) from an exception? 
    Put my code inside Try and except and if there is a error i will show a message and i will add as much as i can the predefined errors catching names like ValueError or ...
4. What is the ```try``` statement for?

    inside try we will write our code and if there is any error the error will catch with the help of except and it allows us to attempt executing some code and catch any errors that arise, preventing the program from crashing unexpectedly.

5. What are the two common variations of the ```try``` statement?
    1. Try - except: 
    2. Try -except - finally
6. What is the ```raise``` statement for?
    with help of raise we can explicitly trigger an exception and we can create custom exceptions or raise existing ones .

## IIb: Practical Warm Up (30 mins)

1. Place ```result="You can't divide by 0"``` in the correct place below such that the program avoids a ```ZeroDivisionError```.

```python
#Type your answer below (pick the correct line).

a=5
b=0
try:
    result=a/b
except ZeroDivisionError:
        result="You can't divide by 0"


print(result)
```

2. Place ```msg="You can't add int to string"``` in the correct place below such that the program avoids a ```BaseExceptionError```.

You can use ```except Exception```, although normally you should be careful using such powerful exception statements.

```python
#Type your answer below.

a="Hello World!"
try:
    a + 10
except TypeError:
    msg="You can't add int to string"



print(msg)

```
3. Place ```msg="You're out of list range"``` in the correct place below such that the program avoids an ```IndexError```.

```python
#Type your answer below.

lst=[5, 10, 20]

try:
    print(lst[5])

except IndexError:
    msg="You're out of list range"


print(msg)
```