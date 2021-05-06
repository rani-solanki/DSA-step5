class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, newData):
		newNode = Node(newData)
		newNode.next = self.head
		self.head = newNode
		
	def addTwoLists(self, first, second):
		Str = " "
		str1 = " "
		for j in range(len(first) or len(second)):
			if(j<len(first)):
				Str = Str+str(first[j])
			if (j < len(second)):
				str1 = str1+str(second[j])

		num1 , num2 = int(Str), int(str1)

		sum = num1 + num2
		return sum
		
	def printList(self):
		list = []
		temp = self.head
		while(temp):
			list.append(temp.data)
			temp = temp.next
		return list

first = LinkedList()
second = LinkedList()

first.push(6)
first.push(4)
first.push(9)
array  = first.printList()

second.push(4)
second.push(8)
second.push(5)
array1 = second.printList()

res = LinkedList()
arr = res.addTwoLists(array, array1)
print(arr)
