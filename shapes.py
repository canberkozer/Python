a = int(input("Dikdörtgen için [1], Üçgen için [0] basınız:"))

if(a== True):
    dk1 = int(input("1. Kenar:"))
    dk2 = int(input("2. Kenar:"))
    dk3 = int(input("3. Kenar:"))
    dk4 = int(input("4. Kenar:"))
    if(dk1==dk2 and dk2==dk3 and dk3==dk4):
        print("Kare seçtiniz...")
    elif(dk1!=dk2 and dk2!=dk3 and dk3!=dk4 and dk1!=dk4 and dk1!=dk3):
        print("Yamuk dörtgen seçtiniz...")
    else:
        print("Dikdörtgen seçtiniz...")
else:
    uk1 = int(input("1. Kenar:"))
    uk2 = int(input("2. Kenar:"))
    uk3 = int(input("3. Kenar:"))    
    if ( abs(uk1+uk2) > uk3 and abs(uk2+uk3) > uk1 and abs(uk1+uk3) > uk2):
        if(uk1==uk2 and uk2==uk3):
            print("Eşkenar üçgen seçtiniz...")
        elif(uk1==uk2 or uk2==uk3 or uk1==uk3):
            print("İkizkenar üçgen seçtiniz...")
        else:
            print("Çeşitkenar üçgen seçtiniz...")
    else:
        print("Üçgen belirtmiyor.")