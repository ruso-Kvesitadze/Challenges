number = 600851475143 
factors = []

while True:
    for i in range(2, int(number)+1):
        if number % i == 0:
            factors.append(i)
            number = number/i

            break
    
    if number == 1:
        break


print(max(factors))