toplam = 0
while True:
    sayi = input("Sayı:")

    if(sayi=='q'):
        break
    sayi= int(sayi)

    toplam += sayi

print("Toplam:",toplam)