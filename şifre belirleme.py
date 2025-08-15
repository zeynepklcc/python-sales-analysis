


import random

şifre=random.randint(1000,9999)
deneme_hakkı=3
şifre_deneme=int(input("Şifrenizi giriniz: "))

while deneme_hakkı>0:
  if şifre_deneme>9999 and şifre_deneme<1000:
    break
  elif şifre_deneme==şifre:
    print("Giriş yaptınız.")
  else:
    print("Hatalı giriş yaptınız. Tekrar deneyiniz")
    deneme_hakkı-=1
else:
  print("Deneme hakkınız bitmiştir. 30 dk sonra tekrar deneyiz.")













