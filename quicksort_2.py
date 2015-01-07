def quicksort(list_input):
	quicksort_recursive(list_input, 0, len(list_input) - 1)


def quicksort_recursive(list_input, first, last):
	if first < last: 
		splitpoint = partition(list_input, first, last)
		quicksort_recursive(list_input, first, splitpoint - 1)
		quicksort_recursive(list_input, splitpoint + 1, last)
	else: 
		return

def partition(list_input, first, last):

	pivot = list_input[first]

	left_mark = first + 1
	right_mark = last 

	done = False
	while not done:

		while left_mark <= right_mark and \
				list_input[left_mark] <= pivot:
			left_mark = left_mark + 1

		while list_input[right_mark] >= pivot and \
				right_mark >= left_mark:
			right_mark = right_mark - 1

		if right_mark < left_mark:
			done = True
		else: 
			temp = list_input[left_mark]
			list_input[left_mark] = list_input[right_mark]
			list_input[right_mark] = temp

	temp = list_input[first]
	list_input[first] = list_input[right_mark]
	list_input[right_mark] = temp

	return right_mark


if __name__ == "__main__":
	alist = [54, 36, 5, 4, 23]
	quicksort(alist)
	print alist