import random
hedef_sayi=random.randint(1,100)
deneme_hakkı=5
puan=100
kalan_hak=0
while (deneme_hakkı>0):
    sayi=int(input("Lütfen bir tam sayı giriniz: "))
    if (sayi<0 or sayi>100):
          print("Lütfen 1 ile 100 arasında bir tam sayı giriniz.")
    if sayi==hedef_sayi:
        print(f"Tebrikler. {6-deneme_hakkı}. denemenizde buldunuz.")
        print(f"Toplam puanınız: {puan}")
        break
    elif sayi<hedef_sayi:
        print("Daha büyük bir sayı giriniz.")
    else: 
        print("Daha küçük bir sayı giriniz.")
    puan-=15
    deneme_hakkı-=1
    if deneme_hakkı>0:
        print(f"Toplam puanınız: {puan}")
        print(f"Kalan deneme hakkı: {deneme_hakkı}")
    else: 
         print(f"Malesef oyunu kaybettiniz.")
         print(f"Toplam puanınız: {puan} ")
     



    

    












