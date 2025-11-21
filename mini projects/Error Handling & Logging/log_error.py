sayi = int(input("Bir sayı giriniz: ") )
try:
    sonuc = 10 / sayi
    print("Sonuç:", sonuc)
except ZeroDivisionError as e:
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"Hata: {e}\n")
    print("Hata: Bir sayı sıfıra bölünemez. Hata kaydedildi." )
except ValueError as e:
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"Hata: {e}\n")
    print("Hata: Geçersiz giriş. Lütfen bir sayı giriniz. Hata kaydedildi." )   
except Exception as e:
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"Beklenmeyen Hata: {e}\n")
    print("Beklenmeyen bir hata oluştu. Hata kaydedildi." )
finally:
    print("Program sonlandı.")

    
