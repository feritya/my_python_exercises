#herhangi bir fonksiyonun çalışma zamanını hesaplayacağm

#ı will calculate the running time of any function
import time

def my_decoratorfunc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} fonksiyonu  {end - start} saniyede çalıştı.")
    return wrapper

@my_decoratorfunc
def print_hello():
    print("hello")
@my_decoratorfunc
def print_world():
    print("world")

@my_decoratorfunc
def game_veriable():
    a=57
    print(type(a))
    sayi_ne =' '
    c=input('tahmin edeceğiniz değeri giriniz: ')
    c=int(c)
    b=5
    while True:
        if a==c:
            print('tebrikler')
            break
        elif a>c:   
            sayi_ne = 'küçük'
        elif a<c:
            sayi_ne = 'büyük'
        c=input(f'{b} hakkınız kaldı girdiğiniz değer tahmin edeceğiniz değerden {sayi_ne} lütfen tekrar deneyiniz: ')
        c=int(c)
        b-=1
        if b==0:
            break
    return print('oyun bitti')

print_hello()
print_world()
game_veriable()




