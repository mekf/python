def InsertsionSort(A):
	for j in range (1, len(A)):
		key = A[j]
		i = j - 1
		while (i >= 0) and (A[i] > key):
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key

x = input("define a list, separted by comma \n> ")
x.split(',')

print "input:"
print x

InsertsionSort(x)
print "output:"
print x