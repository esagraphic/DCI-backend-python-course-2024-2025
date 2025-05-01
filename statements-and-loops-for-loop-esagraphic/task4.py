text = "Hello, I love you, won't you tell me your name?"

text_lenght = int(len(text))
new_text = ""
for i in range ( text_lenght):
    if text[i] == "o":
        new_text+="O"
    else:
        new_text+=text[i]
        
print(new_text)
