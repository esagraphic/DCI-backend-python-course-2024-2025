import ipdb

def fizzbuzz(maximum_value):
        ipdb.set_trace()  # Debugger will stop here

        if maximum_value % 5 == 0 and maximum_value % 3 == 0:
            print('FizzBuzz')
        elif maximum_value % 5 == 0:
            print('Buzz')
        elif maximum_value % 3 == 0:
            print('Fizz')
        else:
            print(maximum_value)



fizzbuzz(25) # Buzz
fizzbuzz(30) # FizzBuzz
fizzbuzz(9)  # fizzbuzz(30)

