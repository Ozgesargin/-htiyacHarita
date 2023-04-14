"""
İHTİYAÇ HARİTA MENÜ YAPISI
Veri saklama ve kullanma ile ilgili sorunlar yaşadım. O yüzden düzgün çalışmayabilir.
SQL araştırıp daha optimize etmeye çalışacağım.
"""
kullanici={}

# Menüyü ekrana yazdırır.
def menu():
    
    menu_item = ["Kayıt Ol", "Giriş Yap", "Hesap Silme", "Şifremi Unuttum"]
    for i in range(len(menu_item)):
        print("{}.{}".format(i+1, menu_item[i]))
        
        
#Bireysel veya kurumsal profil oluşturup kaydeder.
def kayit_ol():
    while True:
        kyt_type = ["1. Bireysel hesap", "2. Kurumsal Hesap"]
        print("\n".join(kyt_type))
        secim = input("İşlem seçiniz:\n")
        if secim == "1":
            sys_ad = input("Kullanıcı adı giriniz: ")
            sys_parola = input("Parolanızı giriniz: ")
            sys_konum = input("Konumunuzu giriniz: ")
            sys_tel_no = input("Tel no giriniz: ")
            # Yeni kullanıcıyı kullanici adına saklıyoruz
            kullanici = {
                "ad": sys_ad,
                "parola": sys_parola,
                "konum": sys_konum,
                "tel no": sys_tel_no,
                "hizmet": None,
                "tip": "bireysel"
            }
            break
        elif secim == "2":
            sys_ad = input("Kurum adı giriniz: ")
            sys_parola = input("Parolanızı giriniz: ")
            sys_konum = input("Yardım noktası konumunu giriniz: ")
            sys_tel_no = input("Tel no giriniz: ")
            sys_hizmet = input("Verilecek hizmet türlerini giriniz: ")
            # Yeni kullanıcıyı kurum adına saklıyoruz
            kurum = {
                "ad": sys_ad,
                "parola": sys_parola,
                "konum": sys_konum,
                "tel no": sys_tel_no,
                "hizmet": sys_hizmet,
                "tip": "kurumsal"
            }
            break
        else:
            print("Hatalı tuşlama yaptınız.")
            continue
            
            
# Uygulamaya giriş yapmayı sağlar.
def giris(kullanici):
    while True:
        ad = input("Kullanıcı adı giriniz: ")
        if ad not in kullanici:
            print("Kullanıcı adınızı yanlış girdiniz.")
            return False
        parola = input("Parolanızı giriniz: ")
        if kullanici[ad]["parola"] != parola:
            print("Parolanızı yanlış girdiniz.")
            return False
        else:
            print("Sisteme giriş yaptınız.")
            return True


#sisteme kayıtlı hesap bilgilerini siler.
def hesap_sil(kullanici, ad, parola):
    for i in range(len(kullanici)):
        if kullanici[i]["ad"] == ad and kullanici[i]["parola"] == parola:
            del kullanici[i]
            print("Hesabınız silinmiştir.")
            return kullanici
    print("Kullanıcı adınızı veya parolanızı yanlış girdiniz.")
    return kullanici


# Sistemdeki parolayı değiştirir.
def yeni_parola(kullanici):
    ad = input("Kullanıcı adı giriniz: ")
    for i in range(len(kullanici)):
        if kullanici[i]["ad"] == ad:
            sys_parola = input("Yeni parola giriniz: ")
            kullanici[i]["parola"]


# Ana fonksiyonum
menu() 
while True:
    secim=int(input("İşlem seçiniz"))  
    if (secim==1):
        kayit_ol()
    elif (secim==2):
        giris()
    elif (secim==3):
        ad = input("Hesabınızı silmek için kullanıcı adı giriniz:")
        parola = input("Hesabınızı silmek için parolanızı giriniz:")
        hesap_sil(kullanici, ad, parola)
    elif(secim==4):
        yeni_parola()
    else: 
        print("lütfen geçerli bir işlem seçiniz")
        continue
  


