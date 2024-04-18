import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 5], [1, 2]])

add = a + b

sub = a - b

prod = np.dot(a, b)

div = a / b

print("加算結果:\n", add)
print("減算結果:\n", sub)
print("行列積結果:\n", prod)
print("除算結果:\n", div)