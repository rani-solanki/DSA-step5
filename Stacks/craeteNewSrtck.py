def isEmpty():
	stack = []
	return stack

stack = isEmpty()

def push(stack,item):
	stack.append(item)

def pop(stack,item):
	stack.pop()

def peek(stack):
	length = len(stack)
	for i in range(1,length+1):
		print(stack[length-i])

for item in range(4):
	item = input("enter the string")
	push(stack,item)

peek(stack)
for item in range(len(stack)):
	pop(stack,item)










