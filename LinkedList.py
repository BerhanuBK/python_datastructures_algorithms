class Node:
	def __init__(self, value):
		if value != None:
			self.value = value
			self.next = None
		else:
			self.value = None
			self.next = None

class LinkedList:
	head = None

	def __init__(self, node):
		if node != None:
			self.current = node
			if self.head == None:
				self.head = self.current

	def display(self, head):
		if head != None:
			if head.next != None:
				print(head.value)
				self.display(head.next)
			else:
				print(head.value)
		else:
			print ("No node to start with")

nd1 = Node(2)
nd2 = Node(4)
nd3 = Node(6)
nd4 = Node(8)
nd5 = Node(10)

nd1.next=nd2
nd2.next=nd3
nd3.next=nd4
nd4.next=nd5
				
ll = LinkedList(None)
ll.display(nd1)

sum=0
print(ll.head)
ll.head = nd1
while ll.head != None:
	print(ll.head.value)
	sum = sum + ll.head.value
	ll.head = ll.head.next

print(f"Sum ---{sum}")			
