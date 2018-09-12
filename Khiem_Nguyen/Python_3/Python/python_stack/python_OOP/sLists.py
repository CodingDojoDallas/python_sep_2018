class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node #once runner is at the last node, it points to its current last node

    def printAllValues(self, msg=""):
        runner = self.head
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))

    def removeNode(self, value):
        runner = self.head
        if self.head.value == value:
            self.head = self.head.next
        prev = runner
        while runner.next != None:
            if runner.value == value:
                prev.next = runner.next
            prev = runner
            runner = runner.next
        if runner.value == value and runner.next == None:
            prev.next = None

        # while (runner.next.value != value):
        #     runner = runner.next
        # runner.next = runner.next.next

print("\n\n\n\n===START OF THE PROGRAM===")
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(9)#middle
list.removeNode(5)#first
list.removeNode(1)#last
list.printAllValues("Attempt 1")
