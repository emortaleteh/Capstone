from tabulate import tabulate

List_RS = [
    {'NIM': '1', 'Nama': 'Brian', 'Umur': 25, 'Dokter': 'Spesialis Gigi', 'Jenis Kelamin': 'Laki-laki', 'Gaji': 1500000},
    {'NIM': '2', 'Nama': 'Salsa', 'Umur': 35, 'Dokter': 'Spesialis Mata', 'Jenis Kelamin': 'Perempuan', 'Gaji': 2000000},
    {'NIM': '3', 'Nama': 'Wati', 'Umur': 32, 'Dokter': 'Spesialis Telinga', 'Jenis Kelamin': 'Perempuan', 'Gaji': 1800000},
    {'NIM': '4', 'Nama': 'Ica', 'Umur': 26, 'Dokter': 'Spesialis Hidung', 'Jenis Kelamin': 'Perempuan', 'Gaji': 1700000},
    {'NIM': '5', 'Nama': 'Morgan', 'Umur': 28, 'Dokter': 'Spesialis Tenggorokan', 'Jenis Kelamin': 'Laki-laki', 'Gaji': 1900000},
    {'NIM': '6', 'Nama': 'Anjas', 'Umur': 20, 'Dokter': 'Spesialis Hewan', 'Jenis Kelamin': 'Laki-laki', 'Gaji': 1600000},
    {'NIM': '7', 'Nama': 'Andi', 'Umur': 21, 'Dokter': 'Spesialis Jantung', 'Jenis Kelamin': 'Laki-laki', 'Gaji': 2100000},
    {'NIM': '8', 'Nama': 'Priscilla', 'Umur': 29, 'Dokter': 'Spesialis Cinta', 'Jenis Kelamin': 'Perempuan', 'Gaji': 2200000}
]

List_Gaji = [{'Uang' : 100000000}]

# Fungsi untuk menu utama
def mainmenu():
    while True:
        print('''
    Main Menu
    1. Tampilkan data tenaga medis.
    2. Menambahkan data tenaga medis.
    3. Menghapus data tenaga medis.
    4. Update data tenaga medis.
    5. Gaji tenaga medis.
    6. Exit.
    ''')
        menu = input("Masukkan menu yang akan anda pilih: ").strip()
        if menu == '1':
            menu1()
        elif menu == '2':
            menu2()
        elif menu == '3':
            tabelmenu3()
        elif menu == '4':
            tabelmenu4()
        elif menu == '5':
            menu5()
        elif menu == '6':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print('\nInput yang anda masukkan tidak valid! Silahkan coba lagi.')

# Fungsi untuk menampilkan semua data tenaga medis
def menu1():
    while True:
        print('''
            Pilihan:
            1. Tampilkan data berdasarkan key
            2. Tampilkan data lengkap berdasarkan NIM
            3. Tampilkan semua data
            4. Kembali ke main menu
            ''') 
        pilihan = input("Masukkan pilihan (1-4): ").strip()

        if pilihan == '1':
            menu1_1()
        elif pilihan == '2':
            menu1_2()
        elif pilihan == '3':                            
            print('Daftar Tenaga Medis Lengkap:')
            headers = ['NIM', 'Nama', 'Umur', 'Dokter', 'Jenis Kelamin', 'Gaji']
            rows = [[isi['NIM'], isi['Nama'], isi['Umur'], isi['Dokter'], isi['Jenis Kelamin'], isi['Gaji']] for isi in List_RS]
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
            menu1lanjut()
        elif pilihan == '4':
            break
        else:
            print('Pilihan tidak valid! Silahkan coba lagi.')
            menu1()

# Fungsi menu 1 pilihan 1
def menu1_1():
    key = input("Masukkan key yang ingin ditampilkan (Nama/Umur/Dokter/Jenis Kelamin/Gaji): ").strip().lower().title()
    if key in List_RS[0]:
        headers = [key]
        rows = [[isi[key]] for isi in List_RS]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        menu1lanjut()
    else:
        print("Key tidak valid!")
        menu1_1()

