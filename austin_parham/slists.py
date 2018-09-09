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
		runner1 = self.head
		runner2 = runner1.next
		if runner1.value == value:
			self.head = runner2

		else:
			while runner2.value != value and runner2.next != None:
				runner1 = runner1.next
				runner2 = runner2.next
			if runner2.next == None:
				runner1.next = None
			else:
				runner1.next = runner2.next


		

list1 = SList(5)
list1.addNode(4)
list1.addNode(6)
list1.addNode(8)
list1.removeNode(8)

list1.display_all()
