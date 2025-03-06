import time
from datetime import datetime

def log_yaz():
    while True:
        with open("log.txt", "a") as dosya:
            zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dosya.write("Sistem çalışıyor - " + zaman + "\n")
        print("Log kaydı yapıldı.")
        time.sleep(10)

def loglari_goruntule():
    try:
        with open("log.txt", "r") as dosya:
            loglar = dosya.readlines()
            if loglar:
                print("\nTüm Loglar:")
                for log in loglar:
                    print(log.strip())
            else:
                print("Log dosyası boş.")
    except FileNotFoundError:
        print("Log dosyası bulunamadı.")

def ana_program():
    while True:
        komut = input("Komut girin ('loglari_goruntule' yazın, çıkmak için 'q' yazın): ").lower()
        
        if komut == "loglari_goruntule":
            loglari_goruntule()
        elif komut == "q":
            print("Programdan çıkılıyor...")
            break

import threading
thread = threading.Thread(target=log_yaz)
thread.daemon = True
thread.start()

ana_program()
