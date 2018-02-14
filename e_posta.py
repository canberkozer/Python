isim = input("İsim: ")
soyad = input("Soyad: ")
sayi = int(input("Kaçıncı kişisiniz? İlk ise 0 giriniz: "))
isim_kucuk = isim.lower()
soyad_kucuk = soyad.lower()
    
if sayi==1 or sayi ==2 or sayi ==3 or sayi ==4 or sayi ==5 or sayi ==6 or sayi ==7 or sayi ==8 or sayi ==9:
    if 'ö' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ö","o")
        soyad_kucuk=tr_en

    if 'ş' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ş","s")
        soyad_kucuk=tr_en

    if 'ü' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ü","u")
        soyad_kucuk=tr_en

    if 'ç' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ç","c")
        soyad_kucuk=tr_en

    if 'ğ' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ğ","g")
        soyad_kucuk=tr_en

    if 'ı' in soyad_kucuk:
        tr_en=soyad_kucuk.replace("ı","i")
        soyad_kucuk=tr_en


    if 'ö' in isim_kucuk:
        tr_en = isim_kucuk.replace("ö","o")
        isim_kucuk=tr_en

    if 'ş' in isim_kucuk:
        tr_en = isim_kucuk.replace("ş","s")
        isim_kucuk=tr_en

    if 'ü' in isim_kucuk:
        tr_en = isim_kucuk.replace("ü","u")
        isim_kucuk=tr_en

    if 'ç' in isim_kucuk:
        tr_en = isim_kucuk.replace("ç","c")
        isim_kucuk=tr_en

    if 'ğ' in isim_kucuk:
        tr_en = isim_kucuk.replace("ğ","g")
        isim_kucuk=tr_en   

    if 'ı' in isim_kucuk:
        tr_en=isim_kucuk.replace("ı","i")
        isim_kucuk=tr_en 

    sayi_son = str(sayi)
    print(isim_kucuk +soyad_kucuk+ sayi_son +"@posta.mu.edu.tr")
#-------------------------------------------------------------------------------------------------------------------------------------------------
else:
    if 'ö' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ö","o")
        soyad_kucuk=tr_en

    if 'ş' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ş","s")
        soyad_kucuk=tr_en

    if 'ü' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ü","u")
        soyad_kucuk=tr_en

    if 'ç' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ç","c")
        soyad_kucuk=tr_en

    if 'ğ' in soyad_kucuk:
        tr_en = soyad_kucuk.replace("ğ","g")
        soyad_kucuk=tr_en

    if 'ı' in soyad_kucuk:
        tr_en=soyad_kucuk.replace("ı","i")
        soyad_kucuk=tr_en


    if 'ö' in isim_kucuk:
        tr_en = isim_kucuk.replace("ö","o")
        isim_kucuk=tr_en

    if 'ş' in isim_kucuk:
        tr_en = isim_kucuk.replace("ş","s")
        isim_kucuk=tr_en

    if 'ü' in isim_kucuk:
        tr_en = isim_kucuk.replace("ü","u")
        isim_kucuk=tr_en

    if 'ç' in isim_kucuk:
        tr_en = isim_kucuk.replace("ç","c")
        isim_kucuk=tr_en

    if 'ğ' in isim_kucuk:
        tr_en = isim_kucuk.replace("ğ","g")
        isim_kucuk=tr_en    

    if 'ı' in isim_kucuk:
        tr_en=isim_kucuk.replace("ı","i")
        isim_kucuk=tr_en

    print(isim_kucuk +soyad_kucuk+"@posta.mu.edu.tr")