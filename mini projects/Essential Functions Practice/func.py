import math


def average():
    numbers=[10,12,14,13,12,15,16,]
    avg = sum(numbers)/len(numbers)
    return avg

def reverse_string(s):
    boyut = len(s)-1
    print ([s[-x-1] for x in range(len(s))]) 

def asal_mi(n):
    if n <=1:
        return False
    for i in range(n):

        if i>1:
            if n % i == 0:
                return False
    return True


print ("lutfen bir seçiim yapınız \n1- average hesabı \n2-metni tersten yazdırma \n3-asal sayı kontrolü")
choise = int(input("seçiminiz: "))
if choise == 1:
    print("average:",average())
elif choise == 2:
    s = input("metni giriniz: ")
    reverse_string(s)
elif choise == 3:
    n = int(input("sayıyı giriniz: "))
    if asal_mi(n):
        print(f"{n} asal sayıdır.")
    else:
        print(f"{n} asal sayı değildir.")
