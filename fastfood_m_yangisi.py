# summa = 0
# tekshirish = 0
from os import system
from time import sleep
def admin(log):
    print("Hurmatli", log ,"admin qismiga hush kelibsiz!")
    sleep(2.0)
    count = 1
    names = list()
    while True:
        system("clear")
        print("Kompaniya ma'lumotlari: ")
        print("1-Kompaniya hisobidagi mavjud pullarni ko'rish")
        print("2-Mavjud user lar ro'yhati")
        # print("3-User qismiga qaytish")
        cho = int(input(":"))
        if cho == 1:
            file = open("summa","r")
            money = file.read()
            print(f"""
Hurmatli {log} hozirda kompaniya hisobida

              {money}
                  
pul mavjud
                  """)
            sleep(3.0)
            system("clear")
        elif cho == 2:
            file = open("login","r")
            txt = file.readlines()
            for i in txt:
                count+=1
            # print(count)
            for i in txt:
                Name,password=i.split(',')
                print(Name)
                print()
                
            print("Mavjud bo'lgan userlar ro'yhati")
            h = input()
            sleep(4.0)
            system("clear")
        else:
            return False

def create(log,pasw):
        fi = open("login","a")
        fi.write(log)
        fi.write(",")
        fi.write(pasw)
        fi.write("\n")
        print("Succesfuly added✅")
        
        # return True

def check(log,pasw):
        file = open("login","r")
        txt = file.readlines()
        # print(txt)
        for i in txt:
            
            Name,password=i.split(',')
            password=password.removesuffix('\n')
            if Name == log and password == pasw:
                # print("Succes✅")
                return True
        else:
                # print("Login error")
                tekshirish = 1
    


def payment(summa):
    print("To'lov turini tanlang")
    print("""
            1-Karta orqali
            2-Naqd
          """)
    method=int(input())
    if method == 1:
        print(f""" **** **** **** **** 
              Shu kartaga {summa}yuboring va chekni kassirga ko'rsating!""") 
        print("1- To'lash✅")
        tolash=int(input())
        if tolash==1:
            sleep(1.0)
            print("To'landi✅")
            sleep(1.0)
            system("clear")
    elif method == 2:
        print("Marhamat!")
        print(f"""Sizdan {summa} sum """)
        print("1- To'lash✅")
        tolash=int(input())
        if tolash==1:
            sleep(1.0)
            print("To'landi✅")
            sleep(1.0)
            system("clear")
def menu_list(): 
    summa = 0   
    while True:
        print("1-Fastfood")
        print("2-Ichimliklar")
        print("3-Shirinliklar")
        print("4-Sho'tni ko'rish")
        print("5-Tugatish")
        b_tanlaw=int(input("Qaysi birini hohlaysiz?\n"))    
        system('clear')
        if b_tanlaw==4:
            print(summa)
        elif b_tanlaw==1:
            print("1-Burger 23000")
            print("2- Pizza 30000")
            print("3- Hot Dog 18000")
            print("4- Tacos 25000")
            tanlaw = int(input(':'))
            if tanlaw==1:
                print("Siz tanlagan mahsulot Burger\n")
                sleep(1.5)
                system("clear")
                summa +=23000
            elif tanlaw==2:
                print("Siz tanlagan mahsulot Pizza\n")
                sleep(1.5)
                system("clear")
                summa +=30000 
            elif tanlaw==3:
                print("Siz tanlagan mahsulot Hot Dog\n")
                sleep(1.5)
                system("clear")
                summa += 18000
            elif tanlaw==4:
                print("Siz tanlagan mahsulot Tacos\n")
                sleep(1.5)
                system("clear")
                summa += 25000
            else:
                print("Bunday mahsulot yo'q\n")
        elif b_tanlaw==2:
            print("1- Suv 5000")
            print("2- Coffee 8000")
            print("3- choy (qora, yashil, etc.) 5000")
            print("4- Sut 6000")
            tanlaw = int(input(':'))
            if tanlaw == 1:
                print("Siz tanlagan mahsulot Suv\n")
                sleep(1.5)
                system("clear")
                summa += 5000
            elif tanlaw == 2:
                print("Siz tanlagan mahsulot Coffee\n")
                sleep(1.5)
                system("clear")
                summa += 8000
            elif tanlaw == 3:
                print("1-Yashil\n2-Qora\n")
                choy_t=int(input())
                if choy_t==1:
                    print("Siz Qora choyni tanladingiz\n")
                elif choy_t==2:
                    print("Siz Yashil choyni tanladingiz\n")
                sleep(1.5)
                system("clear")
                summa += 5000
            elif tanlaw == 4:
                print("Siz tanlagan mahsulot Sut\n")
                sleep(1.5)
                system("clear")
                summa += 6000
            else:
                print("Bunday mahsulot yo'q\n")
                    
            # Ichimliklar listini yozin
        elif b_tanlaw==3:
            print("1- Cookies 15000")
            print("2- Cakes 20000")
            print("3- Ice cream 9000")
            print("4- Cupcakes 17000")
            tanlaw = int(input(':'))
            # Shirinlikla listini yozin
        elif b_tanlaw==5:
            fie = open("summa","r")  
            pul = fie.read()
            pul =  int(pul)
            print(pul)
            h = input()
            fie.close()
            fie = open("summa","w")  
            pul = pul + int(summa)
            fie.write(str(pul))
            payment(summa) 
            break        
        else:
            print("Bunday mahsulot yo'q")
    
    # wunaqa qb toldirb cqin fastfoodla yozb
def display_menu():
    print("Welcome to the Menu")
    print("1. Buyurtma qilish")
    print("2. Dostavka qilish")
    print("3. Ariza yozish")
    print("4. Chiqish")
# if tekshirish == 1:
    
print("Hurmatli mijoz !")
print("Bizning xizmatdan foydalanish uchun logindan o'tishingiz zarur")
sleep(3.0)
system("clear")
log = input("Enter your Name: ")
pasw = input("Enter your password: ")
print("Oldin ro'yhatdan o'tganmisz?")
print("1-HA\n 2-YO'Q")
ch = int(input(":"))
if ch == int(1221):
    #  print("Welcome to the Admin page!")
     admin(log)
if ch == 1:
    check(log,pasw)
elif ch == 2:
    print("Ro'yhatdan o'tish boshlandi!")
    sleep(2.0)
    system("clear")
    create(log,pasw)
else:
    print("Noto'g'ti buyruq")
if check(log,pasw) == True:
    while True:
        display_menu()
        choice = input()
        # menu_list(summa)

        if choice == "1":
            print("Menyu🧾")
            # Menyuni davom ettiring
            menu_list()    

        elif choice == "2":
            print("Adres kriting")
            adres = input()
            print("Adres qabul qilindi", adres)
            sleep(2.0)
            system("clear")
            menu_list()
            # Add your code for Option 2 here

        elif choice == "3":
            print("Arizani shu yerga yozib qoldiring👇🏻")
            comments = input(":")

        elif choice == "4":
            print("Yana kelib turing🤝.")
            break
        else:
            print("Noto'g'ri buyruq iltimos 1 dan 4 gacha tanlang.")
else:
    print("login error")
