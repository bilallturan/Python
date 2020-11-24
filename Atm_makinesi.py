print("""***************************

Atm Makinesine Hoşgeldiniz :))

İşlemler:

1. Bakiye sorgulama

2. Para yatırma

3.Para çekme



************************************

""")

bakiye = 1000

while True:
    işlem = input("İşlem giriniz: ")

    if (işlem == "q"):
        print("programdan çıkılıyor...")

    elif (işlem == "1"):
        print("Bakiyeniz {} tldir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Bakiye giriniz:"))

        bakiye += miktar

    elif (işlem == "3"):
        miktar = int(input("Bakiye giriniz:"))



        if (bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsiniz...")
            continue





    else:
        print("geçersiz işlem")








