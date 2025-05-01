# Task 1
text = 'Berlin is a world city of culture, politics, media and science.'
text_len= len(text)
print(text_len)


# Task 2 
print(text[0],text[-1])


# Task 3 print first 3 char


print('First Three Characters:',text[0:3].upper())


#..................................................

# Task4 

def count_string(txt , sub_txt):
    count_num = txt.count(sub_txt)

    return count_num

New_Text = 'Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg s capital'


sub_text = 'B'

x = count_string(New_Text,sub_text)

print(f'{sub_text}  appears: {x} times ')

# -----------------------------------------------------

# Task5 Print last 10 Char of text 

Text_last10 = 'Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau.'
print(f'Last ten characters:{Text_last10[-10:]}')

#..........................................................................

# Task 6

text6 = '---Python programming---'
print(text6.replace('-',''))

#..........................................................................


# Task 7 

first_name = "Mary"
last_name = "Mat"

print("Firstname:", first_name, "\nLastname:", last_name)

