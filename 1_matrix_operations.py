import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 5], [1, 2]])

add = a + b

sub = a - b
mult = a * b

# Matrix product
prod = np.dot(a, b)

# Element-wise division (be cautious with division by zero)
div = a / b

print("addition result:\n", add)
print("Subtraction result:\n", sub)
print("Element-wise multiplication result:\n", mult)
print("Matrix product result:\n", prod)
print("Element-wise division result:\n", div)