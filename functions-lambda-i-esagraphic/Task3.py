text_check = lambda text : True if text[0]=='P' or text[0]=='p' else False
print(text_check("Python"))
print(text_check("JavaScript"))
print(text_check("pirate"))


# Another method 
text_check = lambda text: text[0] in ('P', 'p')
print(text_check("Python"))      # Output: True
print(text_check("JavaScript"))  # Output: False
print(text_check("pirate"))      # Output: True
