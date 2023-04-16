"""
bu programda temel liste komutlar ile ilgili alıştırmalar yapacağım
aynı zamanda selenium yazılımce bootcampi 2. ders 1. ödevi de yapmış olacağım


"""
liste = []
a = True
b = True
silme = True

while a == True:  
    choise =input("Lütfen yapmak istediğiniz işlemi seçiniz: \n 1-Öğrenci Ekleme \n 2-Öğrenci Silme \n 3-Öğrenci Listeleme \n 4-Öğrenci Numarası Bulma \n 5-Çıkış \n")

    if choise == "1":
        while b == True:
                ogrenci = input("öğrenci adı soyadı giriniz: ")
                if ogrenci != "q":
                   liste.append(ogrenci)
                   print("çıkmak için q'ya basın")
                else:
                    b = False
        
    elif choise == "2":
        print("Öğrenci Silme")
        while silme == True:
            ogrenci = input("silmek itediğiniz öğrencinin adı soyadı giriniz: ")
            liste.remove(ogrenci)
            silme = False
    elif choise == "3":
        print("Öğrenci Listeleme")
        print(liste)
    elif choise == "4":
        print("Öğrenci index  Numarası Bulma")
        ogrenci = input("öğrenci adı soyadı giriniz: ")
        print(liste.index(ogrenci))

    elif choise == "5":
        a=False
        print("Çıkış yapıldı")
    else:
        print("Yanlış Seçim Yaptınız")


