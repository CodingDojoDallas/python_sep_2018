class Node:
	def __init__(self,value):
		self.value = value
		self.next = None
		self.previous = None


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
		runner.next.previous = runner
		return self
		# print(runner.next.previous.value)

	def display_all(self):
		runner = self.head
		while runner.next != None:
			print(runner.value)
			runner = runner.next
		print(runner.value)

	def removeNode(self,value):
		runner = self.head
		if runner.value == value: #If the value is the first node
			self.head = runner.next
			runner.next.previous = None
		while runner.value != value and runner.next != None:
			runner = runner.next
		if runner.next == None:
			runner.previous.next = None
			runner.previous = None
		else:
			runner.previous.next, runner.next.previous = runner.next, runner.previous
		return self

	def insertNode(self,value,prev):
		node = Node(value)
		runner = self.head
		while runner.value != prev:
			runner = runner.next
		node.previous = runner
		node.next = runner.next
		runner.next.previous = node
		runner.next = node





list1 = SList(5)
list1.addNode(3)
list1.addNode(4)
list1.addNode(6)
list1.addNode(8)
list1.removeNode(4)
list1.insertNode(1,6)
list1.display_all()
