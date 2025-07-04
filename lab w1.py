
import numpy as np
"""
v = np.array([[3],[2]])
print(v)

print(v.shape)
print(v.ndim)

# know about vectors

# visualizing vectors
import matplotlib.pyplot as plt
plt.figure()
plt.plot([0,v[0,0]],[0,v[1,0]],'b-') # blue (v)
plt.plot([0,w[0,0]],[0,w[1,0]],'g-') # green(w)
plt.grid()
plt.axis('equal')
plt.show()"""

# understand from chatgpt
# fun with vectors and examples

#---------Matrices
# all matrices are 2d numpy arrays
A = np.array([[3,-5],[-7,11]])
print(A)
print(A.shape)
print(A.ndim)

# matrix multiplications see examples from chatgpt

# Exercises
"""
Exercise 1. Experiment with vector addition, i.e., change the components of the vectors 𝑣
and 𝑤 in the code and see if the parallelogram law of vector addition still holds.
Exercise 2. Experiment with scalar multiplication of vectors using visualisation of vectors.
What happens to a vector when multiplied by scalars of different value (positive, negative,
between 0 and 1, between -1 and 0, etc)?

Exercise 3. The negative of a matrix 𝐴 is found by replacing each component by its negative,
e.g.,
− [3 −5
−7 11] = [
−3 5
7 −11]

A = np.array([[3,-5],[7,9]])
print(A)
Now compare the following fragments of Python code and make a conclusion.
B = -A
print(B)
C = (-1)*A
print(C)
Also, what do you notice about 𝐴 + (−𝐴)? Experiment with different values for the
components of the matrix 𝐴.

Exercise 4. Consider a matrix 𝐴. The transpose of a matrix is a new matrix 𝐵 found by
writing the rows of 𝐴 as the columns of 𝐵 in the same order. The transpose of matrix A is
written as 𝐴
𝑇
.
A = np.array([[3,-5],[7,9]])
print(A)
B = A.T # .T is transpose in numpy
print(B)

Exercise 5. Experiment with matrix addition. Make up your own examples and check these
by hand.

Exercise 6. Experiment with scalar multiplication of matrices. Make up your own examples
and check these by hand.

Group Challenge. Adapt the Python code given for the Quadratic Bezier curve to implement
a Cubic Bezier curve. There should be two endpoints and two control points. The formula
is given on the Wikipedia page below.

"""