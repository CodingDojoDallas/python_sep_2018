class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self,value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node

    def removeNode(self, value):
        runner = self.head
        if runner.value == value:
            runner = runner.next
            self.head = runner
        prevrunner = runner
        while runner.next != None:
            if runner.value == value:
                prevrunner.next = runner.next
            prevrunner = runner
            runner=runner.next
        if runner.value == value and runner.next == None:
            prevrunner.next = None

    def insertNode(self, value, index):
        count = 0
        runner = self.head
        if index == 0:
            self.head = Node(value)
            self.head.next = runner
        prevrunner = runner
        while runner.next!= None:
            if count == index:
                prevrunner.next = Node(value)
                prevrunner.next.next = runner
            count += 1
            prevrunner = runner
            runner = runner.next

    def displayList(self):
        runner = self.head
        while runner.next != None:
            print(runner.value)
            runner = runner.next
        print(runner.value)

list = Slist(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.displayList()