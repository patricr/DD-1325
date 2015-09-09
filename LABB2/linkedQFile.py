class Node(object):
	"""skapar en Node, med två privata attribut"""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	# def setNext(self, newNode):
	# 	self.next = newNode
	#
	# def getNext():
	# 	return self.next
	#
	# def setValue(newNode):
	# 	self.value = newNode
	#
	# def getValue():
	# 	return self.value

class LinkedQ(object):
	"""docstring for LinkedQ"""
	def __init__(self):
		self.first = None
		self.last=None

	def enqueue(self,x):
		"""skapar en nod och stoppar in sist i kön,
		sätter båda attrtibuten till att peka på newNode"""
		newNode=Node(x)
		if self.first==None:
			# om det är tomt i kön och vi vill
			# flytta pekaren "first" till att peka på newNode
			# och sätta pekaren "last" på newNode
			self.first = newNode
			self.last = newNode

		else:
			# när det finns objekt i kön ska self.last.next peka på
			#den nya noden som läggs till. för att peka bakåt
			# därefter måste vi flytta last-pekaren till att peka på nya objektet

			self.last.next = newNode
			self.last=newNode


	def dequeue(self):
		"""plockar ut det som står först i kön"""
		if self.first==None:
			return "tom kö"

		else:
			# value=newNode.getValue()
			# self.first=value
			# self.first=newNode.getNext()
			# return value

			x=self.first.value
			self.first=self.first.next
			return x

	def isEmpty(self):
		"""Returnerar True om tom, False annars"""
		if self.first==None:
			return True
		else:
			return False
	# def __str__(self):
	# 	return self.first + self.last
