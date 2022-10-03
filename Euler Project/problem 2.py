######### create empty list for fibonaci number
fibonaci = [1,1]
answer = 0

######### add in fibonaci list numbers, last number should be less than 4 000 000
while (fibonaci[-1] + fibonaci[-2])<4e6:
    fibonaci.append(fibonaci[-1] + fibonaci[-2])

######## from fibonaci took numbers which are even and sum all these even numbers
for i in fibonaci:
    if i%2 == 1:
        answer += i

        





print(answer)





