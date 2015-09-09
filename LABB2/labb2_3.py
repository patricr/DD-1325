from arrayQFile import ArrayQ
import timeit

#map. är en funktion som utför blblabla för varje element i listan

def main():
	string = input("skriv in tal ")
	stringList=string.split() # lägger stringnummer i en lista

	intList=[]
	for i in stringList: # gör om till intar och lägger i lista
		i = int(i)
		intList.append(i)

	q=ArrayQ() # skapar ett objekt

	for x in intList: #appendar talen till objektets array
		q.enqueue(x)

	while q.isEmpty()==False:
		firstToLast=q.dequeue() # poppar första talet
		q.enqueue(firstToLast) # lägger första talet sist i arrayn
		deal=q.dequeue() 	# printar första talet i arrayn
		print(deal, end=" ")
		# dealed.append(deal)



if __name__ == '__main__':

	main()
