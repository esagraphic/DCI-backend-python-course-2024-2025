x = 0
big_number = False
while x < 2:
    x += 1 
    first_number = input('Enter your First Number')
    sec_number = input('Enter your sec Number')

    if first_number != sec_number:
        print('Numbers are not equal')
    if sec_number > first_number:
        print("Second Number is greater than first number")
    if sec_number >= first_number:
        print("Second Number is greater than or equal to first number ")
    if int(first_number) and int(sec_number) > 1000:
        print('Both Number are big!')
        big_number = True
        print('big_numbers is set to:', big_number)

    if int(first_number) and int(sec_number) < 1000:
        print('Both Number are not big !')
        big_number = False
        print('big_numbers is set to:', big_number)



    

    

