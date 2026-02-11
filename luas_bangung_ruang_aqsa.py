import time, math
print("____Welcome to program calculator bangun ruang____")
time.sleep(0.5)
def wait():
    time.sleep(0.5)
def waitt():
    time.sleep(2)
def balok(p, l, t):
    return p * l * t
def kubus(s):
    return s ** 3
def tabung(r, t):
    return math.pi * r**2 * t
while True:
    mode = input("Mau menghitung volume bangun ruang apa?, yang tersedia : \n   1. Balok\n   2. Kubus\n   3. Tabung\n   4. Stop\nMode : ")
    wait()
    if mode == "Balok":
        print("Rumusnya yaitu PxLxT")
        try:
            p = float(input("Masukkan Nilai P : "))
            l = float(input("Masukkan Nilai l : "))
            t = float(input("Masukkan Nilai t : "))
        except ValueError:
            print("Input valid number")
            waitt()
            continue
        result = balok(p, l, t)
        print(f"Hasil perkaliannya adalah {result}cm")
        waitt()
    if mode == "Kubus":
        print("Rumusnya yaitu SxSxS")
        try:
            s = float(input("Masukkan Nilai s : "))
        except ValueError:
            print("Input valid number")
            waitt()
            continue
        result = kubus(s)
        print(f"Hasil perkaliannya adalah {result}cm")
        waitt()
    if mode == "Tabung":
        print("Rumusnya yaitu phi r^2 t")
        try:
            r = float(input("Masukkan Nilai jari-jari : "))
            t = float(input("Masukkan Nilai tingginya : "))
        except ValueError:
            print("Input valid number")
            waitt()
            continue
        result = tabung(r, t)
        print(f"Hasil perkaliannya adalah {result}cm")
        waitt()
    if mode == "Stop":
        break
    else:
        print("Masukan yang valid")
