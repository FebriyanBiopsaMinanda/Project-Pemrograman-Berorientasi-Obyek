import os


class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def add_music(self, judul, penyanyi, genre):
        print(
            f"\nAdding a generic music : {judul} by {penyanyi}, Genre: {genre}")

    def display_music(self):
        return f"{self.judul:<20} :  {self.penyanyi:<20} {self.genre}"

    def delete_music(self, judul, songs_list):
        for song in songs_list:
            if song.judul == judul:
                songs_list.remove(song)
                return


class Japanese_Song(Music):
    def __init__(self, judul, penyanyi, genre):
        super().__init__(judul, penyanyi, genre)

    def add_music(self, judul, penyanyi, genre):
        print(
            f"\nAdding a Japanese Song : {judul} by {penyanyi}, Genre: {genre}")

    def display_music(self):
        return f"{self.judul:<20} {self.penyanyi:<20} {self.genre}"

    def delete_music(self, judul, songs_list):
        super().delete_music(judul, songs_list)


class Korean_Song(Music):
    def __init__(self, judul, penyanyi, genre):
        super().__init__(judul, penyanyi, genre)

    def add_music(self, judul, penyanyi, genre):
        print(
            f"\nAdding a Korean Song : {judul} by {penyanyi}, Genre: {genre}")

    def display_music(self):
        return f"{self.judul:<20} {self.penyanyi:<20} {self.genre}"

    def delete_music(self, judul, songs_list):
        super().delete_music(judul, songs_list)


class English_Song(Music):
    def __init__(self, judul, penyanyi, genre):
        super().__init__(judul, penyanyi, genre)

    def add_music(self, judul, penyanyi, genre):
        print(
            f"\nAdding a English Song : {judul} by {penyanyi}, Genre: {genre}")

    def display_music(self):
        return f"{self.judul:<20} {self.penyanyi:<20} {self.genre}"

    def delete_music(self, judul, songs_list):
        super().delete_music(judul, songs_list)


def format_display():
    print(f"\n{'Judul':<20} {'Penyanyi':<20} {'Genre'}")
    print(f"{'-'*50}")


def add_new_japanese_song(song_list):
    print("\n>>> Add Japanese Song")
    judul = input("\nMasukan Judul Music : ")
    ada_judul = False
    # Cek Judul Apakah Sudah Terdaftar
    for song in song_list:
        if song.judul == judul:
            ada_judul = True
            break

    if ada_judul == False:
        penyanyi = input(f"Masukan Penyanyi dari {judul} : ")
        genre = "J-Song"
        new_song = Japanese_Song(judul, penyanyi, genre)
        song_list.append(new_song)
        songs.append(new_song)
        print(
            f"\nSuccessfully added {judul} by {penyanyi} to the Japanese Song !")
    else:
        print(f"\nMusic with the title {judul} already exists !")


def add_new_korean_song(song_list):
    print("\n>>> Add Korean Song")
    judul = input("\nMasukan Judul Music : ")
    ada_judul = False
    # Cek Judul Apakah Sudah Terdaftar
    for song in song_list:
        if song.judul == judul:
            ada_judul = True
            break

    if ada_judul == False:
        penyanyi = input(f"Masukan Penyanyi dari {judul} : ")
        genre = "K-Song"
        new_song = Korean_Song(judul, penyanyi, genre)
        song_list.append(new_song)
        songs.append(new_song)
        print(
            f"\nSuccessfully added {judul} by {penyanyi} to the Korean Song !")
    else:
        print(f"\nMusic with the title {judul} already exists !")


def add_new_english_song(song_list):
    print("\n>>> Add English Song")
    judul = input("\nMasukan Judul Music : ")
    ada_judul = False
    # Cek Judul Apakah Sudah Terdaftar
    for song in song_list:
        if song.judul == judul:
            ada_judul = True
            break

    if ada_judul == False:
        penyanyi = input(f"Masukan Penyanyi dari {judul} : ")
        genre = "E-Song"
        new_song = English_Song(judul, penyanyi, genre)
        song_list.append(new_song)
        songs.append(new_song)
        print(
            f"\nSuccessfully added {judul} by {penyanyi} to the English Song !")
    else:
        print(f"\nMusic with the title {judul} already exists !")


# Object Japanese Song
js1 = Japanese_Song("Sprakle", "Radwimps", "J-Song")
js2 = Japanese_Song("Suzume", "Radwimps", "J-Song")
js3 = Japanese_Song("Idol", "Yoasobi", "J-Song")
js4 = Japanese_Song("Tell Me", "Milet", "J-Song")
js5 = Japanese_Song("Tower Of Flower", "Sayuri", "J-Song")
japanese_songs = [js1, js2, js3, js4, js5]

# Object Korean Song
ks1 = Korean_Song("Sheesh", "BabyMonster", "K-Song")
ks2 = Korean_Song("Kill This Love", "BlackPink", "K-Song")
ks3 = Korean_Song("Way Back Home", "Shaun", "K-Song")
ks4 = Korean_Song("Better Up", "BabyMonster", "K-Song")
ks5 = Korean_Song("Cupid", "Fifty Fifty", "K-Song")
korean_songs = [ks1, ks2, ks3, ks4, ks5]

