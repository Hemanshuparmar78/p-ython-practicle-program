#while loop
l=[1,"mee",False,"this",88,"hello"]

i=0

while (i<len(l)):
    print(l[i])
    i+=1

print("     ")

#for...else...
t={2,36,85,9,5}
for i in t:
    print(i)

else:
    print("done")

#break
for i in range(100):
    if(i ==55):
        break
    print(i)

#continue
for i in range(10):
    if(i ==5):
        continue
    print(i)

print("     ")

#pass    
for i in range(10):
    pass

i=1

while(i<10):
    print(i)
    i += 1