def IsDivisebleTo20(number):
    for i in range(1, 11):
        if number % i != 0:
            return False
    return True

number = 1
while True:
    if IsDivisebleTo20(number):
        break
    number +=1

print(number)

