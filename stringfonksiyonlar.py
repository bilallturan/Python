# Substring  stringlerde istediğimiz harf aralığına ulaşmak için "[2:8]" gibi değer kullanırız.

metin = "merhaba dünya"

print(metin[2:8])
# burada 2. indexten başlayıp 8. indexe kadar olan bölümü ekrana yazdırır. (rhaba) gibi...

# len  yazılan değerin uzunluğunu verir.

isim = "bilal turan"

print(len(isim))
# metinin uzunluğu "11" olarak bize verir
# hangi değerin uzunluğunu almak istiyorsak print yazdıktan sonra len() komutunun içerisine o değerin adını yazarız.


#Lower upper

değer = "merhaba dünya"

print(değer.upper())
# upper metodu bize yazılan metinin bütün harflerini büyük harf olarak yazdırır.

print(değer.lower())
# lower metodu ise bize metinin bütün harflerini küçük harf olarak yazdırır.

# Split

# kelime kelime stringlerine ayırma,

bilgi = "Bilal Turan 21 Antalya"

print(bilgi.split())

# ['Bilal', 'Turan', '21', 'Antalya'] böyle bir parçalama işlemi gerçekleştirir.





