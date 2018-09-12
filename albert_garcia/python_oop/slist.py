class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    def Addnode(self, value):
        node = Node(value)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = node
    def PrintAllValues(self, msg=""):
        runner = self.head
        print("\n\nhead points to head")
        print("Printing the values in the list ---", msg,"---")
        while (runner.next != None):
            print("runner =", runner.value)
            runner = runner.next
        print("runner =", runner.value)
    def RemoveNode(self, value):
        runner = self.head
        if self.head.value == value:
            self.head = self.head.next
        holder = runner
        while runner.next != None:
            if runner.value == value:
                holder.next = runner.next
            holder = runner
            runner = runner.next
        if runner.value == value and runner.next == None:
            holder.next = None
        return self

list = SList(5)
list.Addnode(7)
list.Addnode(9)
list.Addnode(1)
list.PrintAllValues()
list.RemoveNode(9) .PrintAllValues("Attempt 1")