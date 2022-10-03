######## Create empty list for subtitution that are polindromics
subtitusion = []

##########  check if number is polidromic and if it is drop in empty list
for i in range(100,1000):
    for k in range(100,1000):
        a = str(i*k)
        if a == a[::-1]:
            subtitusion.append(int(a))
            
######### prin max from these polycromics
print(max(subtitusion))