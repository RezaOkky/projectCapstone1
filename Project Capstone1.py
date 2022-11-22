################################ PROJECT CAPSTONE MODUL 1 : YELLOW PAGES (DATA KONTAK TELEPON) ########################################


## DATABASE ## 
daftarKontak = [
    {
        'No ID' : '101',
        'Nama' : 'RSUD ABC',
        'Email' : 'rsud_abc@gmail.com',
        'No Telepon' : '089237582900',
        'Alamat' : 'Jln Jend.A.Yani no.12'
    },
    {
        'No ID' : '102',
        'Nama' : 'Polsek ABC',
        'Email' : 'polsekabc@gmail.com',
        'No Telepon' : '083957295787',
        'Alamat' : 'Jln Jend.Sudirman no.120'
    },
    {
        'No ID' : '103',
        'Nama' : 'DAMKAR ABC',
        'Email' : 'damkar_abc@gmail.com',
        'No Telepon' : '089385736347',
        'Alamat' : 'Jln Pemuda no.93'
    }
]

#Template Database
def database (listData) :
    print('\n\t\t============= Data Kontak Telepon =============\n')
    print('No ID\t| Nama   \t| Email     \t\t\t| No Telepon\t| Alamat ')
    for i in range (len(listData)) :
        print('{}\t| {}  \t| {}     \t| {}\t| {}'.format(listData[i]['No ID'], listData[i]['Nama'], listData[i]['Email'], 
        listData[i]['No Telepon'], listData[i]['Alamat']))

# Fungsi filter dictionary 
def searchList (Input) :
    searchList = (list(filter(lambda data: data['No ID'] == str(Input), daftarKontak)))
    return searchList

#Template Database Update
def databaseUpdate (listData, x, newData) :
    print('\n\t\t============= Data Kontak Telepon =============\n')
    print('No ID\t| Nama   \t| Email     \t\t\t| No Telepon\t| Alamat ')
    if x == 1 : 
        for i in range (len(listData)) :
            print('{}\t| {}  \t| {}     \t| {}\t| {}'.format(newData, listData[i]['Nama'], listData[i]['Email'], 
            listData[i]['No Telepon'], listData[i]['Alamat']))
    elif x == 2 :
        for i in range (len(listData)) :
            print('{}\t| {}  \t| {}     \t| {}\t| {}'.format(listData[i]['No ID'], newData, listData[i]['Email'], 
            listData[i]['No Telepon'], listData[i]['Alamat']))
    elif x == 3 :
        for i in range (len(listData)) :
            print('{}\t| {}  \t| {}     \t| {}\t| {}'.format(listData[i]['No ID'], listData[i]['Nama'], newData, 
            listData[i]['No Telepon'], listData[i]['Alamat']))
    elif x ==  4 :
        for i in range (len(listData)) :
            print('{}\t| {}  \t| {}     \t| {}\t| {}'.format(listData[i]['No ID'], listData[i]['Nama'], listData[i]['Email'], 
            newData, listData[i]['Alamat']))
    elif x == 5 :
        for i in range (len(listData)) :
            print('{}\t| {}  \t| {}     \t| {}\t| {}'.format(listData[i]['No ID'], listData[i]['Nama'], listData[i]['Email'], 
            listData[i]['No Telepon'], newData))
    else :
        print('Data tidak ditemukan')

# Fungsi Update Kontak
def updateKontak(Data, Kolom, NewData) :
    inputUpdateKontak = (input('Apakah data yang diupdate sudah benar ? (Ya/Tidak) : ')).lower()
    if inputUpdateKontak == 'ya' :
        Data[0][Kolom] = NewData
        print ('\tData sudah diperbaharui' )
    else :
        print ('\t Data tidak terupdate')



###### Function Utama ######

# Fungsi READ ()
def tampilkan_kontak() :
    menuBaca = int(input('''
    Menu Daftar Kontak Telepon :

        1. Menampilkan Data Kontak
        2. Kembali ke Menu Utama

    Masukkan angka menu yang ingin dijalankan = '''
    ))
    if menuBaca == 1 :
        database(daftarKontak)
    elif menuBaca == 2 :
        menu()
    tampilkan_kontak()


# Fungsi ADD()
def tambah_kontak () :
    menuAdd = int(input('''
    Menu Tambah Daftar Kontak Telepon :

        1. Menambah Kontak
        2. Kembali ke Menu Utama

    Masukkan angka menu yang ingin dijalankan = '''
    ))
    if menuAdd == 1:
        add_id = (input('\n\tMasukkan No ID yang baru = '))
        listValue = [value for dataKontak in daftarKontak for value in dataKontak.values()]
        if add_id in listValue :
            print('\n\tData sudah ada')
            return tambah_kontak()
        else :
            nama = input('\tMasukkan Nama = ')
            email = input('\tMasukkan Email = ')
            telepon = input('\tMasukkan No Telepon = ')
            alamat = input('\tMasukkan Alamat = ')
            kontak_baru = [{
                'No ID' : add_id,
                'Nama' : nama,
                'Email' : email,
                'No Telepon' : telepon,
                'Alamat' : alamat
            }]
            database(kontak_baru)
            Save = (input('\n\t Simpan Data ? (Ya/Tidak)= ')).lower()
            if Save == 'ya':
                daftarKontak.extend(kontak_baru)
                database(daftarKontak)
                print('\n \tData Berhasil Ditambahkan')
            else :
                print('\n \tData Tidak Tersimpan')
    elif menuAdd == 2 :
        menu()  
    tambah_kontak ()      
    
