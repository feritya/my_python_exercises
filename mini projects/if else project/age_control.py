print("how old are you? ")
age=int(input())
if age<18:
    print("you are a child")
elif age<65:
    print ("you are an adu8ıılt")
    print(age)
elif age>65:
    print("you are a senior citizen")

else:
    print("wrong input ")             

sayi1=int (input("ilk sayiyi giriniz : "))
sayi2=int(input("ikinci sayiyi giriniz : ")) 
print("1-toplama\n2-cikarma\n3-carpma\n4-bolme")
islem=int(input("yapmak istediginiz islemi seciniz : "))

if islem ==1:
    print("sonuc= ",sayi1+sayi2)
elif islem ==2:
    print("sonuc= ",sayi1-sayi2)
elif islem ==3 :
    print("sonuc= ",sayi1*sayi2)
elif islem ==4 :
    print("sonuc= ",sayi1/sayi2)

