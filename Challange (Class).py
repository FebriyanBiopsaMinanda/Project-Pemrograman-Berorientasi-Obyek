import os

def rupiah(uang) :
    x = str(uang)
    if len(x) <= 3:
        return 'Rp. ' + x
    else:
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b

class daftar_menu:
    def __init__(self, nama, harga):
        self.harga = harga


makanan_1 = daftar_menu("Magelangan", 13000)
makanan_2 = daftar_menu("Nasi Goreng", 12000)
makanan_3 = daftar_menu("Mie Ayam", 10000)
makanan_4 = daftar_menu("Bakso Urat", 10000)

minuman_1 = daftar_menu("Es Teh Manis", 2000)
minuman_2 = daftar_menu("Es Jeruk", 3000)
minuman_3 = daftar_menu("Jus Alpukat", 7000)
minuman_4 = daftar_menu("Milk Shake", 10000)

daftar_makanan = [makanan_1, makanan_2, makanan_3, makanan_4]
daftar_minuman = [minuman_1, minuman_2, minuman_3, minuman_4]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'='*10} PILIHAN MENU {'='*10}")
    print("1. Lihat Daftar Makanan")
    print("2. Lihat Daftar Minuman")
    print("3. Tambah Menu")
    print("0. Keluar")
    pilihan = input("Masukan Pilihan : ")

    if pilihan == '1':
        print(f"\n{'='*10} DAFTAR MAKANAN {'='*10}")
        for makanan in daftar_makanan:
            print(f"{makanan.nama}\t-> {rupiah(makanan.harga)}")
        print(f"\n{'='*36}")

    elif pilihan == '2':
        print(f"\n{'='*10} DAFTAR MINUMAN {'='*10}")
        for minuman in daftar_minuman:
            print(f"{minuman.nama}\t-> {rupiah(minuman.harga)}")
        print(f"\n{'='*36}")

    elif pilihan == '3':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{'='*10} TAMBAH MENU {'='*10}")
            print("1. Tambah Makanan")
            print("2. Tambah Minuman")
            print("0. Kembali")
            sub_menu = input("Masukan Pilihan : ")

            if sub_menu == '1':
                try:
                    print(f"\n{'='*10} TAMBAH MAKANAN {'='*10}")
                    nama = str(input("Masukan Nama Makanan : "))
                    harga = int(input("Masukan Harga Makanan : "))
                    tambah_makanan = daftar_menu(nama=nama, harga=harga)
                    daftar_makanan.append(tambah_makanan)
                    print("\nMakanan Berhasil Ditambahkan")
                    break
                except:
                    print("\nMakanan Gagal Ditambahkan")
                    input("\n\nEnter Untuk Melanjutkan ...")
                    continue

            elif sub_menu == '2':
                try:
                    print(f"\n{'='*10} TAMBAH MINUMAN {'='*10}")
                    nama = str(input("Masukan Nama Minuman : "))
                    harga = int(input("Masukan Harga Minuman : "))

                    tambah_minuman = daftar_menu(nama=nama, harga=harga)
                    daftar_minuman.append(tambah_minuman)
                    print("\nMinuman Berhasil Ditambahkan")
                    break
                except:
                    print("\nMinuman Gagal Ditambahkan")
                    input("\n\nEnter Untuk Melanjutkan ...")
                    continue

            elif sub_menu == '0':
                break

    elif pilihan == '0':
        print("\nTerima Kasih")
        break

    else:
        print("\nPilihan tidak Ada Di Menu")
    input("\n\nEnter Untuk Melanjutkan ...")