# FUNGSI UPDATE()
def update_kontak() :
    menuUpdt = int(input('''
    Menu Update Daftar Kontak Telepon :

        1. Mengupdate Kontak
        2. Kembali ke Menu Utama

    Masukkan angka menu yang ingin dijalankan = '''
    ))
    if menuUpdt == 1:
        database(daftarKontak)
        gantiKontak = input('\nMasukkan No ID yang ingin diubah = ')
        listValue2 = [value for dataKontak in daftarKontak for value in dataKontak.values()]
        if gantiKontak in listValue2 :
            searchList(gantiKontak)
            database(searchList(gantiKontak))
            input1 = input('\nUpdate data berikut ? (Ya/Tidak)= ').lower()
            if input1 == 'ya':
                kategori = int(input('''
                Kategori Kolom Database Kontak :
                    1. No ID
                    2. Nama
                    3. Email
                    4. Telepon
                    5. Alamat
                Masukkan no kategori yang akan diubah = '''
                ))
                if kategori == 1 :
                    dataBaru = input('\nMasukkan data baru = ')
                    databaseUpdate(searchList(gantiKontak),1,dataBaru)
                    updateKontak(searchList(gantiKontak),'No ID',dataBaru)
                elif kategori == 2 :
                    dataBaru = input('\nMasukkan data baru = ')
                    databaseUpdate(searchList(gantiKontak),2,dataBaru)
                    updateKontak(searchList(gantiKontak),'Nama',dataBaru)
                elif kategori == 3 :
                    dataBaru = input('\nMasukkan data baru = ')
                    databaseUpdate(searchList(gantiKontak),3,dataBaru)
                    updateKontak(searchList(gantiKontak),'Email',dataBaru)
                elif kategori == 4 :
                    dataBaru = input('\nMasukkan data baru = ')
                    databaseUpdate(searchList(gantiKontak),4,dataBaru)
                    updateKontak(searchList(gantiKontak),'Telepon',dataBaru)
                elif kategori == 5 :
                    dataBaru = input('\nMasukkan data baru = ')
                    databaseUpdate(searchList(gantiKontak),5,dataBaru)
                    updateKontak(searchList(gantiKontak),'Alamat',dataBaru)
                else :
                    print('\tKategori tidak tersedia')
            else :
                print('\nData tidak terupdate')        
        else :
            print('\n\tData tidak ada')
    elif menuUpdt == 2 : 
        menu() 
    update_kontak()  


# FUNGSI DEL()
def hapus_kontak() :
    menuDel = int(input('''
    Menu Hapus Daftar Kontak Telepon :

        1. Menghapus Kontak
        2. Kembali ke Menu Utama

    Masukkan angka menu yang ingin dijalankan = '''
    ))
    if menuDel == 1:
        database(daftarKontak)
        indexNama = input('\nMasukkan No ID di daftar kontak yang akan dihapus = ')
        listValue3 = [value for dataKontak in daftarKontak for value in dataKontak.values()]
        if indexNama in listValue3 :
            searchList(indexNama)
            database(searchList(indexNama))
            input1 = input('\nHapus data berikut ? (Ya/Tidak)= ').lower()
            if input1 == 'ya':
                for i  in searchList(indexNama) :
                    daftarKontak.remove(i)
                print('\n\t Data Kontak Berhasil Dihapus')
            else:
                print('\n\t Data Kontak Tidak Dihapus')
        else :
            print ('\nData tidak ditemukan')
    elif menuDel == 2:
        menu()
    hapus_kontak()


# FUNGSI FIND()
def cari_kontak() :
    menuFind = int(input('''
    Menu Cari Daftar Kontak Telepon :

        1. Mencari Kontak
        2. Kembali ke Menu Utama

    Masukkan angka menu yang ingin dijalankan = '''
    ))
    if menuFind == 1 :
        id_dicari = input('Masukkan No ID yang dicari = ')
        searchList(id_dicari)
        if len(searchList(id_dicari)):
            database(searchList(id_dicari))
        else :
            print('\nData Yang Dicari Tidak Ada')
    elif menuFind == 2 :
        menu()
    cari_kontak()

# Menu Utama
def menu() :
    while True :
        print('''
            Selamat Datang di Daftar Kontak Telepon 


            List Menu :
            1. Daftar Kontak
            2. Cari Kontak
            3. Tambah Kontak
            4. Update Kontak
            5. Hapus Kontak
            6. Keluar Program
            '''
            )
        Menu = input('Pilih menu = ')
        if Menu == '6' :
            print('Terima Kasih, Sampai Jumpa')
            exit()
        elif Menu == '1' :
            tampilkan_kontak()
        elif Menu =='2' :
            cari_kontak()
        elif Menu == '3' :
            tambah_kontak()
        elif Menu == '4' :
            update_kontak()
        elif Menu == '5' :
            hapus_kontak()     
        else :
            print('Menu tidak tersedia')
        
menu()
