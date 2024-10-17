# 1. Buatkan Program Dalam Bentuk Menu
# 2. Menampilkan Bilangan Prima
# 3. Menampilkan Bilangan Ganjil
# 4. Menampilkan Bilangan Genap
# 5. Keluar Sistem

import os

def cek_prima():
    try:
        def prima(x):
            for i in range(2, x):
                if x % i == 0:
                    return False

            return True
    
        print(f"\n{'='*10} Cek Bilangan Prima {'='*10}")
        awal = int(input("Masukan Bilangan Awal : "))
        akhir = int(input("Masukan Bilangan Akhir : "))
        print(f"\nBilangan Prima Dari {awal} Sampai {akhir}")
        for x in range(awal, akhir + 1):
            if prima(x):
                print(x, end=', ')
    except ValueError as e:
        print(f"\n{'='*10} EROR !!! {'='*10}")
        print(f"Error : {e}")


def cek_ganjil():
    try:
        print(f"\n{'='*10} Cek Bilangan Ganjil {'='*10}")
        awal = int(input("Masukan Bilangan Awal : "))
        akhir = int(input("Masukan Bilangan Akhir : "))

        print(f"\nBilangan Ganjil Dari {awal} Sampai {akhir}")
        for i in range(awal, akhir + 1):
            if i % 2 == 1:
                print(i, end=' ')
    except ValueError as e:
        print(f"\n{'='*10} EROR !!! {'='*10}")
        print(f"Error : {e}")


def cek_genap():
    try:
        print(f"\n{'='*10} Cek Bilangan Genap {'='*10}")
        awal = int(input("Masukan Bilangan Awal : "))
        akhir = int(input("Masukan Bilangan Akhir : "))

        print(f"\nBilangan Genap Dari {awal} Sampai {akhir}")
        for i in range(awal, akhir + 1):
            if i % 2 == 0:
                print(i, end=' ')
    except ValueError as e:
        print(f"\n{'='*10} EROR !!! {'='*10}")
        print(f"Error : {e}")


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{'='*10} Cek Bilangan {'='*10}")
    print("1. Bilangan Prima")
    print("2. Bilangan Ganjil")
    print("3. Bilangan Genap")
    print("0. Keluar")
    menu = input("Masukan Pilihan Menu : ")

    if menu == '1':
        cek_prima()
    elif menu == '2':
        cek_ganjil()
    elif menu == '3':
        cek_genap()
    elif menu == '0':
        print("\nProgram Selesai Terima Kasih :)")
        break
    else:
        print("\nPilihan Tidak Ada Di Menu")
    input("\n\nEnter Untuk Melanjutkan...")
