import random
import time
import os
import sys
import select
import termios
import tty

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
    ketik("[2] - Ular Nokia ")
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

    if pilih_menu == "1":
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

    elif pilih_menu == "2":
        os.system("clear")
        ketik("===Ular Nokia===")
        time.sleep(1)
        
        border_buffer = []
        
        os.system("clear")
        print("+" + "-" * 20 + "+")
        for y in range(10):
            print("|" + " " * 20 + "|")
        print("+" + "-" * 20 + "+")
        print("Gunakan W / A / S / D untuk gerak, 9 untuk keluar.")
        
        time.sleep(0.5)
        
        os.system("clear")

        lebar, tinggi = 20, 10
        ular = [(5,5)]
        arah = "KANAN"
        makanan = (random.randint(0, lebar-1), random.randint(0, tinggi-1))

        def print_papan():
            sys.stdout.write("\033[s")  
            
            sys.stdout.write("\033[1;1H")
            
            print("+" + "-" * lebar + "+", end="")
            
            for y in range(tinggi):
                sys.stdout.write("\033[{};1H".format(y + 2)) 
                print("|", end="")
                for x in range(lebar):
                    if (x, y) == ular[0]:
                        print("O", end="")
                    elif (x, y) in ular[1:]:
                        print("o", end="")
                    elif (x, y) == makanan:
                        print("X", end="")
                    else:
                        print(" ", end="")
                print("|", end="")
            
           
            sys.stdout.write("\033[{};1H".format(tinggi + 2))
            print("+" + "-" * lebar + "+", end="")
            
            
            sys.stdout.write("\033[{};1H".format(tinggi + 4))
            
            if not hasattr(print_papan, 'counter'):
                print_papan.counter = 0
            
            print_papan.counter += 1
            
            if print_papan.counter % 8 < 5:
                print("Gunakan W / A / S / D untuk gerak, 9 untuk keluar." + " " * 10, end="")
            else:
                print(" " * 60, end="")
            
            sys.stdout.write("\033[u")
            sys.stdout.flush()

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        
        try:
            tty.setraw(fd)
            
            last_move_time = time.time()
            move_delay = 0.4
            game_over = False
            
            
            print_papan()
            
            while not game_over:
                current_time = time.time()
                time_since_last_move = current_time - last_move_time
                
                if time_since_last_move < move_delay:
                    timeout = move_delay - time_since_last_move
                    if select.select([sys.stdin], [], [], timeout)[0]:
                        gerak = sys.stdin.read(1).lower()
                        if gerak == "w" and arah != "BAWAH":
                            arah = "ATAS"
                        elif gerak == "s" and arah != "ATAS":
                            arah = "BAWAH"
                        elif gerak == "a" and arah != "KANAN":
                            arah = "KIRI"
                        elif gerak == "d" and arah != "KIRI":
                            arah = "KANAN"
                        elif gerak == "9":
                            game_over = True
                    
                    current_time = time.time()
                
                if current_time - last_move_time >= move_delay:
                    kepala_x, kepala_y = ular[0]
                    if arah == "ATAS":
                        kepala_y -= 1
                    elif arah == "BAWAH":
                        kepala_y += 1
                    elif arah == "KIRI":
                        kepala_x -= 1
                    elif arah == "KANAN":
                        kepala_x += 1

                    if kepala_x < 0 or kepala_x >= lebar or kepala_y < 0 or kepala_y >= tinggi or (kepala_x, kepala_y) in ular:
                        os.system("clear")
                        ketik("Game Over!")
                        time.sleep(2)
                        game_over = True
                    else:
                        ular.insert(0, (kepala_x, kepala_y))

                        if (kepala_x, kepala_y) == makanan:
                            makanan = (random.randint(0, lebar-1), random.randint(0, tinggi-1))
                        else:
                            ular.pop()
                        
                        print_papan()
                        last_move_time = current_time
                    
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    elif pilih_menu == "3":
        os.system("clear")
        ketik("Coming Soon...")
        time.sleep(2)
                    