# Fungsi menu 1 pilihan 2
def menu1_2():
    nim = input("Masukkan NIM yang ingin ditampilkan: ").strip()
    for isi in List_RS:
        if isi['NIM'] == nim:
            print('Daftar Tenaga Medis Berdasarkan NIM: ')
            headers = ['NIM', 'Nama', 'Umur', 'Dokter', 'Jenis Kelamin', 'Gaji']
            rows = [[isi['NIM'], isi['Nama'], isi['Umur'], isi['Dokter'], isi['Jenis Kelamin'], isi['Gaji']]]
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
            menu1lanjut()
    else:
        print(f'Tenaga Medis dengan NIM {nim} tidak ditemukan!')
        menu1_2()

# Fungsi input NIM
def NIM():
    while True:
        nim = input('\nMasukkan NIM Tenaga Medis: ').strip()      
        if not nim.isdigit() or int(nim) <= 0:
            print('NIM yang anda masukkan tidak valid! Silahkan coba lagi.')
            continue

        if any(isi_nim['NIM'] == nim for isi_nim in List_RS):
            print('NIM sudah ada! Silahkan coba lagi.')
        else:
            print(f'\nNIM {nim} diterima!')
            return nim

# Fungsi input Nama        
def Nama():
    while True:
        nama = input('\nMasukkan Nama Tenaga Medis: ').strip().title()
        if any(char.isdigit() for char in nama):
            print('Nama yang anda masukkan tidak valid! Silahkan coba lagi.')
        else:
            print(f"\nNama {nama} diterima!")
            return nama

# Fungsi input Umur
def Umur():
    while True:
        try:
            umur = int(input('\nMasukkan Umur Tenaga Medis: '))
            if umur <= 0:
                print('Umur yang anda masukkan tidak valid! Silahkan coba lagi.')
            else:
                print(f'\nUmur {umur} tahun diterima!')
                return umur
        except ValueError:
            print('Data yang anda masukkan tidak valid! Silahkan coba lagi.')

# Fungsi input Dokter
def Dokter():
    while True:
        spesialisasi = input('\nMasukkan Spesialisasi Tenaga Medis: ').strip().title()
        if any(char.isdigit() for char in spesialisasi):
            print('Data yang anda masukkan tidak valid! Silahkan coba lagi.')
        else:
            spesialisasi = f'Spesialis {spesialisasi}'
            print(f'\n{spesialisasi} diterima!')
            return spesialisasi

# Fungsi input Kelamin
def Kelamin():
    while True:
        kelamin = input('\nMasukkan Jenis Kelamin Tenaga Medis: (L/P) ').strip().upper()
        if kelamin == 'L':
            print(f'\nJenis kelamin Laki-laki diterima!')
            return 'Laki-laki'
        elif kelamin == 'P':
            print(f'\nJenis kelamin Perempuan diterima!')
            return 'Perempuan'
        else:
            print('Input yang anda masukkan tidak valid! Silahkan coba lagi.')
            
# Fungsi input gaji
def Gaji():
    while True:
        try:
            gaji = int(input('\nMasukkan Gaji Tenaga Medis: '))
            if gaji <= 0:
                print('Gaji yang anda masukkan tidak valid! Silahkan coba lagi.')
            else:
                print(f'\nGaji {gaji} diterima!')
                return gaji
        except ValueError:
            print('Data yang anda masukkan tidak valid! Silahkan coba lagi.')

# Fungsi pilihan menu 2
def menu2opsi():
    while True:
        print('''
            Pilihan:
            1. Menambah data tenaga medis baru.
            2. Kembali ke main menu.
            ''') 
        pilihan = input("Masukkan pilihan (1-2): ").strip()

