import operator

def ins_sort(a,op):
    for j in range(1,len(a)):
        key = a[j]
        print key
	i=j-1
	while i>=0 and op(a[i],key):
		a[i+1] = a[i]
		i=i-1
  	a[i+1]=key
    return a


n = int(raw_input())
arr = map(int,raw_input().strip().split())


print arr
assd = ins_sort(arr,operator.gt)
print arr
