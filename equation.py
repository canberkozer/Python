print("ax^2+bx+c şeklindeki denklemin a,b,c değerlerini giriniz...")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b**2 - 4*a*c
kok1 = (-b-delta**0.5)/(2*a)
kok2 = (-b+delta**0.5)/(2*a)

if(delta<0):
    print("\nDelta: {}\nReel kök yoktur.".format(delta))
elif(delta==0):
    print("\nDelta: 0\nÇift katlı kök: {:.0f}".format(kok1))
else:
    print("\nDelta: {}\nBirinci Kök: {:.0f}\nİkinci Kök: {:.0f}".format(delta,kok1,kok2))
