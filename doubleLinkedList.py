class Node:

    def __init__(
        self,
        next=None,
        prev=None,
        data=None,
        ):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def AddFirst(self, data):
        new_meeting = Node(data = data)
        new_meeting.next = self.head
        new_meeting.prev = None

        if self.head is not None:
            self.head.prev = new_meeting

        self.head = new_meeting
    
    def AddLast(self, data):
        new_meeting = Node(data = data)
        new_meeting.next = None
	
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_meeting
        new_meeting.prev = node
	
    # def AddByKey():
    # def DeleteFirst():
    # def DeleteLast():
    # def DeleteByKey():

    def Show(self, node):
        while node is not None:
            print (' % s' % node.data),
            node = node.next

#   def hapusmeeting(self):

if __name__ == '__main__':

    linkedList = LinkedList()

    while True:
        print ('Perintah yang tersedia (ADD_FIRST, ADD_LAST, DELETE, PRINT, SELESAI) \n')

        command = input('Masukan perintah! \n')

        if command == 'ADD_FIRST':
            nama_meeting = input('Masukan nama meeting! \n')
            linkedList.AddFirst(nama_meeting)
        elif command == 'ADD_LAST':
            nama_meeting = input('Masukan nama meeting! \n')
            linkedList.AddLast(nama_meeting)
        elif command == 'DELETE':
            linkedList.hapusmeeting()
        elif command == 'PRINT':
            linkedList.Show(linkedList.head)
        elif command == 'SELESAI':
            linkedList.Show(linkedList.head)
            break
        else:
            print ('Perintah yang anda masukan tidak ada!')
