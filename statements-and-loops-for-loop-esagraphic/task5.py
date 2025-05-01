text = input("Input your characters:")
text_lenght = int(len(text))
counter_digit=0
counter_letter =0

for i in range (text_lenght):
    if text[i].isdigit()==True:
        counter_digit +=1
    else:
        counter_letter +=1
print(f'Number of digit is {counter_digit}')
print(f'Number of letters:{counter_letter}')