numbers = [int(i) for i in input().split(' ')]
numscount = {} 
for i in numbers:
    if i in numscount:
        numscount[i] += 1
    else:
        numscount[i] = 1
print(numscount) #checking the dictionary for key values
l=[]
for value in numscount.values():
    if value>1:
        l=l+[value]
print(l) #printing list of keys whose values>1
print(len(l)) #prints how many repeated numbers are there.