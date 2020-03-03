class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        currentnode = self.head
        count = 0
        while currentnode is not None:
            count = count + 1
            currentnode = currentnode.next
        return count

    def insert(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode

    def insertatpos(self, newnode, position):
        currentpos = 0
        currentnode = self.head
        previousnode = currentnode
        currentnode = currentnode.next
        currentpos = currentpos + 1
        while currentpos == position:
            previousnode.next = newnode
            newnode.next = currentnode
            break

    def inserthead(self, newnode):
        tempnode = self.head
        self.head = newnode
        self.head.next = tempnode
        del tempnode

    def printlist(self):
        if self.head is None:
            print("the list is empty")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next


firstnode = Node(10)
LinkedList = LinkedList()
LinkedList.insert(firstnode)
secondnode = Node(20)
LinkedList.insert(secondnode)
thirdnode = Node(30)
LinkedList.insert(thirdnode)
fourthnode = Node(40)
LinkedList.insertatpos(fourthnode, 0)
LinkedList.printlist()
print(LinkedList.length())
