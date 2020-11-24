print("""**************************

Faktoriyel Bulma Programı

Programdan çıkmak için q'ya basınız.

**************************
""")


while True:
    sayı = input("Sayı giriniz:")

    if (sayı == "q"):
        print("programdan çıkılıyor...")
        break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):

            faktoriyel *= i

            print("faktöriyel =",faktoriyel)
            continue










