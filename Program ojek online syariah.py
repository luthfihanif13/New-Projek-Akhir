#Program Ojekonline syariah

def login():
  print('login Pejuang PA')
  while True:
    username = input('username : ')
    passw = input('password : ')
    if username == 'Luthfi' and passw == '082' or username == 'Adit' and passw == 'unsend' or username == 'puput' and passw == 'sibukmc' :
        print('---------------------------------')
        print('-------Ojek Online Syariah-------')
        print('--Membantu Antum dalam Berpergian--')
        print('------Aman,Nyaman,Terpercaya------')
        print('---------------------------------')
        break
    else:
        print('silahkan antum memasukkan password/username dengan benar!')
        continue  

def motor():
    pilihan = input('motor')
    motor[pilihan]

def mobil():
    pilihan = input('mobil')
    mobil[pilihan]


def kendaraan():
  while True:
    print('kendaraan')
    print('1. Motor\n2. Mobil')
    pilihan = input('masukan pilihan: ')
    if pilihan == '1':
        motor()
        print('\nAntum memilih motor')
        input()
    elif pilihan == '2':
        mobil()
        print('\nAntum memilih mobil')
        input()
        break


  
penjemputan = {
  'lokasi': ['Sentosa', 'Gajah Mada', 'Pramuka', 'Perjuangan', 'Bengkuring', 'Palaran', 'Juanda', 'Cendana', 'Alaya', 'Lempake', 'Remaja', 'Pahlawan', 'Makroman', 'Kebaktian', 'Awang Long', 'Pemuda',]
}

tujuan = {
  'lokasi': ['Sentosa', 'Gajah Mada', 'Pramuka', 'Perjuangan', 'Bengkuring', 'Palaran', 'Juanda', 'Cendana', 'Alaya', 'Lempake', 'Remaja', 'Pahlawan', 'Makroman', 'Kebaktian', 'Awang Long', 'Pemuda',]
}

if penjemputan.upper == 'Sentosa' and tujuan == 'Alaya' or penjemputan == 'Alaya' and tujuan == 'Sentosa':
  print('Jarak = 1km')
elif penjemputan.upper == 'Pramuka' and tujuan == 'Palaran' or penjemputan == 'Palaran' and tujuan == 'Pramuka':
  print('jarak = 17km')
elif penjemputan.upper == 'Bengkuring' and tujuan == 'Cendana' or penjemputan == 'Cendana' and tujuan == 'Bengkuring':
  print('jarak = 9km')
elif penjemputan.upper == 'Remaja' and tujuan == 'Perjuangan' or penjemputan == 'Perjuangan' and tujuan == 'Remaja':
  print('jarak = 2km')
elif penjemputan.upper == 'Kebaktian' and tujuan == 'Pahlawan' or penjemputan == 'Pahlawan' and tujuan == 'Kebaktian':
  print('jarak = 3km')
elif penjemputan.upper == 'Gajah Mada' and tujuan == 'Pemuda' or penjemputan == 'Pemuda' and tujuan == 'Gajah Mada':
  print('jarak = 8km')
elif penjemputan.upper == 'Lempake' and tujuan == 'Awang Long' or penjemputan == 'Awang Long' and tujuan == 'Lempake':
  print('jarak = 15km')
elif penjemputan.upper == 'Juanda' and tujuan == 'Makroman' or penjemputan == 'Makroman' and tujuan == 'Juanda':
  print('jarak = 20km')
else:
  print('Silahkan memilih dengan benar')


def list_jalanan_penjemputan():
    penjemputan
    for key, value in penjemputan.items():
      print(key, value)


def tambah():
    input_baru = input('masukan nama jalan: ')
    penjemputan[input_baru]

def update():
    input_baru = input('update nama jalan: ')
    penjemputan[input_baru]

def hapus():
    del penjemputan [input('menghapus jalan: ')]


def list_jalanan_tujuan():
    tujuan
    for key, value in tujuan.items():
      print(key, value)


def tambah_tujuan():
    input_baru = input('masukan nama jalan: ')
    tujuan[input_baru]

def update_tujuan():
    input_baru = input('update nama jalan: ')
    tujuan[input_baru]

def hapus_tujuan():
    del tujuan [input('menghapus jalan: ')]


def main_menu():
    while True:
        print('menu')
        print('==============')
        print('1. List jalanan')
        print('2. Menambahkan lokasi penjemputan')
        print('3. Mengupdate lokasi penjemputan')
        print('4. Menghapus lokasi penjemputan')
        print('5. Menambahkan lokasi tujuan')
        print('6. Mengupdate lokasi tujuan')
        print('7. Menghapus lokasi tujaun')
        print('8. Keluar dari program ')
        pilih = input('Masukan pilihan: ')
        if pilih == '1':
            list_jalanan_penjemputan()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '2':
            tambah()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '3':
            update()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '4':
            hapus()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '5':
            tambah_tujuan()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '6':
            update_tujuan()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '7':
            hapus_tujuan()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '8':
            print('Antum telah keluar')
            break
        
def ikhwan():
    pilihan = input('Ikhwan')
    ikhwan[pilihan]

def akhwat():
    pilihan = input('Akhwat')
    akhwat[pilihan]

def driver():
  while True:
    print('kendaraan')
    print('1. Ikhwan\n2. Akhwat')
    pilihan = input('masukan pilihan: ')
    if pilihan == '1':
        ikhwan()
        print('\nAntum memilih pengemudi Ikhwan')
        input()
    elif pilihan == '2':
        akhwat()
        print('\nAntum memilih pengemudi Akhwat')
        input()
        break

harga_km_motor = 5000
harga_km_mobil = 12000
harga = 0
jarak =[]

def gopay():
    pilihan = input('Gopay')
    gopay[pilihan]

def tunai():
    pilihan = input('Tunai')
    tunai[pilihan]


if kendaraan == motor:
  total = jarak * harga_km_motor 
else:
  total = jarak * harga_km_mobil
def pembayaran():
  while True:
      print('mau bayar pakai apa: ')
      print('1. Gopay\n2. Tunai')
      pilihan = input('masukan pilihan: ')
      if pilihan == '1':
        gopay()
        print('\nAntum memilih membayar dengan gopay')
        input()
      elif pilihan == '2':
        tunai()
        print('\nAntum memilih membayar dengan tunai')
        input()
        break

  while True:
    bayar=int(input('jumlah nominal uang = Rp '))
    if total <= bayar:
      kembalian = (bayar-total)
      print('Uang kembalian = ', 'Rp',kembalian)
      break
    else:
      print('Afwan uang antum kurang')

while True:
  login()
  print('Menu')
  print('1. Pilih kendaraan')
  print('2. Penjemputan')
  print('3. Tujuan' )
  print('4. Pemilihan driver')
  print('5. Pembayaran')
  print('6. exit')
  a = input('masukkan pilihan : ')
  if a == '1' :
    main_menu ()
  elif a == '2' :
    list_jalanan_penjemputan ()
  elif a == '3' :
    list_jalanan_tujuan ()
  elif a == '4' :
    driver ()
  elif a == '5' :
    pembayaran ()
  elif a == '6' :
    print('Antum telah logout')
    print('Jazakallah khair telah menggunakan program kami')
    break


