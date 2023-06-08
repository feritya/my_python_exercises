#we will use file operations to realize a student system
#dosya işlemlerini kullanarak belli bir öğrenci sistemi gerçekleştireceğiz 
def notlari_oku():
    with open("notlar.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(satir)
            print( not_hesapla(satir))
    
def not_gir():
    ad =input ("öğrenci adı: ")
    soyad=input("öğrencinin soyadı : ")
    notu=input("öğrencinin notu : ")
    with(open("notlar.txt","a",encoding="utf-8")) as file:
        file.write(ad+" "+soyad+" "+notu+"\n")



def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(" ")
    isim=liste[0]
    soyisim=liste[1]
    notu=int(liste[2])
  
    son_not=(notu*0.98)
    if son_not>=90:
        harf="AA"
    elif son_not>=85:
        harf="BA"
    elif son_not>=80:
        harf="BB"
    elif son_not>=75:
        harf="CB"
    elif son_not>=70:
        harf="CC"
    elif son_not>=65:
        harf="DC"
    elif son_not>=60:
        harf="DD"
    elif son_not>=55:
        harf="FD"
    else:
        harf="FF"
    return isim+" "+soyisim+"------->"+harf+"\n"

def notlari_kaydet():
    with open("sinav.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)   

while   True:
    secim=input("1- Notları oku \n2-Not Gir\n3-Notları kaydet\n4-Çıkış\n  ")
    if secim == "1":
        notlari_oku()
    elif secim == "2":
        not_gir()
    elif secim == "3":
        notlari_kaydet()
    elif secim == "4":
        break
    else:
        print("Hatalı seçim")
        continue

