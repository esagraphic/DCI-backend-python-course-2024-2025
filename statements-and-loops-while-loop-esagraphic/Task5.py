start_num = int(input('starting integer '))
end_num = int(input('sending integer'))
divisor = int(input('divisor '))
index = start_num


while index < end_num and divisor >0:
    
    #print(f'{index}')
    index+=1
    
    if index % divisor == 0 :
        print(f'{index} is divisible by {divisor}')
    if divisor == 0:
        print('Thanks for using our system')
        break
