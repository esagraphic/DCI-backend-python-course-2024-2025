text = input("Input a word to reverse :")
text_lenght = int(len(text))
for i in range (text_lenght - 1, -1, -1):
    print(text[i], end='')
