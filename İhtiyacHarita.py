import sqlite3 as sql

vt = sql.connect('ihtiyacharita.db')
im = vt.cursor()

# Kullanıcı tablosu
im.execute("CREATE TABLE IF NOT EXISTS kullanicilar (ad TEXT, sifre TEXT)")
           
# İhtiyaç tablosu
im.execute("CREATE TABLE IF NOT EXISTS ihtiyaclar (konum TEXT, malzeme TEXT,adet INTEGER)")

# Yardım noktaları 
im.execute("CREATE TABLE IF NOT EXISTS yardim_noktalari (konum TEXT, iletişim_numarasi TEXT, acilis_saati TEXT, kapanis_saati TEXT, hizmet_icerigi TEXT)")


# Admin kullanıcıları
admin_kullanicilar = [{"kullanici_adi": "admin","sifre": "123456"}]
    


def menu():
    
    while(True): 

        print("\nAna Menü\n")
        print("1. Üye ol")
        print("2. Giriş yap")
        print("3. şifremi unuttum")
        print("4. Çıkış")  

        secim = input("İstediğiniz işlemi tuşayın")  
        
        if secim=="1":
            uye_ol()
        elif secim=="2":
            giris_yap()
        elif secim=="3":
            sifre_unuttum()
        elif secim=="4":
            break
        else:
            print("Hatalı tuşlama yaptınız")

        
def uye_ol(): 

    kullanici_adi = input("Kullanıcı adı:")
    sifre = input("Sifre:")
    
    im.execute("""INSERT INTO kullanicilar VALUES (?, ?)""",( kullanici_adi, sifre))
    vt.commit()
    
    print("Üye kaydı tamamlandı.")
    
def giris_yap():
    
    ad = input("Kullanıcı adı:")
    
    if ad =="admin":
        parola = input("Şifre:")
        for admin in admin_kullanicilar:
            if admin["kullanici_adi"] == ad and admin["sifre"] == parola:
                print("Admin girişi yapıldı.")
                admin_menu()
                return
    
    else:
        
        parola = input("Şifre:")
        im.execute("SELECT * FROM kullanicilar WHERE ad = ? AND sifre = ?", (ad, parola))
        kullanici = im.fetchone()
        
        if kullanici:
            print("Kullanıcı girişi yapıldı")
            kullanici_menu()
        else:
            print("Kullanıcı adı veya şifre hatalı!")


def sifre_unuttum():
    ad = input("Kullanıcı adı:")
    
    im.execute("SELECT * FROM kullanicilar WHERE ad = ?", (ad,))
    kullanici = im.fetchone()
    
    if kullanici:
        yeni_sifre = input("Yeni şifre:")
        im.execute("UPDATE kullanicilar SET sifre = ? WHERE ad = ?", (yeni_sifre, ad))
        vt.commit()
        print("Şifre sıfırlama işlemi başarılı! Yeni şifreniz: {} ".format(yeni_sifre))
    else:
        print("Kullanıcı bulunamadı!")

def admin_menu():
    
    while (True):
        
        print("\nAdmin Menüsü\n")
        print("1. İhtiyac Ekle")
        print("2. İhtiyaçları Listele")
        print("3. Yardım Noktaları Ekle")
        print("4. Yardım Noktaları Listele")
        print("0. Çıkış")     
        
        secim = input("İstediğiniz işlemi tuşayın")  
        
        if secim=="1":
            ihtiyac_ekle()
        elif secim=="2":
            ihtiyac_listele()
        elif secim=="3":
            yardım_nok_ekle()
        elif secim=="4":
            yardım_nok_listele()
        elif secim=="0":
            break
        else:
            print("Hatalı tuşlama yaptınız")        

def ihtiyac_listele():
    im.execute("SELECT * FROM ihtiyaclar")
    ihtiyaclar = im.fetchall()
    if ihtiyaclar:
        print("İhtiyaçlar:")
        for konum, malzeme, adet in ihtiyaclar:
            print(f"Konum: {konum}")
            print(f"Malzeme: {malzeme}")
            print(f"Adet: {adet}")
            print()
    else:
        print("Henüz ihtiyaç eklenmedi.")

def yardım_nok_ekle():
    konum = input("Yardım noktasının konumunu girin: ")
    iletişim_numarası = input("Yardım noktasının iletişim numarasını girin: ")
    acilis_saati = input("Yardım noktasının açılış saatini girin: ")
    kapanis_saati = input("Yardım noktasının kapanış saatini girin: ")
    hizmet_icerigi = input("Yardım noktasının hizmet içeriğini girin: ")

    im.execute("INSERT INTO yardim_noktalari VALUES (?, ?, ?, ?, ?)",
               (konum, iletişim_numarası, acilis_saati, kapanis_saati, hizmet_icerigi))
    vt.commit()
    print("Yardım noktası başarıyla eklendi.")
    
def kullanici_menu():
    
    while (True):
        
        print("\nMenü\n")
        print("1. İhtiyac Ekle")
        print("2. Yardım Noktaları Listele")
        print("0. Çıkış")     
        
        secim = input("İstediğiniz işlemi tuşayın")  
        
        if secim=="1":
            ihtiyac_ekle()
        elif secim=="2":
            yardım_nok_listele()
        elif secim=="0":
            break
        else:
            print("Hatalı tuşlama yaptınız")
        
        

def ihtiyac_ekle():
    konum = input("İhtiyacın konumunu girin: ")
    malzeme = input("İhtiyaç malzemesini girin: ")
    adet = int(input("İhtiyaç adedini girin: "))

    im.execute("INSERT INTO ihtiyaclar VALUES (?, ?, ?)",
               (konum, malzeme, adet))
    vt.commit()
    print("İhtiyaç başarıyla eklendi.")

def yardım_nok_listele():
    im.execute("SELECT * FROM yardim_noktalari")
    yardim_noktalari = im.fetchall()
    if yardim_noktalari:
        print("Yardım Noktaları:")
        for konum, iletişim_numarası, acilis_saati, kapanis_saati, hizmet_icerigi in yardim_noktalari:
            print(f"Konum: {konum}")
            print(f"İletişim Numarası: {iletişim_numarası}")
            print(f"Açılış Saati: {acilis_saati}")
            print(f"Kapanış Saati: {kapanis_saati}")
            print(f"Hizmet İçeriği: {hizmet_icerigi}")
            print()
    else:
        print("Henüz yardım noktası eklenmedi.")


menu()       