# Fungsi menu 2
def menu2():
    print('\nMasukkan data tenaga medis baru:')    
    nim = NIM()
    nama = Nama()
    umur = Umur()
    dokter = Dokter()
    kelamin = Kelamin()
    gaji = Gaji()
    
    print('\nData yang akan ditambahkan:')
    print(f'NIM: {nim}')
    print(f'Nama: {nama}')
    print(f'Umur: {umur}')
    print(f'Dokter: {dokter}')
    print(f'Jenis Kelamin: {kelamin}')
    print(f'Gaji: {gaji}')
    while True:   
        konfirmasi = input('\nApakah anda yakin untuk menambahkan data tersebut? (y/n): ').strip().lower()
        if konfirmasi == 'y':
            List_RS.append({'NIM': nim, 'Nama': nama, 'Umur': umur, 'Dokter': dokter, 'Jenis Kelamin': kelamin, 'Gaji': gaji})
            print('Data Tenaga Medis berhasil ditambahkan!')
            menu2lanjut()
        elif konfirmasi == 'n':
            print('Penambahan data dibatalkan.')
            menu2lanjut()
        else:
            print('Input tidak valid.')

# Fungsi tabel menu 3
def tabelmenu3():
    print('Daftar Tenaga Medis Lengkap:')
    headers = ['NIM', 'Nama', 'Umur', 'Dokter', 'Jenis Kelamin', 'Gaji']
    rows = [[isi['NIM'], isi['Nama'], isi['Umur'], isi['Dokter'], isi['Jenis Kelamin',isi['Gaji']]] for isi in List_RS]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
    menu3()

# Fungsi menu3    
def menu3():        
    print('\nMasukkan NIM Tenaga Medis yang ingin dihapus:')
    nim = input("NIM: ").strip()
    for i in range(len(List_RS)):
        if List_RS[i]['NIM'] == nim:
            print('\nData yang akan dihapus:')
            headers = ['NIM', 'Nama', 'Umur', 'Dokter', 'Jenis Kelamin','Gaji']
            rows = [[List_RS[i]['NIM'], List_RS[i]['Nama'], List_RS[i]['Umur'], List_RS[i]['Dokter'], List_RS[i]['Jenis Kelamin', List_RS[i]['Gaji']]]]
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
            
            while True:
                konfirmasi = input('\nApakah Anda yakin ingin menghapus data ini? (y/n): ').strip().lower()
                if konfirmasi == 'y':
                    del List_RS[i]
                    print(f'Data Tenaga Medis dengan NIM {nim} berhasil dihapus!')
                    menu3lanjut()
                    return
                elif konfirmasi == 'n':
                    print('Penghapusan data dibatalkan.')
                    menu3lanjut()
                    return
                else:
                    print('Input tidak valid. Silakan masukkan y atau n.')
    else:
        print(f'Tenaga Medis dengan NIM {nim} tidak ditemukan!')
        menu3()

# Fungsi tabel menu 4
def tabelmenu4():
    print('Daftar Tenaga Medis Lengkap:')
    headers = ['NIM', 'Nama', 'Umur', 'Dokter', 'Jenis Kelamin', 'Gaji']
    rows = [[isi['NIM'], isi['Nama'], isi['Umur'], isi['Dokter'], isi['Jenis Kelamin', isi['Gaji']]] for isi in List_RS]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
    menu4()

# Fungsi menu 4
def menu4():
    print('\nMasukkan NIM tenaga medis yang ingin diedit :')
    nim = input("NIM: ").strip()
    for isi in List_RS:
        if isi['NIM'] == nim:
            print("\nMasukkan data baru tenaga medis :")
            isi['NIM'] = NIM()
            isi['Nama'] = Nama()
            isi['Umur'] = Umur()
            isi['Dokter'] = Dokter()
            isi['Jenis Kelamin'] = Kelamin()
            isi['Gaji'] = Gaji()
            print("\nData Tenaga Medis berhasil diperbarui!")
            print(f"NIM: {isi['NIM']}, Nama: {isi['Nama']}, Umur: {isi['Umur']}, Dokter: {isi['Dokter']}, Jenis Kelamin: {isi['Jenis Kelamin']}, 'Gaji': {[isi['Gaji']]}")
            break
    else:
        print(f'Tenaga Medis dengan NIM {nim} tidak ditemukan!')
        menu4()

# Fungsi menu 5
def menu5():
    while True:
        print('''Menu:
        1. Tampilkan Data Kas dan Gaji Dokter
        2. Tambahkan Uang Kas
        3. Gaji Dokter
        4. Keluar''')
        
        try:
            pilihan = int(input('Masukkan pilihan: '))
            if pilihan == 1:
                menu5_1()
            elif pilihan == 2:
                menu5_2()            
            elif pilihan == 3:
                menu5_3()
            elif pilihan == 4:
                mainmenu()            
            else:
                print('Pilihan tidak valid. Silakan pilih 1-4.')
        except ValueError:
            print('Input harus berupa angka!')

