#basit bir banka hesaplama algoritması
def create_account(owner_name):
    return {"owner":owner_name,"balance":0}

def deposit(account,amount):
    if (amount>0):
        account["balance"]+=amount
        print(f"{amount} TL başarılı bir şekilde yatırıldı.Güncel bakiye: {account["balance"]} TL")
    else:
        print("Yatırılacak miktar pozitif olmalı")

def  withdraw(account,amount):
    if (amount>0):
        if account["balance"]>=amount:
            account["balance"]-=amount
            print(f"{amount} TL başarılı bir şekilde çekildi.Güncel bakiye: {account["balance"]} TL")
        else:
            print("Yetersiz Bakiye")
            print(f"Güncel bakiye: {account["balance"]} TL")

    else:
        print("Çekilecek miktar pozitif olmalı")

def display_balance(account):
    print(f"{account["owner"]} hesabının güncel bakiyesi: {account["balance"]} TL")

print("Bankamızın hesap uygulamasına hoş geldiniz!")
owner=input("Hesap sahibinin adı: ")
account=create_account(owner)
while(True):
    print("\nSeçenekler:")
    print("1. Para Yatır")
    print("2. Para Çek")
    print("3. Bakiye Görüntüle")
    print("4. Çıkış Yap")
    choice=int(input("Seçiminizi yapın(1-4):"))
    if (choice==1):
        amount=float(input("Yatırmak istediğiniz miktarı giriniz: "))
        deposit(account,amount)
    elif (choice==2):
        amount=float(input("Çekmek istediğiniz miktarı giriniz: "))
        withdraw(account,amount)
    elif (choice==3):
        display_balance(account)
    elif(choice==4):
        print("Uygulamadan çıktınız. İyi günler dileriz!")
        break
    else:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir seçenek giriniz.")


















