x = int(input("X:"))
ucunkatları=[]
for i in range(1,100,1):
    if(i%x==0):
        ucunkatları.append(i)
    else:
        continue
print(ucunkatları)