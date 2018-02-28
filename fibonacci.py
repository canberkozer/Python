print("""*********
Fibonacci
*********""")

len = int(input("Array Lenght:"))
i=1
j=1

fibonacci =[i,j]
for x in range(len):
    i,j=j,i+j
    fibonacci.append(j)
print(fibonacci)
