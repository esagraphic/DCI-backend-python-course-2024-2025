index = 0 
text= "he came to me one morning One lonely Sunday morning Her long hair flowing in the mid-winter wind I know not how she found me For in darkness I was walking And destruction lay around me from a fight I could not win"
char_tofind=input('What shoud be find ')

while index < len(text):
    foundch =text[index]
    # print(text[index])
    index+=1
    if char_tofind == foundch:
        print(f'we found it at locaton {index}')
        
    if index == len(text):
        break

    # if text[index] == 'S':
    #     print(f'Charcter {char_tofind} at index{index}')
    #     index+=1
