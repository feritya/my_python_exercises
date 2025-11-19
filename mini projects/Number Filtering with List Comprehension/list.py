sayilar =[]
cift_sayilar = []
for  i in range (5):
    i=int(input())
    sayilar.append((i))
for sayi in sayilar:
    if sayi%2==0:
        cift_sayilar.append(sayi)

maxsayi = max(sayilar)
minsayi = min(sayilar)
average = sum(sayilar)/len(sayilar)
   
print("maksimum",maxsayi, "minimum ",minsayi,"ortalama ",avarage)
print("Cift sayilar: ", cift_sayilar)