import time
#_____________________________________________________________________
def pertambahan ():
    num = 0
    while True:
        time.sleep(0.5)
        num1 = input("Masukan Nilai : ")
        time.sleep(0.5)
        if num1 == "=":
            print(f"{num}")
            time.sleep(0.5)
            break
        try:
            num1 = int(num1)
            num = num + num1

        except ValueError:
            print("Masukkan angka yang valid")
            break
#_____________________________________________________________________
def pengurangan ():
    time.sleep(0.5)
    num = int(input("Masukkan Nilai yang ingin dikurang : "))
    time.sleep(0.5)
    while True:
        num1 = input("Masukan Nilai : ")
        time.sleep(0.5)
        if num1 == "=":
            print(f"{num}")
            time.sleep(0.5)
            break
        try:
            num1 = int(num1)
            num = num - num1
        except ValueError:
            print("Masukkan angka yang valid")
            break
#_____________________________________________________________________
def perkalian ():
    num = 0
    time.sleep(0.5)
    while True:
        num1 = input("Masukan Nilai : ")
        time.sleep(0.5)
        if num1 == "=":
            print(f"{num}")
            time.sleep(0.5)
            break
        try:
            num1 = int(num1)
            num = num * num1
        except ValueError:
            print("Masukkan angka yang valid")
            break
#_____________________________________________________________________
def pembagian ():
    time.sleep(0.5)
    num = int(input("Masukkan Nilai yang ingin dibagi : "))
    time.sleep(0.5)
    while True:
        num1 = input("Masukan Nilai : ")
        time.sleep(0.5)
        if num1 == "=":
            print(f"{num}")
            time.sleep(0.5)
            break
        try:
            num1 = int(num1)
            num = num // num1
        except ValueError:
            print("Masukkan angka yang valid")
            break
#_____________________________________________________________________
def luaspersegipanjang():
    time.sleep(0.5)
    p = int(input("Masukan Panjang : "))
    time.sleep(0.5)
    l = int(input("Masukan Lembar : "))
    time.sleep(0.5)
    print("Panjang x Lebar")
    time.sleep(0.5)
    result = p*l
    print(f"{result}cm")
    time.sleep(0.5)
#_____________________________________________________________________
def kelilingpersegipanjang():
    time.sleep(0.5)
    p = int(input("Masukkan Panjang : "))
    time.sleep(0.5)
    l = int(input("Masukkan Lebar : "))
    time.sleep(0.5)
    print("(2 x p) = (2 x l)")
    time.sleep(0.5)
    result = (2 * p) + (2 * l)
    print(f"{result}cm")
    time.sleep(0.5)