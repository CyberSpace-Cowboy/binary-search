# Binary Search

#given any array (e.g. [1,2,3,6,10]) find the key element (e.g. 6)

import shutil
columns = shutil.get_terminal_size().columns 

def Binary_Search():
	
	#to get the data
	array = input("\nInput numbers seperated by commas in ascending order: ").split(",")
	array = [int(x) for x in array]
	print("\n"+ str(array).center(columns))
	target = int(input("\nInput the target number: "))
	n = len(array)


	# Iterative Implementation of the Binary Search:

	(left, right) = (0, n-1)

	while left <= right:
		mid = left + (right - left) // 2
		#if faced with stack overflow, use these:
		
		if target == array[mid]:
			return mid

		if target < array[mid]:
			right = mid - 1

		if target > array[mid]:
			left = mid + 1

	# target doesn't exist in the list
	return -1


if __name__ == '__main__':

	print("BINARY SEARCH".center(columns))
	while True:
		index = Binary_Search()

		if index != -1:
			print("\nElement found at index", index)
		else:
			print("\nThere is no such element in the array")

		ask = input("\nWanna Continue? [y/n]: ").lower()
		if ask == "y":
			continue
		elif ask == "n":
			exit()

#Recursive Implementation: (feedback the return contents back to the function till the goal is met or a certain condition is true)
"""
def Binary_Search(array, target, left, right):

	if left > right:
		return -1

	mid = (right + left) // 2
	# mid = left + (right - left) / 2
	# mid = right - (right - left) // 2

	if target == array[mid]:
		return mid

	elif target < array[mid]:
		return Binary_Search(array, target, left, mid - 1)

	elif target > array[mid]:
		return Binary_Search(array, target, mid + 1, right)

	# target doesn't exist in the list
	return -1





if __name__ == '__main__':

	print("BINARY SEARCH - RECURSION".center(columns))
	array = input("Input the numbers for the sorted array seperated by commas in ascending order: ").split(",")
	array = [int(x) for x in array]
	target = int(input("Input the target number: "))
	n = len(array)
	(left, right) = (0, n-1)
	
	index = Binary_Search(array, target, left, right)

	if index != -1:
		print("Element found at: ", index)
	else:
		print("There's such element in the array")
"""
