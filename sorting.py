def InsertsionSort(A):
	for j in range (1, len(A)):
		key = A[j]
		i = j - 1
		while (i >= 0) and (A[i] > key):
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key

x = raw_input("define a list?, separted by comma \n> ")
x = x.split(',')

print "input:"
print x
# print "converted input:"
# print y

InsertsionSort(x)
print "output:"
print x