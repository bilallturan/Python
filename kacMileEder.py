# -*- coding: utf-8 -*-
# bize mil soruduğu için mil için donuşum atıyoruz
donusumOrani = 0.621371192
# kullanıcıdan kaç km olduğunu yazması için input istiyoruz
km = int(input("kaç km ="))
# burada km nin kaç mil ettiğini hesaplamamız için formülümüzü yazıyoruz
mil = km * donusumOrani
# burada değeri yazdırmamız gerekiyor ve integer bir değer olduğu için dönüşümler bunları string değerlere dönüştürüyoruz
print(str(km)+" km ="+ str(mil)+ " mil eder.." )


