def digit_filter(strings):
    def contains_digit(s):
        return any(char.isdigit() for char in s)
    
    filtered_strings = [s for s in strings if not contains_digit(s)]
    
    return filtered_strings

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
result = digit_filter(l33t)
print(result)
