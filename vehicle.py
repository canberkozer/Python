km_ucret = float(input("km başı aracın yaktığı ücret:"))
km = int(input("kaç km gittiniz:"))

odeme = km_ucret * km

print("Ödemeniz gereken ücret: {:.0f}".format(odeme))