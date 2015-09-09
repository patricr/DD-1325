from array import array

class ArrayQ(object):

	def __init__(self):
		#self.top= None
		#self._quelist=_quelist)
		self.__quelist=array('i',[])

	def enqueue(self,x):
		# self.top=self.quelist
		return self.__quelist.append(x)

	def dequeue(self):
		return self.__quelist.pop(0)

	def isEmpty(self):
		if self.__quelist==None:
			return True
		elif len(self.__quelist)==0:
			return True
		else:
			return False
