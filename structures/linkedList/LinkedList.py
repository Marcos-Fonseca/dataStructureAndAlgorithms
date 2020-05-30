class LinledList():
    class Node():
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.root = None

    def push(self, element):
        if self.root == None:
            self.root = self.Node(element)
        else:
            pointer = self.root
            while pointer.next != None:
                pointer = pointer.next

            pointer.next = self.Node(element)
            
    def insert(self, element, index):
        pass

    def removeAt(self, element):
        pass

    def getElementAt(self, index):
        pass

    def indexOf(self, index):
        pass

    def __str__(self):
        if self.root == None:
            return '[]'
        else:
            printList = '['

            pointer = self.root
            while pointer.next != None:
                printList += f'{pointer.element}, '
                pointer = pointer.next
            
            printList += f'{pointer.element}]'

            return printList

if __name__ == "__main__":
    list = LinledList()

    for x in range(10):
        list.push(x)

    print(list)