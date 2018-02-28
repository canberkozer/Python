print("*****Factorial*****\n")

while True:
    
    num = input("Press 'q' to Quit or Choose your number:")
    i = 1
    if(num=='q'):
        print("Your'e leaving the program...")
        break
    else:
        num = int(num)
        for num in range(num,1,-1):
            i *= num
        print("Fact:",i)
