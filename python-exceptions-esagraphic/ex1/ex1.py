lst=[5, 10, 20]

try:
    print(lst[5])

except IndexError:
    msg="You're out of list range"


print(msg)