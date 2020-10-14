fifo = ();

def append(data):
  global fifo;
  fifo = (data, fifo);

def pop():
  global fifo
  ret, fifo = fifo;
  return ret

while True:
  try:
    command = input("Masukan perintah: \n");

    if command == "ADD":
      nama_kapal = input("Masukan nama kapal bongkar muat: \n");
      append(nama_kapal);
    elif command == "DELETE":
      # nama_kapal = input("Masukan nama kapal selesai: \n");
      pop();
    elif command == "SELESAI":
      print(fifo)
      break;
    else:
      print("Perintah tidak diketahui \n");
  except Exception as e:
    print(e);
