# tr: taifiğe çıkmış bir aracın kaç kez bakımdan geçtiini ve ne zaman bakıma gitmesi gerektiğini gösteren bir uygulama yazacağım 
# en : I will write an application that shows how many times a vehicle that has gone to the traffic has been serviced and when it needs to go to maintenance.
#burada koşul ve datetime modelini kullanacağız
# we will use the condition and datetime model here  
import datetime


# Kullanıcıdan tarih bilgisini alalım
#we get the date information from the user
tarih_str = input("aracın trafiğe çıkış Tarihini girin (gg/aa/yyyy): ")
# şimdi tarih bilgisini datetime objesine çevirelim
# now let's convert the date information to the datetime object
tarih = datetime.datetime.strptime(tarih_str, "%d/%m/%Y")
# şimdi de tarih bilgisini yazdıralım
# now let's print the date information
print("aracınızın trafiğe çıkış  tarihi: ", tarih)

now = datetime.datetime.today()

gun_farki = (now - tarih).days
# gün farkını hesaplayalım
# let's calculate the day difference
if gun_farki >365:
    print("aracınız trafiğe çıkış üzerinden {} gün geçmiş".format(gun_farki))
    print("aracınızın {} kez bakıma girmesi gerekiyor.".format(1 + (gun_farki // 365)))
# 365 günü geçen araçlar için bakım hesabı
# maintenance calculation for vehicles exceeding 365 days

elif 0<gun_farki<365 :
    print("aracınız trafiğe çıkış üzerinden {} gün geçmiş ve henüz bir yılını doldurmamıs".format(gun_farki))
# 365 günü geçmeyen araçlar için bakım hesabı
# maintenance calculation for vehicles not exceeding 365 days

else:
    print("aracınız henüz trafiğe çıkış yapmadı. ")
# trafiğe çıkış yapmayan araçlar için bakım hesabı
# maintenance calculation for vehicles that do not go to traffic

