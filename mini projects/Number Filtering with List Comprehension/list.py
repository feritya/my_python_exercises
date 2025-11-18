sayilar =[]
cift_sayilar = []
for  i in range (5):
    i=int(input())
    sayilar.append(int(i))
for sayi in sayilar:
    maxsayi = max(sayilar)
    minsayi = min(sayilar)
    avarage = sum(sayilar)/len(sayilar)
    if sayi%2==0:
        cift_sayilar.append(sayi)
   
print("maksimum",maxsayi, "minimum ",minsayi,"ortalama ",avarage)
print("Cift sayilar: ", cift_sayilar)