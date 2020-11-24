print("""
***********************

Kullanıcı Giriş Programı

***********************

""")

sys_kullanıcı_adı ="bilal"
sys_parola = "123"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı adı giriniz:")
    parola = input("Parola giriniz:")

    if (sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola):
        print("Kullanıcı adı hatalı...")
        giriş_hakkı -= 1

    elif (sys_kullanıcı_adı == kullanıcı_adı and sys_parola != parola):
        print("Parola hatalı...")
        giriş_hakkı -= 1

    elif (sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola):
        print("Kullanıcı adı ve Parola hatalı...")
        giriş_hakkı -= 1


    else:
        print("Başarıyla giriş yapıldı...")
        break
    if (giriş_hakkı == 0):
        print("Giriş hakkınız bitmiştir...")
        break

        










