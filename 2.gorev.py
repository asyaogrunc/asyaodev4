import os

def not_ekle():
    while True:
        notu = input("Notunuzu girin (görüntülemek için 'goruntule' yazın, silmek için 'sil' yazın, çıkmak için 'q' yazın): ")
        
        if notu.lower() == "goruntule":
            notlari_goruntule()
        elif notu.lower() == "sil":
            dosya_sil()
        elif notu.lower() == "q":
            print("Programdan çıkılıyor...")
            break
        else:
            with open("gunluk.txt", "a") as dosya:
                dosya.write(notu + "\n")
            print("Notunuz kaydedildi.")

def notlari_goruntule():
    if os.path.exists("gunluk.txt"):
        with open("gunluk.txt", "r") as dosya:
            notlar = dosya.readlines()
            if notlar:
                print("\nDosyadaki Tüm Notlar:")
                for not_ in notlar:
                    print(not_.strip())
            else:
                print("Henüz herhangi bir not kaydedilmemiş.")
    else:
        print("Dosya bulunamadı.")

def dosya_sil():
    try:
        os.remove("gunluk.txt")
        print("Dosya silindi.")
    except FileNotFoundError:
        print("Dosya zaten bulunamadı.")

not_ekle()