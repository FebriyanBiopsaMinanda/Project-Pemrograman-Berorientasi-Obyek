import os


def rupiah(uang):
    x = str(uang)
    if len(x) <= 3:
        return 'Rp.' + x
    else:
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b


class Debitur:
    def __init__(self, ktp, nama, limit_pinjaman):
        self.__ktp = ktp
        self.nama = nama
        self._limit_pinjaman = limit_pinjaman

    def get_ktp(self):
        return self.__ktp

    def set_ktp(self, ktp):
        self.__ktp = ktp

    def DisplayDebitur(self):
        print("{:<10} {:>10}{:>20}".format(
            self.nama, self.__ktp, rupiah(self._limit_pinjaman)))


class Pinjaman(Debitur):
    def __init__(self, nama, limit_pinjaman, pinjaman, bunga, bulan):
        self.nama = nama
        self.limit_pinjaman = limit_pinjaman
        self.pinjaman = pinjaman
        self.bunga = bunga
        self.bulan = bulan

        # Perhitungan Angsuran
        self.angsuran_pokok = self.pinjaman * (self.bunga / 100)
        self.angsuran_bulan = self.angsuran_pokok / self.bulan
        self.total_angsuran = self.angsuran_pokok + self.angsuran_bulan

    def DisplayAngsuran(self):
        print("{:<10}{:>17}{:>5}% {:>10}{:>25}".format(
            self.nama, rupiah(self.pinjaman), self.bunga, self.bulan, rupiah(int(self.total_angsuran))))


def Display_All_Debitur(list_debitur):
    print(f"\n{'='*15} Daftar Debitur {'='*15}")
    print("\n{:<5} {:>10}{:>18}".format(
        "Nama Debitur", "No KTP", "Limit Pinjaman"))
    print("-" * 50)

    for debitur in list_debitur:
        debitur.DisplayDebitur()
    input("\n\nEnter Untuk Melanjutkan...")


def Display_One_Debitur(list_debitur):
    print("\n>>> Cari Debitur")
    nama = input("\nMasukan Nama Debitur yg Ingin Di Cari : ")

    # Cek apakah Nama ada
    ada_nama = False
    for debitur in list_debitur:
        if debitur.nama == nama:
            ada_nama = True
            break

    if ada_nama:
        print(f"\n{'='*15} Hasil Cari Debitur {'='*15}")
        print("\n{:<5} {:>10}{:>18}".format(
            "Nama Debitur", "No KTP", "Limit Pinjaman"))
        print("-" * 50)
        for debitur in list_debitur:
            if debitur.nama == nama:
                debitur.DisplayDebitur()
                break
    else:
        print(f"\n{nama} Tidak ditemukan!")
    input("\n\nEnter Untuk Melanjutkan...")


def Add_Debitur(list_debitur):
    try:
        print("\n>>> Tambah Debitur")
        ktp_baru = int(input("\nMasukkan KTP baru: "))

        # Cek apakah KTP sudah ada
        ada_ktp = False
        for debitur in list_debitur:
            if debitur.get_ktp() == ktp_baru:
                ada_ktp = True
                break

        if ada_ktp:
            print("\nKTP sudah ada!")
        else:
            nama_baru = input("Masukkan nama baru: ")
            limit_baru = int(input("Masukkan limit pinjaman baru: "))
            debitur_baru = Debitur(ktp_baru, nama_baru, limit_baru)
            list_debitur.append(debitur_baru)
            print(f"\nDebitur Atas Nama {nama_baru} berhasil ditambahkan.")
    except ValueError as e:
        print(f"\nEror : {e}")
    input("\n\nEnter Untuk Melanjutkan...")


def FindDebitur(list_debitur, nama):
    for debitur in list_debitur:
        if debitur.nama == nama:
            return debitur
    return None


