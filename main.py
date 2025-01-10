# add quicksort algo

# add insert sort algo

##BOOYA, are you cyborg??

###Lets do it


def insert_sort_version1(arr):

	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]
	return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

print(quicksort([3,6,8,10,1,2,1])) # [1, 1, 2, 3, 6, 8, 10]
