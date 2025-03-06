def ogrenci_ekle():
    with open("ogrenciler.txt", "a") as dosya:
        while True:
            ogrenci_adi = input("Öğrenci adını girin (bitirmek için 'bitti' yazın): ")
            if ogrenci_adi.lower() == "bitti":
                print("Giriş işlemi sonlandırıldı.")
                break
            dosya.write(ogrenci_adi + "\n")

def ogrencileri_yazdir():
    try:
        with open("ogrenciler.txt", "r") as dosya:
            ogrenciler = dosya.readlines()
            if ogrenciler:
                print("Öğrenci Listesi:")
                for ogrenci in ogrenciler:
                    print(ogrenci.strip())
            else:
                print("Henüz öğrenci eklenmemiş.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")

ogrenci_ekle()

ogrencileri_yazdir()