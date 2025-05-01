import re

# Task 1 Create a variable called text to store the data: Berlin is a world city of culture, politics, media and science. . Then search for the first white space character in the string and print its location using the appropriate label.
text = "Berlin is a world city of culture, politics, media and science."

match = re.search('\s', text)

if match:
    print(f"The first white-space character is located at position: {match.start()}")
else:
    print("No white-space character found.")



#Task2
# Create a variable called text to store the data: Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital. . Then search for the word Frankfurt in the string .

text2 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
match2 = re.search('Frankfurt', text2)
if match:
    print(match2)
else:
    print("None")

# Task 3
# Create a variable called text to store the data: Berlin is a city of culture. . Replace the spaces with a hyphen.

text3 = 'Berlin is a city of culture.'
result = re.sub('\s','-', text3)
print(result)

# Task 4
# Create a variable called text to store the data: Berlin is a city of culture. . Search if the phrase in appears inside the string. Print the output of the regex function.


Text4 = 'Berlin is a city of culture.'
result4 = re.search('in' , Text4)
print(result4)

# Task 5
# Use the text variable from the previous task. Create a regular expression to look for any word that starts with an upper case "B". Print the position (start- and end-position) of the first match occurrence.
Text5 = 'Berlin is a city of culture.'
result5 = re.search(r'\bB\w*', Text5)
print(result5.start(),result5.end())


#Task6 
Text6 = 'The rain in Spain.'
result6 = re.findall(r'ai', Text6)
print(len(result6))