# Object Engslish Song
es1 = English_Song("MockingBird", "Eminem", "E-Song")
es2 = English_Song("Thunder", "Imagine Dragons", "E-Song")
es3 = English_Song("Nobody", "OneRepublic", "E-Song")
es4 = English_Song("Daylight", "David Kushner", "E-Song")
es5 = English_Song("Bye bye bye", "NSYNC", "E-Song")
english_songs = [es1, es2, es3, es4, es5]

songs = list(japanese_songs + korean_songs + english_songs)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'='*15} Playlist Music {'='*15}")
    print("1. Japanese Song")
    print("2. Korean Song")
    print("3. English Song")
    print("4. Display All")
    print("5. Search Music")
    print("0. Keluar")
    menu = input("Masukan Pilihan Menu : ")

    # Japanese Song
    if menu == '1':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{'='*15} Japanese Song {'='*15}")
            print("1. Display Song")
            print("2. Add Song")
            print("3. Delete Song")
            print("0. Kembali")
            submenu = input("Masukan Pilihan Sub Menu Japenese Song : ")

            if submenu == '1':
                print("\n>> List Japanese Song")
                format_display()
                for song in japanese_songs:
                    print(song.display_music())
            elif submenu == '2':
                add_new_japanese_song(japanese_songs)
            elif submenu == '3':
                print("\n>> Delete Japanese Song")
                song_to_delete = input(
                    "\nMasukan Judul Music yg Ingin Di Hapus : ")
                found = False
                for song in songs:
                    if song.judul == song_to_delete:
                        found = True
                        break

                if found == True:
                    song.delete_music(song_to_delete, songs)
                    print(
                        f"\nDeleted '{song_to_delete}' from the Japanese Song.")
                    song.delete_music(song_to_delete, japanese_songs)
                else:
                    print(f"\nSong '{song_to_delete}' not found in the list.")
            elif submenu == '0':
                break
            else:
                print("\nOption Not In Menu Japanese Song")
            input("\n\nEnter Untuk Melanjutkan...")

    # Korean Song
    elif menu == '2':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{'='*15} Korean Song {'='*15}")
            print("1. Display Song")
            print("2. Add Song")
            print("3. Delete Song")
            print("0. Kembali")
            submenu = input("Masukan Pilihan Sub Menu Korean Song : ")

            if submenu == '1':
                print("\n>> List Korean Song")
                format_display()
                for song in korean_songs:
                    print(song.display_music())
            elif submenu == '2':
                add_new_korean_song(korean_songs)
            elif submenu == '3':
                print("\n>> Delete Korean Song")
                song_to_delete = input(
                    "\nMasukan Judul Music yg Ingin Di Hapus : ")
                found = False
                for song in songs:
                    if song.judul == song_to_delete:
                        found = True
                        break

                if found == True:
                    song.delete_music(song_to_delete, songs)
                    print(
                        f"\nDeleted '{song_to_delete}' from the Korean Song.")
                    song.delete_music(song_to_delete, korean_songs)
                else:
                    print(f"\nSong '{song_to_delete}' not found in the list.")
            elif submenu == '0':
                break
            else:
                print("\nOption Not In Menu Korean Song")
            input("\n\nEnter Untuk Melanjutkan...")

    # English Song
    elif menu == '3':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{'='*15} English Song {'='*15}")
            print("1. Display Song")
            print("2. Add Song")
            print("3. Delete Song")
            print("0. Kembali")
            submenu = input("Masukan Pilihan Sub Menu English Song : ")

            if submenu == '1':
                print("\n>> List English Song")
                format_display()
                for song in english_songs:
                    print(song.display_music())
            elif submenu == '2':
                add_new_english_song(english_songs)
            elif submenu == '3':
                print("\n>> Delete English Song")
                song_to_delete = input(
                    "\nMasukan Judul Music yg Ingin Di Hapus : ")
                found = False
                for song in songs:
                    if song.judul == song_to_delete:
                        found = True
                        break

                if found == True:
                    song.delete_music(song_to_delete, songs)
                    print(
                        f"\nDeleted '{song_to_delete}' from the English Song.")
                    song.delete_music(song_to_delete, english_songs)
                else:
                    print(f"\nSong '{song_to_delete}' not found in the list.")
            elif submenu == '0':
                break
            else:
                print("\nOption Not In Menu English Song")
            input("\n\nEnter Untuk Melanjutkan...")

    # Display Song
    elif menu == '4':
        print("\n>> List Song")
        print(f"\nTotal Songs = {len(songs)}")
        format_display()
        sorted_songs = sorted(songs, key=lambda song: song.judul)
        for song in sorted_songs:
            print(song.display_music())

    # Search Song
    elif menu == '5':
        print("\n>> Search Song")
        search_song = input("\nMasukan Penyanyi yg Ingin Di Cari : ")
        found = False
        result = []
        for song in songs:
            if song.penyanyi == search_song:
                result.append(song)
                found = True

        if found == True:
            format_display()
            for song in result:
                print(song.display_music())
        else:
            print(f"\n{search_song} is not in the music list!")

    elif menu == '0':
        break

    else:
        print("\nOption Not In Menu")
    input("\n\nEnter Untuk Melanjutkan...")
