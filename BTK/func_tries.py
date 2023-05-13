#gönderilen bir parametreyi belirtilen kez ekrana yazan bir fonksiyon 
#en: a function that prints the sent parameter to the screen a specified number of times

def yazdir(metin, adet):
    for i in range(adet):
        print(metin)

# yazdir("Merhaba", 5)


# kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon
# en: a function that converts an unlimited number of parameters sent to itself into a list
def parameter_list(*args):
    liste = []
    for i in args:
        liste.append(i)
    return print (liste)
# parameter_list(1,2,3,4,5,6,7,8,9,10)


# kendisine gönderilen bir sayının asal sayı olup olmadığını belirten fonksiyon
# en: a function that determines whether a number sent to it is a prime number
def asal_bul(sayi):
    if sayi==1:
        return print("Sayı asal değildir.")
    elif sayi==2:
        return print("Sayı asaldır.")
    elif sayi>2:
        for i in range(2,sayi):
            if sayi%i==0:
                return print("Sayı asal değildir.")
        
    else:
        return print("sayi asaldır .")
asal_bul(1)
asal_bul(2)
asal_bul(323)


