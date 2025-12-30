import random
import time
import os
import sys

def ketik(teks, delay=0.05):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def ketik_2(teks, delay=0.05):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)

def menu():
    os.system("clear")
    ketik("===Menu=Game===")
    ketik("[1] - Tebak Angka ")
    ketik("[2] - Coming Soon ")
    ketik("[3] - Coming Soon ")
    return input("Pilih Menu : ")

def intro():
    os.system("clear")
    ketik("Welcome To Kuiz Mr.Lolzzz")
    time.sleep(1)
    os.system("clear")

tampilkan_intro = True

while True:
    os.system("clear")
    pilih_menu = menu()

    if pilih_menu != "1":
        continue

    if tampilkan_intro:
        intro()
        tampilkan_intro = False

    os.system("clear")
    angka_random = random.randint(1, 1000)

    while True:
        try:
            tebakan = int(input("Masukkan Angka 1 - 1000: "))
        except ValueError:
            sys.stdout.write("\033[F\033[K")
            ketik_2("Hanya Masukkan Angka!!!")
            time.sleep(1)
            sys.stdout.write("\r\033[K")
            continue

        if tebakan == angka_random:
            os.system("clear")
            ketik(f"{tebakan} - BENAR")
            time.sleep(1)
            ketik(f"Jawabannya: {angka_random}")
            time.sleep(1)
            ketik("DAWG MUSTAHIL")
            time.sleep(1)
            os.system("clear")            

            while True:
                pilih = input("Kembali ke menu (y/n): ").lower()

                if pilih == "y":
                    break
                elif pilih == "n":
                    angka_random = random.randint(1, 1000)
                    break
                else:
                    ketik_2("Masukkan (y/n)")
                    time.sleep(1)
                    sys.stdout.write("\r\033[K")

            if pilih == "y":
                break

        elif tebakan > angka_random:
            print(f"{tebakan} - Kebesaran")
        else:
            print(f"{tebakan} - Kekecilan")
