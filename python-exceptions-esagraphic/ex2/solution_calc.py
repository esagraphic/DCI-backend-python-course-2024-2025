class MathematicalError(Exception):
    pass

def parse_input(user_input):
    parts = user_input.split()
    
    if len(parts) != 3:
        raise MathematicalError("Input does not consist of three elements")
    
    try:
        n1 = float(parts[0])
        n2 = float(parts[2])
    except ValueError:
        raise MathematicalError("The first and third input value must be numbers")

    op = parts[1]

    if op not in ['+', '-']:
        raise MathematicalError('Invalid operator. Can only use "+" or "-"')

    return n1, op, n2

def calculate(n1, op, n2):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2

if __name__ == "__main__":
    while True:
        user_input = input(">>> ")
        if user_input == "quit":
            break
       
        # Parse the input
        try:
            n1, op, n2 = parse_input(user_input)
            result = calculate(n1, op, n2)
            print(result)
        except MathematicalError as e:
            print(f"Error: {e}")
