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

    def DeleteFirst(self):
        if self.head is not None:
            self.head = self.head.next
    
    def AddLast(self, data):
        new_meeting = Node(data = data)
        new_meeting.next = None
	
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_meeting
        new_meeting.prev = node

    def DeleteLast(self):	
        node = self.head
        while node.next is not None:
            node = node.next

        node.prev.next = None

	
    # def AddByKey():
    # def DeleteByKey():

    def Show(self, node):
        while node is not None:
            print (' % s' % node.data),
            node = node.next

if __name__ == '__main__':

    linkedList = LinkedList()

    while True:
        print ('Perintah yang tersedia (ADD_FIRST, ADD_LAST, ADD_BY_KEY, DELETE_FIRST, DELETE_LAST, DELETE_BY_KEY, PRINT, SELESAI) \n')

        command = input('Masukan perintah! \n')

        if command == 'ADD_FIRST':
            nama_meeting = input('Masukan nama meeting! \n')
            linkedList.AddFirst(nama_meeting)
        elif command == 'ADD_LAST':
            nama_meeting = input('Masukan nama meeting! \n')
            linkedList.AddLast(nama_meeting)
        elif command == 'DELETE_FIRST':
            linkedList.DeleteFirst()
        elif command == 'DELETE_LAST':
            linkedList.DeleteLast()
        elif command == 'PRINT':
            linkedList.Show(linkedList.head)
        elif command == 'SELESAI':
            linkedList.Show(linkedList.head)
            break
        else:
            print ('Perintah yang anda masukan tidak ada!')