# FUngsi menu 5 pilihan 1          
def menu5_1():
    print('\nData Kas:')
    print(tabulate(List_Gaji, headers='keys', tablefmt='fancy_grid'))
    print('\nData Gaji Dokter:')
    print(tabulate(List_RS, headers='keys', tablefmt='fancy_grid'))        
    menu5lanjut()

# Fungsi menu 5 pilihan 2
def menu5_2():
    while True:
        try:
            tambahan = int(input('Masukkan jumlah uang yang ingin ditambahkan: '))
            if tambahan < 0:
                print('Jumlah uang tidak boleh negatif!')
            else:
                List_Gaji[0]['Uang'] += tambahan
                print(f'Uang kas berhasil ditambahkan. Total uang kas sekarang: {List_Gaji[0]["Uang"]}')
                menu5lanjut()
        except ValueError:
            print('Input harus berupa angka!')

# Fungsi menu 5 pilihan 3
def menu5_3():
    print('\nDaftar Dokter:')
    print(tabulate(List_RS, headers='keys', tablefmt='fancy_grid'))                
    while True:
        try:
            nim = input('\nMasukkan NIM dokter yang akan digaji: ')
            dokter = next((d for d in List_RS if d['NIM'] == nim), None)
                        
            if dokter:
                gaji = dokter['Gaji']
                if List_Gaji[0]['Uang'] >= gaji:
                    List_Gaji[0]['Uang'] -= gaji
                    print(f'Dokter {dokter["Nama"]} telah digaji sebesar {gaji}. Sisa uang kas: {List_Gaji[0]["Uang"]}')
                    menu5lanjut()
                else:
                    print('Uang kas tidak mencukupi untuk menggaji dokter ini.')
                    menu5lanjut()
                break
            else:
                print(f'Dokter dengan NIM {nim} tidak ditemukan.')
        except ValueError:
            print('Input tidak valid!')

# Fungsi menu 1 lanjutan
def menu1lanjut():
        kembali = input('\nApakah Anda ingin kembali ke menu 1? (y/n): ').strip().lower()
        if kembali == 'n':
            mainmenu()
        elif kembali == 'y':
            menu1()
        else:
            print('Input yang anda masukkan tidak valid! Silahkan coba lagi.')
            menu1lanjut()

# Fungsi menu 2 lanjutan
def menu2lanjut():
        kembali = input('\nApakah Anda ingin kembali ke menu 2? (y/n): ').strip().lower()
        if kembali == 'n':
            mainmenu()
        elif kembali == 'y':
            menu2()
        else:
            print('Input yang anda masukkan tidak valid! Silahkan coba lagi.')
            menu2lanjut()

# Fungsi menu 3 lanjutan
def menu3lanjut():
        kembali = input('\nApakah Anda ingin kembali ke menu 3? (y/n): ').strip().lower()
        if kembali == 'n':
            mainmenu()
        elif kembali == 'y':
            menu3()
        else:
            print('Input yang anda masukkan tidak valid! Silahkan coba lagi.')
            menu3lanjut()

# Fungsi menu 4 lanjutan
def menu4lanjut():
        kembali = input('\nApakah Anda ingin kembali ke menu 4? (y/n): ').strip().lower()
        if kembali == 'n':
            mainmenu()
        elif kembali == 'y':
            menu4()
        else:
            print('Input yang anda masukkan tidak valid! Silahkan coba lagi.')
            menu4lanjut()

# Fungsi menu 5 lanjutan
def menu5lanjut():
        kembali = input('\nApakah Anda ingin kembali ke menu 5? (y/n): ').strip().lower()
        if kembali == 'n':
            mainmenu()
        elif kembali == 'y':
            menu5()
        else:
            print('Input yang anda masukkan tidak valid! Silahkan coba lagi.')
            menu5lanjut()  


# Jalankan program
mainmenu()