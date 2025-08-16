 





j=2
büyük_sayı=int(input("Büyük pozitif sayıyı giriniz: "))
küçük_sayı=int(input("Küçük pozitif sayıyı giriniz: "))

while j<büyük_sayı:
    if büyük_sayı%j!=0:
       j+=1
    else:
      büyük_sayı-=1
    büyük_sayı-=1

print(büyük_sayı)















