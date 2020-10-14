print("Perintah yang tersedia (ADD, SELESAI) \n");

books = [];

def urutkanData(data):
  totalData = len(data);

  for i in range(totalData - 1):
    for j in range(totalData - i - 1):
      if data[j]  > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j];
  return data;

while True:
  command = input("Masukan perintah! \n");
  if command == "ADD":
    judul_buku = input("masukan nama buku \n");
    books.append(judul_buku);
  elif command == "SELESAI":
    # tampilkan list buku yang sudah diurutkan
    print(urutkanData(books));
    break;  
  else:
    print("Perintah yang anda masukan tidak ada! \n");


