"""Python 3.6.0
Georgia Barnes
Appends input into a list and sorts in ascending order"""

def start():
    listA=[]
    n = int(input("How many numbers would you like to sort? "))
    for i in range(int(n)):
        x = int(input("Enter numbers(one at a time): "))
        listA.append(int(x))
    listsort(listA)
    
def listsort(listA):
    for passnum in range(len(listA)-1,0,-1):
        for i in range(passnum):
            if listA[i]>listA[i+1]:
                listA[i],listA[i+1] = listA[i+1],listA[i] 
    print (listA)
#sort(listA)

if __name__== "__main__":
    start()

