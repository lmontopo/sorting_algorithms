

def mergesort(alist):
	"sorts the inputed list"
	if len(alist) > 1:
		
		left, right = split(alist)
		left = mergesort(left)
		right = mergesort(right)
		result = merge(left, right)
		return result
	else:
		return alist
	
def merge(left, right):
	temp = []
	while len(left) > 0 and len(right) > 0:
		item1 = left[0]
		item2 = right[0]
		temp.append(min(item1, item2))
		if min(item1, item2) == item1 :
			left = left[1:]
		elif min(item1, item2) == item2:
			right = right[1:]
	temp.extend(left)
	temp.extend(right)
	return temp

def split(alist):
	"splits the list into two equal sized lists"
	split_pos = len(alist) / 2 
	return alist[0: split_pos], alist[split_pos:]



alist = [103, 9, 7, 20, 12, 3, 66, 24]
print mergesort(alist)
