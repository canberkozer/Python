print("üye Girişi...\n")

sys_id = 'test'
sys_password = '1234'
counter =3
while True:
    input_id = input("Kullanıcı Adı:")
    input_password = input("Şifre:")

    if (sys_id != input_id and sys_password == input_password):
        print("Kullanıcı adı hatalı!\n")
        counter -=1
    elif (sys_id == input_id and sys_password != input_password):
        print("Şifre hatalı!\n")
        counter -=1
    elif(sys_id != input_id and sys_password != input_password):
        print("Kullanıcı adı ve şifre hatalı!\n")
        counter -=1
    else:
        print("Sisteme başarılı giriş yapıldı...")
        break
    if(counter==0):
        print("Giriş hakkınız bitti!")
        break
