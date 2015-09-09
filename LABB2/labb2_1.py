from arrayQFile import ArrayQ
def main():
	q=ArrayQ()
	q.enqueue(1)
	q.enqueue(2)
	x= q.dequeue()
	y= q.dequeue()
	print(x,y)

if __name__ == '__main__':
	main()
