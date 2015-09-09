from tildalabb1class import*
import timeit


def fileReader():
	with open('geodataSW.txt', encoding="utf8") as indata:
		 # öppnar behöver då inte skriva close
		in_list= [row.strip() for row in indata] #listkomprehension
		objectList=[Location(in_list[x],in_list[x+1],in_list[x+2], in_list[x+3],in_list[x+4]) for x in range(6,len(in_list)-4,6)]
		#skapar onjektet från textfilen. startar på rad 6. slutar på sista raden (len()-4). hoppar 6 steg
	return objectList

def main():
	objectList=fileReader()
	chosenLocation= input("select name:")
	for x in range(0,len(objectList)):
		if chosenLocation==objectList[x].name:
			print(objectList[x])


if __name__ =='__main__':

	main()

# in_list=[]
		# for row in indata:
		# 	in_list.append(row.strip())
# objectList=[]
	# for x in range(6,len(in_list)-4,6):
	# 	objectList.append(Location(in_list[x],in_list[x+1],in_list[x+2], in_list[x+3],in_list[x+4]))
