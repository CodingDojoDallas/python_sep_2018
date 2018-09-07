class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class SList:
	def __init__(self,value):
		node = Node(value)
		self.head = node

	def addNode(self,value):
		node = Node(value)
		runner = self.head
		while runner.next != None:
			runner = runner.next
		runner.next = node

	def display_all(self):
		runner = self.head
		while runner.next != None:
			print(runner.value)
			runner = runner.next
		print(runner.value)

	def removeNode(self,value):
		runner = self.head
		while runner != value and runner.next == None:
			runner = runner.next
		remove(runner)

list1 = SList(5)
list1.addNode(4)
list1.addNode(6)
list1.addNode(8)
list1.removeNode(6)

list1.display_all()
