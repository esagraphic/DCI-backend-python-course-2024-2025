print ( "Input few integers to calculate their average!")
print("Input 0 to exit!!!")
counter = 0
sum = 0
while True:
    number = int(input("Type a interger: "))
    sum= sum + number
    if number!=0:
     counter +=1
    if number==0:
        break
print(sum/counter)
