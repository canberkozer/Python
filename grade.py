vize = int(input("Vize notunuzu giriniz:"))
proje = int(input("Proje notunuzu giriniz:"))
final = int(input("Final notunuzu giriniz:"))

gno =vize*0.3 + proje*0.3 +final*0.4

if(final<40):
    print("Büte kaldınız..")
    but = int(input("Büt notunuzu giriniz:"))
    gno2 =vize*0.3 + proje*0.3 +but*0.4
    if(gno2<45):
        print("Dersten KALDINIZ...")
    else:
        if(gno2>=90):
            print("AA ile geçtiniz...")
        elif(gno2>=80):
            print("BA ile geçtiniz...")
        elif(gno2>=70):
            print("BB ile geçtiniz...")
        elif(gno2>=65):
            print("CB ile geçtiniz...")
        elif(gno2>=60):
            print("CC ile geçtiniz...")
        elif(gno2>=50):
            print("DC ile geçtiniz...")
        elif(gno2>=45):
            print("DD ile geçtiniz...")
elif(gno<45):
    print("Büte kaldınız..")
    but = int(input("Büt notunuzu giriniz:"))
    gno2 =vize*0.3 + proje*0.3 +but*0.4
    if(gno2<45):
        print("Dersten KALDINIZ...")
    else:
        if(gno2>=90):
            print("AA ile geçtiniz...")
        elif(gno2>=80):
            print("BA ile geçtiniz...")
        elif(gno2>=70):
            print("BB ile geçtiniz...")
        elif(gno2>=65):
            print("CB ile geçtiniz...")
        elif(gno2>=60):
            print("CC ile geçtiniz...")
        elif(gno2>=50):
            print("DC ile geçtiniz...")
        elif(gno2>=45):
            print("DD ile geçtiniz...")
else:
    if(gno>=90):
        print("AA ile geçtiniz...")
    elif(gno>=80):
        print("BA ile geçtiniz...")
    elif(gno>=70):
        print("BB ile geçtiniz...")
    elif(gno>=65):
        print("CB ile geçtiniz...")
    elif(gno>=60):
        print("CC ile geçtiniz...")
    elif(gno>=50):
        print("DC ile geçtiniz...")
    elif(gno>=45):
        print("DD ile geçtiniz...")