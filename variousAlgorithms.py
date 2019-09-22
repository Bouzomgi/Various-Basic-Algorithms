
def linearSearch(lst, target):
	for index in range(len(lst)):
		if lst[index] == target:
			return index
	return -1

def recursiveBinarySearch(lst, target, startingIndex = 0):
	midpoint = len(lst)//2
	if len(lst) == 0:
		return -1
	elif lst[midpoint] == target:
		return startingIndex + midpoint
	elif target > lst[midpoint]:
		return(recursiveSearch(lst[midpoint:], target, startingIndex + midpoint))
	return(recursiveSearch(lst[:midpoint], target, startingIndex))


def binarySearch(lst, target):
	lst.sort()
	return recursiveSearch(lst,target) if recursiveSearch(lst,target) != -1 else -1

def minMaxSearch(lst):
	if not lst:
		return -1
	minimum = [lst[0], 0]; maximum = minimum[:]
	for i in range(len(lst)):
		if lst[i] < minimum[0]:
			minimum = [lst[i], i]
		if lst[i] > maximum[0]:
			maximum = [lst[i], i]
	return(f'The maximum in the list is {maximum[0]} at index {maximum[1]}\n The minimum in the list is {minimum[0]} at index {minimum[1]}')

def uniqueSearch(lst):
	uniqueSearchDict = {}
	for i in lst:
		try:
			uniqueSearchDict[i]
			return "Not unique"
		except:
			uniqueSearchDict.update({i:1})
	return("Unique")

def selectionSort(lst):
	for i in range(len(lst) - 1):
		starter = i
		for j in range(i + 1,len(lst)):
			if lst[j] < lst[starter]:
				starter = j
		lst.insert(i,lst[starter])
		lst.pop(starter + 1)
	return lst

def insertionSort(lst,targetIndex=1):
	if targetIndex == len(lst):
		return lst
	for index in range(targetIndex):
		if lst[targetIndex] < lst[index]:
			targetValue = lst.pop(targetIndex)
			lst.insert(index, targetValue)
			return insertionSort(lst, targetIndex+1)
	return insertionSort(lst, targetIndex+1)


def bubbleSort(lst, swaps = True):
	while swaps:
		swaps = False
		for i in range(len(lst)-1):
			if lst[i+1] < lst[i]:
				lst[i+1],lst[i] = lst[i],lst[i+1]
				swaps = True
	return lst

def quickSort(lst):
	if not lst:
		return []
	partition = lst.pop()
	leftBranch = [i for i in lst if i <= partition]
	rightBranch = [i for i in lst if i > partition]
	return quickSort(leftBranch) + [partition] + quickSort(rightBranch)


def merge(lst1, lst2):
	returnlst = []
	while lst1 and lst2:
		if lst1[0] < lst2[0]:
			returnlst.append(lst1.pop(0))
		else:
			returnlst.append(lst2.pop(0))
	return returnlst + lst1 + lst2

def mergeSort(lst):
	if len(lst) == 1:
		return lst
	leftBranch = mergeSort(lst[:len(lst)//2])
	rightBranch = mergeSort(lst[len(lst)//2:])
	return merge(leftBranch, rightBranch)

def findDistinct(lst):
	return len(lst) == len(set(lst))

















