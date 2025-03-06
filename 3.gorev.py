import json
import os

def kullanici_ekle():
    while True:
        ad = input("Adınızı girin: ")
        soyad = input("Soyadınızı girin: ")
        yas = input("Yaşınızı girin: ")
        
        kullanici = {"ad": ad, "soyad": soyad, "yas": yas}
        
        if os.path.exists("kullanicilar.json"):
            with open("kullanicilar.json", "r") as dosya:
                kullanicilar = json.load(dosya)
        else:
            kullanicilar = []

        kullanicilar.append(kullanici)

        with open("kullanicilar.json", "w") as dosya:
            json.dump(kullanicilar, dosya, indent=4)

        print("Kullanıcı kaydedildi.")
        
        komut = input("Devam etmek için bir tuşa basın ya da 'listele' yazın: ")
        if komut.lower() == "listele":
            listele_kullanicilar()
            break

def listele_kullanicilar():
    if os.path.exists("kullanicilar.json"):
        with open("kullanicilar.json", "r") as dosya:
            kullanicilar = json.load(dosya)
            if kullanicilar:
                print("\nKullanıcı Listesi:")
                for kullanici in kullanicilar:
                    print("Ad: " + kullanici['ad'] + ", Soyad: " + kullanici['soyad'] + ", Yaş: " + kullanici['yas'])
            else:
                print("Henüz kullanıcı kaydedilmemiş.")
    else:
        print("Dosya bulunamadı.")

kullanici_ekle()