upper = int(input("Max:"))

armstrong=[]

for num in range(1, upper + 1):
   order = len(str(num))
   sum = 0
   temp = num

   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       armstrong.append(num)

print(armstrong)