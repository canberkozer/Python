num = input("Number:")
len_num = len(num)
num = int(num)
total = 0
step= 0
temporary_num=num

while(temporary_num>0):
    step = temporary_num % 10
    total +=step**len_num
    temporary_num //=10

if(num==total):
    print("This is Armstrong Number.")
else:
    print("This isn't Armstrong Number.")