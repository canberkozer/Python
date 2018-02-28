boy = float(input("Boyunuz:"))
kilo = int(input("Kilonuz:"))

vki= kilo/(boy**2)

print("Vucut Kitle Endeksiniz:{:.0f}".format(vki))

if(vki>=30):
    print("Obez")
elif(vki>=25):
    print("Fazla Kilolu")
elif(vki>=18.5):
    print("Normal")
else:
    print("Zayıf")