# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

#--------------------CEVAPLAR--------------------

type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)


#Görev 2: Verilen string ifadenin tüm harflerini büyükharfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight"

#--------------------CEVAPLAR--------------------

new_text = text.upper().replace(",", " ").replace(".", " ").split()
print(new_text)



#Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

#Adım1: Verilen listenin eleman sayısına bakınız.
#Adım2: Sıfırıncı v onuncu indeksteki elemanları çağırınız
#Adım3: Verilen liste üzerinden["D", "A", "T", "A"] listesi oluşturunuz.
#Adım4: Sekizinci indeksteki elemanı siliniz.
#Adım5: Yeni bir eleman ekleyiniz.
#Adım6: Sekizinci indekse"N" elemanını tekrar ekleyiniz.

#--------------------CEVAPLAR--------------------

#1
len(lst)

#2
istenen_index = [0, 9]
istenen_lst = [lst[i] for i in istenen_index]
print(istenen_lst)

#3
lst[0:4]

#4
lst.pop(7)

#5
lst.append("UGUR")
print(lst)

#6
lst[7] = "E"
print(lst)



#Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]

#--------------------CEVAPLAR--------------------

tek_lst = []
cift_lst = []

def kontrol(liste):
     for i in liste:
          if i % 2 == 0:
               cift_lst.append(i)
          else:
               tek_lst.append(i)

     return (tek_lst,cift_lst)

kontrol(l)


#Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye girenöğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

#--------------------CEVAPLAR--------------------

mühendislik = "Mühendislik Fakültesi"
tip = "Tıp Fakültesi"

for i, ogrenci in enumerate(ogrenciler, start=1):
    if i <= 3:
        grup = mühendislik
    else:
        grup = tip
    print(f"{grup} {i if i <= 3 else i - 3}. öğrenci: {ogrenci}")



#Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

#--------------------CEVAPLAR--------------------

for ders, kr, kon in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kr} olan {ders} kodlu dersin kontenjanı {kon} kişidir.")



#Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2):
     print(kume1.intersection(kume2))
else:
     print(kume2.difference(kume1))






























