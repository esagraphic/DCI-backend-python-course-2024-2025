text = "Overhead the albatross Hangs motionless upon the air And deep beneath the rolling waves In labyrinths of coral caves"
result = ""
index = 0
while index < len(text):
    letter = text[index]
    
    if letter.islower():
        result += letter.upper()
    else:         
        result += letter.lower()
    
    index += 1

print(result)
