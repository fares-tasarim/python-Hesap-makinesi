import time
g = 0.3
d = 0.8
print(

"\n"
"█  █  █▀▀  █▀▀  █▀▀█  █▀▀█    █▀▄▀█  █▀▀█  █▄▀   ▀  █▀▄ █  █▀▀  █▀▀  ▀\n"
"█▀▀█  █▀▀  ▀▀█  █▄▄█  █▄▄█    █ ▀ █  █▄▄█  █▄▄   █  █ █ █  █▀▀  ▀▀█  █\n"
"▀  ▀  ▀▀▀  ▀▀▀  ▀  ▀  ▀       ▀   ▀  ▀  ▀  ▀  ▀  ▀  ▀  ▀▀  ▀▀▀  ▀▀▀  ▀\n"
)
print("yapımcı:")

print(
"█▀▀▀ █▀▀█  █▀▀█  █  █  █▀▀█  █▀▄ █  ▀  █ █\n"  
"█▀▀  █▄▄█  █▄▄▀  ▀▀▀█  █  █  █ █ █  █   █ \n"   
"▀    ▀  ▀  ▀ ▀▀  ▀▀▀▀  ▀▀▀▀  ▀  ▀▀  ▀  ▀ ▀\n"  

)

def topla(say1,say2):
    top = say1+say2
    print(f"toplama sonucu:{top}")

def çıkarma(say1,say2):
    top = say1-say2
    print(f"çıkarma sonucu:{top}")

def çarpma(say1,say2):
    top = float(say1)*float(say2)
    print(f"çarpma sonucu:{top}")

def bölme(say1,say2):
    top = float(say1)/float(say2)
    print(f"bölme sonucu:{top}")

def üsalma(say1,say2):
    top = float(say1)**float(say2)
    print(f"üs alma sonucu:{top}")

while True:

    say1 = input("1.sayı yı giriniz:")
    say2 = input("2.sayı yı giriniz:")
    menu1 = "toplama işlemi yapmak için 1 yazın"
    menu2 = "çıkarma işlemi yapmak için 2 yazın"
    menu3 = "çarpma işlemi yapmak için 3 yazın"
    menu4 = "bölme işlemi yapmak için 4 yazın"
    menu5 = "üs alma işlemi yapmak için 5 yazın"
    exitmenu = "çıkış yapmak için exit yazın"


    try:
        say1 = float(say1)
        say2 = float(say2)
    except ValueError:
        print("sadece sayı giriniz")
        continue

    print(menu1)
    
    time.sleep(g)

    print(menu2)

    time.sleep(g)

    print(menu3)

    time.sleep(g)

    print(menu4)

    time.sleep(g)

    print(menu5)

    time.sleep(g)

    print(exitmenu)

    time.sleep(g)

    islem = input("Yapıcağınız işlemi yazınız:")
    if islem == "1":
        topla(say1,say2)
        time.sleep(d)

    elif islem == "2":
        çıkarma(say1,say2)
        time.sleep(d)

    elif islem == "3":
        çarpma(say1,say2)
        time.sleep(d)

    elif islem == "4":
        bölme(say1,say2)
        time.sleep(d)

    elif islem == "5":
        üsalma(say1,say2)
        time.sleep(d)

    elif islem == "exit":
        break

    else:
        print("Hatalı işlem")
