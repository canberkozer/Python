sayı = int(input("Number:"))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print(sayı,"Perfect Number.")
else:
    print(sayı,"not a Perfect Number.")