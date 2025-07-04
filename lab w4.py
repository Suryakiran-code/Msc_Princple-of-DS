"""
Exercises
Exercise 1. A 2013 journal article published in Nutrition and Cancer found a negative
correlation between coffee consumption and breast cancer in women. Can we conclude
that coffee protects against cancer?
Ref: Lowcock E.C., Cotterchio M., Anderson L.N., Boucher B.A., El-Sohemy A. (2013) High
coffee intake, but not caffeine, is associated with reduced estrogen receptor negative and
postmenopausal breast cancer risk with no effect modification by CYP1A2 genotype,
Nutrition and Cancer, 65(3), 398–409. https://pubmed.ncbi.nlm.nih.gov/23530639/

Exercise 2. Consider the following Python code.
import numpy as np
n = 1000000
a = np.random.random(size=n)
b = np.random.random(size=n)
z = np.sqrt(-2*np.log(a))*np.cos(2*np.pi*b)
(a) Write Python code to find the covariance between 𝑎 and 𝑏.
(b) Write Python code to find the mean and standard deviation of 𝑧, and plot a
histogram of 𝑧 using 30 bins. What distribution does 𝑧 appear to follow? Include
both Python code and output in your answer.

Exercise 4. The Python code given below creates a random sample from a particular
bivariate normal distribution.
import numpy as np
import scipy.stats as stats
n = 1000
sample = stats.multivariate_normal.rvs(size=n,mean=[0,0],
 cov=np.eye(2))
print(sample.shape)
(a) Use Python to plot an appropriate scatterplot of this sample and calculate the
sample correlation coefficient. Briefly comment on what you observe. Include both
Python code and output in your answer.
(b) Consider the Python code given below. What conclusion can you make about the
correlation coefficient of transformed_sample? Justify your answer using at least
two different values of 𝑟.
import numpy as np
r = 0.5
M = np.array([[1,r],[r,1]])
L = np.linalg.cholesky(M)
transformed_sample = sample@L.T

Group Challenge. The Python code given below draws a 𝑛 × 2 random sample from a
particular bivariate normal distribution.
import numpy as np
import scipy.stats as stats
mu = np.array([[1],[2]])
sigma = np.array([[3,-2],[-2,5]])
n = 100
sample = stats.multivariate_normal.rvs(size=n,mean=mu.flatten(),cov=sigma)
(a) Calculate the 2 × 1 sample mean vector (mean of each column but reshaped as a
2 × 1 vector) and the 2 × 2 sample covariance matrix 𝐶 using np.cov() and
compare these to mu and sigma. What do you notice as 𝑛 increases in value?
(b) Carefully subtract the mean of each column of the sample from that column; this
gives the centred sample 𝑋𝐶. Make sure that 𝑋𝐶 has the same shape as sample.
Investigate how the covariance matrix 𝐶 (from part (a)) is related to the matrix
product 𝑋𝐶
𝑇𝑋𝐶.
(c) Calculate the sample correlation matrix 𝑅 using np.corrcoef(). Make sure that
𝑅 is a 2 × 2 matrix. Let 𝐸 be the diagonal matrix consisting of the square roots of
the diagonal elements of 𝐶. Investigate how 𝑅 can be calculated from 𝐶 and 𝐸
−1
by matrix multiplication. Note that 𝐸
−1
is the matrix inverse of 𝐸.
"""