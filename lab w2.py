"""
Exercises
When comparing matrices, please use np.isclose() or np.allclose() in your answers in
an appropriate way.
Exercise 1. What kind of matrix (diagonal, upper triangular, lower triangular, symmetric,
skew-symmetric, orthogonal) is each of the matrices below? If you are not sure, you can
use Python to check. For √3 you can use np.sqrt(3).
𝐴 = [
1 2 3
0 4 5
0 0 6
] 𝐵 = [
7 8 9
8 10 11
9 11 12
] 𝐶 = [
13 0 0
0 14 0
0 0 15
] 𝐷 = [
1
√3
1
√6
1
√2
−
1
√3
2
√6
0
1
√3
1
√6
−
1
√2
]
𝐸 = [
16 0 0
17 18 0
19 20 21
] 𝐹 = [
0 22 23
−22 0 24
−23 −24 0
]
7144CEM Data Science Python Labs (2024/25 Semester 2)
17
Exercise 2.
(a) Give an example of a 2 × 2 matrix 𝑀 that is an orthogonal matrix and includes some
numbers other than just 0, −1 and 1. Write Python code to enter your matrix 𝑀 as a
numpy array and print out 𝑀. Hint: use a google search to find a suitable matrix.
(b) Consider the two columns of your matrix 𝑀 from part (a) as vectors, say vector 𝒂 and
vector 𝒃. Use numpy to calculate the vector dot products 𝒂 ∙ 𝒂, 𝒃 ∙ 𝒃, and 𝒂 ∙ 𝒃. What
conclusions can you make about vectors 𝒂 and 𝒃?
(c) Choose any 2 × 1 vectors 𝒄 and 𝒅 . Now consider the matrix transformation
represented by your matrix 𝑀 from part (a). Use matplotlib to visualise vector 𝒄,
vector 𝒅, vector 𝑀𝒄 and vector 𝑀𝒅.
• What do you suspect about the magnitude of vectors 𝒄 and 𝑀𝒄?
• What do you suspect about the magnitude of vectors 𝒅 and 𝑀𝒅?
• What do you suspect about the angle between vectors 𝒄 and 𝒅 in comparison to
the angle between vectors 𝑀𝒄 and 𝑀𝒅?
(d) Using the same vectors from part (c), use numpy to calculate 𝒄 ∙ 𝒄 and compare to
(𝑀𝒄) ∙ (𝑀𝒄) . Calculate 𝒅 ∙ 𝒅 and compare to (𝑀𝒅) ∙ (𝑀𝒅) . Calculate 𝒄 ∙ 𝒅 and
compare to (𝑀𝒄) ∙ (𝑀𝒅). Explain how these calculations confirm your suspicions
from part (c).
Exercise 3. An 𝑛 × 𝑛 matrix 𝑀 is diagonalisable if there is a particular 𝑛 × 𝑛 matrix 𝑃 and a
particular diagonal matrix 𝐷, such that 𝑃 is invertible (has a matrix inverse) and 𝑃𝐷𝑃
−1 = 𝑀.
The process of finding matrices 𝑃 and 𝐷 is called diagonalisation. It turns out that every
symmetric matrix is diagonalisable.
Consider the specific example matrix below.
𝑀 = [
−2 3 −3
3 3 2
−3 2 3
]
(a) Write Python code to enter 𝑀 as a numpy array and print out 𝑀.
(b) The Python code below uses numpy to find the eigenvalues and eigenvectors of 𝑀.
V, P = np.linalg.eig(M)
print(V)
7144CEM Data Science Python Labs (2024/25 Semester 2)
18
print(P)
Write Python code to create a diagonal matrix 𝐷 which has the entries from 𝑉 along
the main diagonal. Use numpy to check that 𝑃𝐷𝑃
−1 = 𝑀 in this case.
(c) Interpret the matrix product 𝑃𝐷𝑃
−1
in terms of matrix transformations.
Exercise 4. Consider the following matrix.
𝑀 = [
1 1 0
1 0 1
0 1 1
]
(a) Write Python code to enter 𝑀 as a numpy array and print out 𝑀.
(b) The Python code below constructs the matrices 𝑄 and 𝑅 from 𝑀. Add Python code
to print out 𝑄 and 𝑅, and check that 𝑄𝑅 = 𝑀.
import scipy.linalg as sla
Q, R = sla.qr(M)
(c) Write Python code to check that 𝑄 is an orthogonal matrix, i.e., that 𝑄
𝑇𝑄 = 𝐼. What
kind of matrix is 𝑅?
Exercise 5. Consider the following matrix.
𝑀 = [
6 15 55
15 55 225
55 225 979
]
(a) Write Python code to enter 𝑀 as a numpy array and print out 𝑀.
(b) The Python code below constructs the matrix 𝐿 from the matrix 𝑀. Add Python code
to compare 𝑀 with 𝐿𝐿
𝑇 and 𝐿
𝑇𝐿. What conclusions can you draw about 𝐿? In
general, what condition does 𝑀 need to satisfy so that 𝐿 can be calculated from 𝑀?
import numpy as np
L = np.linalg.cholesky(M)
print(L)
7144CEM Data Science Python Labs (2024/25 Semester 2)
19
(c) Consider the Python code given below. Investigate (through Python code and online
documentation) how 𝑆 and 𝑇 are related to 𝑀.
import scipy.linalg as sla
S = np.sqrt(M)
T = sla.sqrtm(M)
Exercise 6. Consider the matrix 𝑀 given below.
𝑀 = [
1 2 3
5 1 2
9 5 1
]
(a) Write Python code to enter 𝑀 as a numpy array and print out 𝑀.
(b) Use np.sum() to calculate the sum of each row of 𝑀 and the sum of each column of
𝑀. Hint: check your output from np.sum() makes sense and look at the online
documentation.
(c) Consider the two diagonal matrices 𝐷 and 𝐸 given in the Python code below.
Calculate the matrix product 𝑆 = 𝐷𝑀𝐸 and print out 𝑆. What property do the rows
and columns of 𝑆 have? Hint: 𝑆 is called a “doubly stochastic” matrix.
import numpy as np
D = np.diag([1.29769972, 1.27691898, 0.67262161])
E = np.diag([0.07280195, 0.13820884, 0.14045822])
(d) Write Python code to build the matrices 𝐴 =
1
2
(𝑀 + 𝑀𝑇
) and 𝐵 =
1
2
(𝑀 − 𝑀𝑇
). Use
np.allclose() to demonstrate that one of 𝐴 and 𝐵 is a symmetric matrix, the other
one is a skew-symmetric matrix, and that 𝐴 + 𝐵 gives 𝑀.
7144CEM Data Science Python Labs (2024/25 Semester 2)
20
Group Challenge. The trace of a square matrix is the sum of the elements on its main
diagonal (from the top-left to the bottom-right). We can randomly generate 2 × 2 matrices
using the Python code below. Then we can use numpy to calculate the trace and
determinant of the matrix.
M = np.random.randint(-10,11,(2,2))
print('Generated M:')
print(M)
trace = np.trace(M)
print(' trace =',trace)
det = np.linalg.det(M)
print(' det =',det)
(a) Explore how the trace and determinant of the matrix 𝑀 are related to the
eigenvalues of 𝑀. Do you get the same conclusion for 3 × 3 matrices?
(b) Investigate the value of the matrix 𝐵:
𝐵 = 𝐴
2 − 𝑡𝐴 + 𝑑𝐼
where 𝐴 is a 2 × 2 matrix, 𝑡 is the trace of 𝐴, 𝑑 is the determinant of 𝐴, and 𝐼 is the
identity matrix. Note that 𝐴
2
is A@A not A*A. Do you get the same conclusion for
3 × 3 matrices?
"""