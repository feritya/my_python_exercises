#1-sayılar[] listesindeki tek sayıların karesini  bulan bir program yazınız.
#2-sayılar[] listesindeki çift sayıların karekökünü bulan bir program yazınız. 
#3verilen ürünlerin fiyatlarını ekrana yadıran program yazınız.
#4-urunler listesinde max fiyatı 4000 olan ürünleri ekrana yazdıran program yazınız.

#1-write a program that finds the squares of odd numbers in the sayılar [] list.
#2-write a program that finds the square root of even numbers in the sayılar [] list.
#3-write a program that prints the prices of the given products on the screen.
#4-write a program that prints products with a max price of 4000 in the urunler list.
urunler=[
    {"name":"samsung s6","price":"3000"},
    {"name":"samsung s7","price":"4000"},
    {"name":"samsung s8","price":"5000"},
    {"name":"samsung s9","price":"6000"},
    {"name":"samsung s10","price":"7000"},
]
#1
sayilar=[1,2,3,4,5,6,7,8,9,10,12,19,25,26]
for sayi in sayilar:
    if sayi%2==1:
        print(sayi**2)
print("\n\n------------------------------------------------------------------------------------")
#2
for sayi in sayilar:
    if sayi%2==0:
        print(sayi**0.5)
totoal_price=0
print("\n\n------------------------------------------------------------------------------------")
#3
for urun in urunler:
    price=0
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")
    price=int(urun['price'])
    totoal_price =totoal_price +price
print(f"toplam fiyat: {totoal_price}")

print("\n\n------------------------------------------------------------------------------------")
#4
totoal_price=0
for urun in urunler:
    if urun['price']<='4000':
        
        price=0
        print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")
        price=int(urun['price'])
        totoal_price =totoal_price +price

print(f"toplam fiyat: {totoal_price}")   