def AddPinjamanan(list_debitur):
    try:
        print("\n>>> Tambah Pinjaman")
        nama_pinjam = input("\nSiapa yg Ingin Meminjam : ")
        ada_nama = False
        # Cek Nama Apakah Sudah Terdaftar
        for debitur in list_debitur:
            if debitur.nama == nama_pinjam:
                ada_nama = True
                break

        if ada_nama:
            pinjaman = int(input("Masukan Jumlah Pinjaman : "))
            debitur = FindDebitur(list_debitur, nama_pinjam)
            if debitur:
                limit_pinjaman = debitur._limit_pinjaman
                if limit_pinjaman < pinjaman:
                    print("\nJumlah Pinjaman Melebihi Limit")
                else:
                    bunga = int(input("Masukan Suku Bunga : "))
                    bulan = int(input("Masukan Limit Waktu dalam Bulan : "))
                    pinjaman_baru = Pinjaman(
                        nama_pinjam, limit_pinjaman, pinjaman, bunga, bulan)
                    list_pinjam.append(pinjaman_baru)
                    print(
                        f"\nPinjaman Atas Nama {nama_pinjam} berhasil ditambahkan.")
            else:
                print("Terjadi kesalahan dalam mencari data debitur.")

        else:
            print(f"\n{nama_pinjam} Tidak Terdaftar")
        input("\n\nEnter Untuk Melanjutkan...")
    except ValueError as e:
        print(f"\nEror : {e}")
        input("\n\nEnter Untuk Melanjutkan...")


def Display_Pinjaman(list_pinjam):
    print(f"\n{'='*25} Daftar Pinjaman {'='*25}")
    print("\n{:<10}{:>12}{:>10} {:>11}{:>25}".format(
        "Nama Debitur", "Pinjaman", "Bunga", "Bulan", "Angsuran(Bln)"))
    print("-" * 70)

    for pinjam in list_pinjam:
        pinjam.DisplayAngsuran()
    input("\n\nEnter Untuk Melanjutkan...")


Debitur1 = Debitur(123, "Rimuru", 50000000)
Debitur2 = Debitur(234, "Diablo", 3500000)
Debitur3 = Debitur(345, "Carera", 3000000)
Debitur4 = Debitur(456, "Testarossa", 3000000)
Debitur5 = Debitur(567, "Ultima", 2500000)
list_debitur = [Debitur1, Debitur2, Debitur3, Debitur4, Debitur5]
list_pinjam = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'='*15} Aplikasi Admin Pinjol {'='*15}")
    print("1. Kelola Debitur")
    print("2. Pinjaman")
    print("0. Keluar")
    menu = input("Masukan Pilihan : ")

    if menu == "1":
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{'='*15} Kelola Debitur {'='*15}")
            print("1. Tampilkan Semua Debitur")
            print("2. Cari Debitur")
            print("3. Tambah Debitur")
            print("0. Kembali")
            submenu = input("Masukan Pilihan Sub Menu : ")

            if submenu == '1':
                Display_All_Debitur(list_debitur)
            elif submenu == '2':
                Display_One_Debitur(list_debitur)
            elif submenu == '3':
                Add_Debitur(list_debitur)
            elif submenu == '0':
                break
            else:
                print("\nPilihan Tidak Ada Di Menu")
                input("\n\nEnter Untuk Melanjutkan...")

    elif menu == '2':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{'='*15} Menu Pinjaman {'='*15}")
            print("1. Tambah Pinjaman")
            print("2. Tampilkan Pinjaman")
            print("0. Kembali")
            submenu = input("Masukan Pilihan Sub Menu : ")

            if submenu == '1':
                AddPinjamanan(list_debitur)
            elif submenu == '2':
                Display_Pinjaman(list_pinjam)
            elif submenu == '0':
                break
            else:
                print("\nPilihan Tidak Ada Di Menu")
                input("\n\nEnter Untuk Melanjutkan...")

    elif menu == '0':
        print("\nTerima Kasih\n")
        break

    else:
        print("\nPilihan Tidak Ada Di Menu")
    input("\n\nEnter Untuk Melanjutkan...")
