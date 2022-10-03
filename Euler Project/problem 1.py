########## create empty list for multiples
multiples = []

###### choose numbers that are multiples of 3 or 5 for any range 
for i in range(1000):
    if i % 3 == 0 or i % 5== 0:
        multiples.append(i)

########### print sum
print(sum(multiples))


        

