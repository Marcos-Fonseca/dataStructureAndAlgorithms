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
        if index == 0:
            newNode = self.Node(element)
            newNode.next = self.head
            self.head = newNode
            self.count += 1

        elif index > 0 and index <= self.count:
            pointer = self.head

            for x in range(index-1):
                pointer = pointer.next

            newNode = self.Node(element)
            newNode.next = pointer.next
            pointer.next = newNode
            self.count += 1
            
    def removeAt(self, index):
        if index >= 0 and index < self.count:
            if index == 0:
                pointer = self.head.next
                del(self.head)
                self.head = pointer
            
            else:
                pointer = self.head
                for x in range(index+1):
                    if x == index-1:
                        removeNode = pointer.next
                        pointer.next = pointer.next.next
                        del(removeNode)
                    else:
                        pointer = pointer.next

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
    list1 = LinledList()
    for x in range(10):
        list1.push(x)

    list2 = LinledList()
    list2.push(0)

    assert list1.__str__() == f'{[x for x in range(10)]}'
    assert list2.__str__() == '[0]'
    assert list1.getElementAt(0) == 0
    assert list1.getElementAt(4) == 4
    assert list1.getElementAt(11) == None

    list1.insert(18, 0)
    assert list1.__str__() == '[18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'

    list2.insert(18, 0)
    assert list2.__str__() == '[18, 0]'
    list2.insert(17, 2)
    assert list2.__str__() == '[18, 0, 17]'

    list2.removeAt(1)
    assert list2.__str__() == '[18, 17]'
    list2.removeAt(0)
    assert list2.__str__() == '[17]'