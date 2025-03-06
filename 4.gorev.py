def telefon_ekle():
    while True:
        komut = input("Komut girin ('ekle', 'ara', 'listele', 'çık' için): ").lower()

        if komut == "ekle":
            ad = input("Adı girin: ")
            telefon = input("Telefon numarasını girin: ")
            with open("rehber.txt", "a") as dosya:
                dosya.write(ad + ":" + telefon + "\n")
            print("Kişi eklendi.")
            
        elif komut == "ara":
            ad_ara = input("Aramak istediğiniz kişinin adını girin: ")
            telefon_ara(ad_ara)
            
        elif komut == "listele":
            listele_rehber()
            
        elif komut == "çık":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz komut, tekrar deneyin.")

def telefon_ara(ad_ara):
    try:
        with open("rehber.txt", "r") as dosya:
            bulundu = False
            for satir in dosya:
                ad, telefon = satir.strip().split(":")
                if ad.lower() == ad_ara.lower():
                    print(ad + " : " + telefon)
                    bulundu = True
                    break
            if not bulundu:
                print("Kişi bulunamadı.")
    except FileNotFoundError:
        print("Rehber dosyası bulunamadı.")

def listele_rehber():
    try:
        with open("rehber.txt", "r") as dosya:
            rehber = dosya.readlines()
            if rehber:
                print("\nRehber Listesi:")
                for satir in rehber:
                    ad, telefon = satir.strip().split(":")
                    print(ad + " : " + telefon)
            else:
                print("Rehberde hiç kişi bulunmamaktadır.")
    except FileNotFoundError:
        print("Rehber dosyası bulunamadı.")
 
telefon_ekle()
