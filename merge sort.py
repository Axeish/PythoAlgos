import operator
def merge(left,right):
	if not len(left) or not len(right):
		return Left or right
	result = []
	i,j = 0,0
        while (len(result) < len(left) + len(right)):
		if left[i] <right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
		if i== len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break
	return result
def merge_sort(a):
    	#mergesort(a,0,len(a)-1)
    	if len(a) < 2:
		return a
	mid= len(a)/2
        left = merge_sort(a[:mid])
	right = merge_sort(a[mid:])
	return merge(left, right)

n = int(raw_input())
arr = map(int,raw_input().strip().split())


print arr
assd = merge_sort(arr)
print assd
