import numpy as np
list1 = np.random.random_integers(1, 20, 20)
print(list1)
array1 = list1.reshape((4, 5))
print(array1)
res = np.argmax(array1, axis=1)
array1[0][res[0]] = 0
array1[1][res[1]] = 0
array1[2][res[2]] = 0
array1[3][res[3]] = 0
print(array1)

