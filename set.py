# #SET 

# number={11,8,0,1,5,2,4,6,9,6,14}
# number2={8,12,15,9,20,7,3,17,6}
# number3={19,6,24,12,5,0,15,8,11}


# result=number.intersection(number2)
# print(result)

# number|=number2 | number3
# print(number)

# #set sıralı olmadığından pop() komutu herhangi bir elemanı siler

# remove_item=number2.pop()
# print(remove_item)


 

küçük_sayı=int(input("Küçük pozitif sayıyı giriniz: "))
büyük_sayı=int(input("Büyük pozitif sayıyı giriniz: "))

i=büyük_sayı

j=2

while j<=i and i>=küçük_sayı:
    if i%j==0:
        j+=1
        print(i)
    else:
        i-=1
        








