unordered_list = [1,7,9,10,3,3,2,1,4]

def quicksort(list_input):
	list_len = len(list_input)
	if list_len > 1:
		pivot_pos = list_len / 2
		pivot = list_input[pivot_pos]
		lower = []
		upper = []
		for i in range(list_len):
			if i != pivot_pos:
				new_list = []
				if list_input[i] < pivot:
					lower.append(list_input[i])
				else: 
					upper.append(list_input[i])
		new_list.extend(quicksort(lower))
		new_list.append(pivot)
		new_list.extend(quicksort(upper))
		return new_list
	else: 
		return list_input
	


print my_quicksort(unordered_list)