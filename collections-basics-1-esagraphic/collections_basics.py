#Task 1 Create a variable called fruits and one after another add the elements Apples, Cherries and Strawberries. Loop over the list fruits and print every element to the screen.
fruits = []

fruits.append('Apples')
fruits.append('Cherries')
fruits.append('Strawberries')

for fruit in fruits:
    print(fruit)


#Task2 
cities = ['London', 'Paris', 'Berlin', 'Amsterdam']
print(f'The capital city of Germany is: {cities[2]}')
#...........................................................................

#Task3 Store the colors cyan, magenta, green, yellow, black and white in a list called colors. Remove the colors green and white. Print the remaining colors to the screen.

colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']

colors.remove('green')
colors.remove('white')
for color in colors:
    print(color)

#Task4
letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']
word = ''.join(letters)
capitalized_word = word.capitalize()
print(capitalized_word)
