sayi1=float(input("Lütfen birinci sayıyı giriniz:"))
sayi2=float(input("Lütfen ikinci sayıyı giriniz:"))
islem =input("lütfen bir işlem seçiniz (+,-,*,/):")
if islem== "+":
    print(sayi1+sayi2)
elif islem== "-":
    print((sayi1)-(sayi2))
elif islem== "*":
    print(sayi1*sayi2)
elif islem == "/":
    if sayi2 != 0:
        print(sayi1/sayi2)
    else:
        print("Bir sayıyı sıfıra bölemezsiniz.")