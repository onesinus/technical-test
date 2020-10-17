from collections import deque

urutan_pelanggan = deque([])

no_urutanPelanggan = 0

def tampilkan_antrian (data):
    for d in data:
        print ("No. " , d["no_urut"] , " Nama: ", d["nama"])

while True:
    perintah = input("Masukkan perintah \n ketik 'Input nama' untuk menambahkan urutan, \n ketik 'now' untuk cek urutan sekarang: \n ketik 'out' atau saat pelanggan telah mendapatkan produk \n ketik 'exit' saat selesai\n")
    if perintah =="Input nama":
        no_urutanPelanggan += 1
        nama_pelanggan = input("Masukkan nama pelanggan! :")
        urutan_pelanggan.append({ "no_urut": no_urutanPelanggan, "nama": nama_pelanggan})   
    elif perintah == 'out':
        print("no urutan yang keluar:", urutan_pelanggan.popleft()) 
    elif perintah == 'now':
        print("antrian terakhir CS adalah: ", no_urutanPelanggan) 
        print("\n Total antrian: ", len(urutan_pelanggan))  
    elif perintah == 'show':
        print("daftar antrian pada CS \n")
        tampilkan_antrian(urutan_pelanggan)  
    elif perintah == 'exit':
        print("makasih pak")
        break
    else:
        print("perintah tidak ditemukan")
