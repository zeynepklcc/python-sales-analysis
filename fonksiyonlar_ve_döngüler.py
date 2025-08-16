
# FONKSIYONLAR



#toplama
def toplama(x):
    return x+25

print(f"toplamanın sonucu: {toplama(24)}")


#çarpım ve bölüm

def çarpım_ve_bölüm(x,y):
    return x*y/2

print(f"işlemin sonucu: {çarpım_ve_bölüm(2,17)}")


#üs alma

def üs_alma(a,b):
    result=a**b
    return result

print(f"kuvvetin sonucu: {üs_alma(2,9)}")


#bir fonksiyonun birden çok işlemini tek seferde yazmak

def işlemler(a,b):
    result1=a+b-2
    result2=a**b-9*a
    result3=a**2+b/3
    result4=(3-a)*(7-b)
    return result1,result2,result3,result4

print(f"işlemlerin sonuçları: {işlemler(2,5)}")


#döngü ile fonksiyon oluşturmak

def fonksiyonlar(x,y,z):
    if x>y:
        return x-y+z
    elif x==y:
        return z
    else:
        return x*2-y+2*z

print(fonksiyonlar(1,2,5))
print(fonksiyonlar(3,3,7))
print(fonksiyonlar(5,3,12))


# KOŞULLAR


# basit otomat işleyişi

eklenen_para=int(input("Lütfen gireceğiniz ücreti belirleyin: "))
istenen_ürün_fiyatı=int(input("Lütfen seçtiğiniz ürünün fiyatını girin: "))

if eklenen_para<1:
    print("paranız iade edildi. 1 tl ve üzeri yükleme yapılmalıdır.")
elif istenen_ürün_fiyatı<1:
    print("1 tl altı ürünümüz yoktur.")
elif istenen_ürün_fiyatı>eklenen_para:
    print("Girdiğiniz ücret yetersizdir. Ücretiniz iade edildi.")
elif istenen_ürün_fiyatı<eklenen_para:
    print(f"Ürün ücreti: {istenen_ürün_fiyatı} TL \nPara iadesi: {eklenen_para-istenen_ürün_fiyatı} TL ")
    print("Teşekkür ederiz")
else:
    print(f"Ürün ücreti: {istenen_ürün_fiyatı} TL \nPara iadesi: {eklenen_para-istenen_ürün_fiyatı} TL ")
    print("Teşekkür ederiz")



#range

for item in range(12):
    result=item**2+1
    print(result,end="-")


#sort
numbers=[12,25,0,38,15,28,36,19,7,12,32,21,2,11,20]

numbers.sort()
print(numbers)

#sort ve reverse
numbers=[12,25,0,38,15,28,36,19,7,12,32,21,2,11,20]

numbers.sort(reverse=True)
print(numbers)
 

#sort ve çift sayılar
numbers=[12,25,0,38,15,28,36,19,7,12,32,21,2,11,20]

for item in numbers:
    if item%2==0:
        print(item,end=" ")


#sort ve 25 ten büyük sayılar
numbers=[12,25,0,38,15,28,36,19,7,12,32,21,2,11,20]

for item in numbers:
    if item>25:
        print(item,end=" ")


#döngü ve yüzdelik alma

numbers=[12,25,0,38,15,28,36,19,7,12,32,21,2,11,20]

for item in numbers:
    if item>25:
        result=item*1.25
    elif item>10:
        result=item*1.30
    else:
        result=item*1.35
    print(f"{result:.1f}",end=" ")




