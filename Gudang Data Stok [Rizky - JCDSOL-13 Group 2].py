#Rizky Rahmatullah Putra
#JCDSOL-13 Group 2
#Capstone Project Modul 1 Pyton - Stok Gudang

listGadget  = [    #function untuk melihat list stok Gadget
    {
        'Kode Gadget': 'WH01GD',
        'Nama Gadget': '15ProMax',
        'Merk': 'Iphone',
        'Jenis': 'Smartphone',
        'Harga' : 25000000,
        'Stok' : 50
    },
    {
        'Kode Gadget': 'WH02GD',
        'Nama Gadget': 'S9Ultra5G',
        'Merk': 'Samsung',
        'Jenis': 'Tablet',
        'Harga' : 20000000,
        'Stok' : 30
    },
    {
        'Kode Gadget': 'WH03GD',
        'Nama Gadget': 'ThinkpadX270',
        'Merk': 'Lenovo',
        'Jenis': 'Laptop',
        'Harga' : 15000000,
        'Stok' : 25
    }
]

def halo():  #function untuk melihat menu utama
    print(f'''
        Hallo Admin Gadget Warehouse
        
        List menu:

        1. Melihat Daftar Stok Gadget
        2. Menambahkan Daftar Stok Gadget
        3. Update Daftar Stok Gadget
        4. Menghapus Daftar Stok Gadget
        5. Keluar
    ''')

def showGadget1(): #1.1 function untuk melihat semua stok Gadget
    print('\n-----  List Stock Gadget  -----\n')
    print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
    for i in range(len(listGadget)):
        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))

def showKodeGadget(): #1.2.1 function untuk melihat berdasarkan pencarian kode Gadget
        kodeGadget = input('\n   Masukkan kode Gadget : ')
        print('\n----- List Stock Gadget -----\n')
        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
        for i in range(len(listGadget)):
            if kodeGadget == listGadget[i]['Kode Gadget']:
                print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))
                break
        else:
            print('\n     "Data tidak ditemukan"')

def showKeyWord(): #1.2.2 function untuk melihat berdasarkan pencarian nama/jenis/merk
        Search = input('\n     Masukkan keyword : ')
        print('\n----- List Stock Gadget -----\n')
        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
        for i in range(len(listGadget)):
            if  Search == listGadget[i]['Nama Gadget'] or Search == listGadget[i]['Merk'] or Search == listGadget[i]['Jenis']:
                print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))

def showHarga(): #1.2.3 function untuk melihat berdasarkan range harga
        Harga1 = int(input('\n     Masukkan harga minimum : '))
        Harga2 = int(input('     Masukkan harga maksimum : '))
        print('\n----- List Stock Gadget -----\n')
        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
        for i in range(len(listGadget)):
            if Harga1 <= listGadget[i]['Harga'] <= Harga2:
                print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))

def showStok(): #1.2.4 function untuk melihat berdasarkan jumlah stok
        Stok = int(input('\n     Masukkan stok maksimum yang dicari : '))
        print('\n----- List Stock Gadget -----\n')
        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
        for i in range(len(listGadget)):
            if listGadget[i]['Stok'] <= Stok:
                print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))

def showGadget2(): #1.2 function untuk pencarian dengan kata kunci
    while True:
        menu_showGadget2 = input ('''
        1. Pencarian menggunakan kode Gadget 
        2. Pencarian menggunakan keyword
        3. Pencarian menggunakan range harga
        4. Pencarian menggunakan jumlah stok tersedia
        5. Kembali ke menu sebelumnya
        Ketik nomor menu yang ingin dijalankan : ''')

        if menu_showGadget2 == '1' :
            showKodeGadget()
        elif menu_showGadget2 == '2' :
            showKeyWord()
        elif menu_showGadget2 == '3':
            showHarga()
        elif menu_showGadget2 == '4':
            showStok()
        elif menu_showGadget2 == '5':
            break

def readData(): #1 Fitur READ = function menampilkan menu read data
    while True:
        menuRead = input('''
        1. Tampilkan seluruh data stok Gadget
        2. Tampilkan data pencarian kata kunci
        3. Kembali ke menu utama
        Ketik nomor menu yang ingin dijalankan : ''')

        if menuRead == '1' :
            showGadget1()
        elif menuRead == '2' :
            showGadget2()
        elif menuRead == '3' :
            break
            
def addGadgets(): #2.1 function menambahkan data / create data
    while True:
        inKode = input('\n        Masukkan kode Gadget : ')
        inGadget = input('        Masukkan nama Gadget : ')
        inMerk = input('        Masukkan nama merk : ')
        inJenis = input('        Masukkan nama Jenis : ')
        inHarga = int(input('        Masukkan harga : '))
        inStok = int(input('        Masukkan jumlah stok : '))
        tambahan = {
        'Kode Gadget' : '{}'.format(inKode),
        'Nama Gadget' : '{}'.format(inGadget),
        'Merk' : '{}'.format(inMerk),
        'Jenis' : '{}'.format(inJenis),
        'Harga' : '{}'.format(inHarga),
        'Stok' : '{}'.format(inStok)
    }
        print('\n        Gadget yang ditambahkan adalah : ',tambahan)
        cekCreate = input('\n        Mohon dikonfirmasi kembali apakah data yang ingin ditambahkan sudah benar? (Y/N) : ').lower()
        if cekCreate == 'y':
            listGadget.append(tambahan)
            print('\n        "Gadget berhasil ditambahkan"')
            break
        elif cekCreate == 'n':
            print('\n        "Gadget tidak ditambahkan"')
            break
        else:
            break
        
