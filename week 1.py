# why vectors and matrices 
"""
Artificial intelligence
computer graphics
computer games
data science 
robotics 
machine learning
optimisation

"""
"""
A vector has both magnitude and direction ex- force momentum velocity acceleration
A scalar has only magnitude(its just a single number) ex- mass, time, temp, distance, speed
1. Cartisian cordinate system 
2.distance between points
3. Linear algeabra
4.square matrix 
5.scalar multiplication
"""
# numpy arrays 1d vs 2d
import numpy as np;
height=np.array([12,13,14])
print(height)
print(height.ndim) 
# we call this a "1D numpy array"

a=np.array([[4],[3]])
print(a)
# vectors in mathematics MUST be 2D
# numpy arrays in numpy
# all vectors are 1 column

# 4. Matrices in Python
A = np.array([[1,-2],
              [3, 4]])
print(A)
B = np.array([[ 5,6],
              [-7,8]])
print(B)


print(A@B) # @ is matrix multiplication
#            (NOT *) 

print(0.001)
print(2**64)
print(0.001 == 1-0.999)
print(np.isclose(0.001,1-0.999))
print(np.isclose(A,B))
print(np.allclose(A,B))



