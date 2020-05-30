class LinledList():
    class Node():
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, element):
        if self.head == None:
            self.head = self.Node(element)
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next

            pointer.next = self.Node(element)

        self.count += 1
            
    def insert(self, element, index):
        pass

    def removeAt(self, index):
        pass

    def getElementAt(self, index):
        if index < 0 or index > self.count:
            return None
        else:
            pointer = self.head
            for x in range(index):
                pointer = pointer.next

            return pointer.element

    def indexOf(self, index):
        pass

    def __str__(self):
        if self.head == None:
            return '[]'
        else:
            printList = '['

            pointer = self.head
            while pointer.next != None:
                printList += f'{pointer.element}, '
                pointer = pointer.next
            
            printList += f'{pointer.element}]'

            return printList

if __name__ == "__main__":
    list = LinledList()

    for x in range(10):
        list.push(x)
    
    assert list.__str__() == f'{[x for x in range(10)]}'
    assert list.getElementAt(0) == 0
    assert list.getElementAt(4) == 4
    assert list.getElementAt(11) == None
