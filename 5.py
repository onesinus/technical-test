class Node:
 def __init__(self, data):
   self.data = data;
   self.next = None;

class LinkedList:
  def __init__(self):
    self.head = None;

  def tambahKapal(self, data):
    new_kapal = Node(data);
    if self.head is None:
      self.head = new_kapal;
    else:    
      last = self.head
      while last.next:
        last = last.next;
    
      last.next = new_kapal;

  def tampilkanKapal(self):
    temp = self.head;
    while temp:
      print(temp.data);
      temp = temp.next;

  def hapusKapal(self):
    print("Proses penghapusan data...");
    if self.head == None:
      return None;
    
    self.head = self.head.next;

if __name__ == '__main__':
  linkedList = LinkedList();

  while True:
    print("Perintah yang tersedia (ADD, DELETE, PRINT, SELESAI) \n");
    command = input("Masukan perintah! \n")

    if (command == "ADD"):
      nama_kapal = input("Masukan nama kapal! \n");
      linkedList.tambahKapal(nama_kapal);
    elif command == "DELETE":
      linkedList.hapusKapal();
    elif command == "PRINT":
      linkedList.tampilkanKapal();
    elif command == "SELESAI":
      linkedList.tampilkanKapal();
      break;
    else:
      print("Perintah yang anda masukan tidak ada!");