def createData(): #2. Fitur CREATE = function menampilkan menu add / create data
    while True:
        menuCreate = input('''
        1. Tambahkan data Gadget baru
        2. Kembali ke menu utama
        
        Ketik nomor menu yang ingin dijalankan : ''')
    
        if menuCreate == '1' :
            addGadgets()
        elif menuCreate == '2' :
            break

def Update(): #3.1 function untuk update data
    codeUpdate = input('\n        Masukkan kode Gadget yang ingin diupdate : ')
    print('\n----- List Stock Gadget -----\n')
    for i in range(len(listGadget)):
        if codeUpdate == listGadget[i]['Kode Gadget']:
            print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
            print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))
            cekUpdate = input('\n        Mohon dikonfirmasi kembali apakah data yang ingin diupdate sudah benar? (Y/N) : ' ).lower()
            if cekUpdate == 'y':
                while True:
                    cmUpdate = input('''
                    1. Update Kode Gadget
                    2. Update Nama Gadget
                    3. Update Merk Gadget
                    4. Update Jenis Gadget
                    5. Update Harga Gadget
                    6. Update Stok Gadget
                    7. Selesai update data
                    
                    Ketik nomor menu yang ingin dijalankan : ''')
                   
                    if cmUpdate == '1':
                        listGadget[i]['Kode Gadget'] = input('\n        Update kode : ')
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))
                    elif cmUpdate == '2':
                        listGadget[i]['Nama Gadget'] = input('\n        Update nama : ')
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))
                    elif cmUpdate == '3':
                        listGadget[i]['Merk'] = input('\n        Update merk : ')
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))
                    elif cmUpdate == '4':
                        listGadget[i]['Jenis'] = input('\n        Update Jenis : ')
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))
                    elif cmUpdate == '5':
                        listGadget[i]['Harga'] = int(input('\n        Update harga : '))
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))
                    elif cmUpdate == '6':
                        listGadget[i]['Stok'] = int(input('\n        Update stok : '))
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Gadget\t|  Nama Gadget\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listGadget[i]['Kode Gadget'],listGadget[i]['Nama Gadget'],listGadget[i]['Merk'],listGadget[i]['Jenis'],listGadget[i]['Harga'],listGadget[i]['Stok']))
                    elif cmUpdate == '7':
                        break
            elif cekUpdate == 'n':
                print('\n        "Data tidak diupdate"')
                break
            else:
                print('\n        "Perintah yang anda masukkan salah"')
                break

def updateData(): #3.Fitur UPDATE = function menampilkan menu update data
    while True:
        menuUpdate = input('''
        1. Update data
        2. Kembali ke menu utama
        
        Ketik nomor menu yang ingin dijalankan : ''')

        if menuUpdate == '1' :
            Update()
        elif menuUpdate == '2':
            break

def Delete(): #4.1 function delete data
    while True:
        codeDelete = input('\n        Masukkan kode Gadget yang ingin dihapus : ')
        for i in range(len(listGadget)):
            if codeDelete == listGadget[i]['Kode Gadget']:
                print('\n        Gadget yang ingin dihapus adalah : ', listGadget[i])
                cekDelete = input('\n        Apakah yakin ingin menghapus data ini? (Y/N) : ')
                if cekDelete == 'Y':
                    del listGadget[i]
                    print('\n        "Data berhasil dihapus"') 
                    break
                elif cekDelete == 'N':
                    print('\n        "Data tidak terhapus"')
                    break
                else:
                    print('\n        "Perintah yang anda masukkan salah"')
                    break

        else:
            print('\n        "Data tidak ditemukan"')
        break

def deleteData(): #4.Fitur Delete = function menampilkan menu delete data
    while True:
        menuDelete = input('''
        1. Delete Data
        2. Kembali ke menu utama
        
        Ketik nomor menu yang ingin dijalankan : ''')

        if menuDelete == '1' :
            Delete()
        elif menuDelete == '2':
            break

def keluar(): #function untuk keluar dari aplikasi
    print(f'''
        \nSee You Next Project
        \n  ===Thankyou====''')

while True: #function menu awal
    halo()
    pilihan_menu = (input('Ketik nomor menu yang ingin dijalankan : '))
    if pilihan_menu =='1':
        readData()
    if pilihan_menu == '2':
        createData()
    if pilihan_menu == '3':
        updateData()
    if pilihan_menu =='4':
        deleteData()
    elif pilihan_menu =='5':
        keluar()
        break
    else:
        print('Pilihan yang anda masukan salah')
        continue