"""
Exercises
Exercise 1. Suppose we roll two regular unbiased 6-sided dice. We are interested in the
distribution of the maximum of the two dice rolls. We can use the Python code below to
observe values from this process.
import numpy as np
A = np.random.choice([1,2,3,4,5,6],size=100)
print(A)
B = np.random.choice([1,2,3,4,5,6],size=100)
print(B)
sample = np.maximum(A,B) # careful this is not np.max()
print(sample)
(a) In probability theory we can calculate the mean and variance of the distribution of
the maximum of two dice rolls: mean is exactly 161/36 and variance is exactly
2555/1296. Do the sample mean and sample variance agree with these? Hint: you
might need a larger sample size.
(b) Modify the Python code above to investigate the maximum of three dice rolls (each
dice is a regular unbaised 6-sided dice). Estimate the mean and variance.

Exercise 2. Consider the triangular distribution which has three parameters: 𝐿 (left), 𝑀
(middle), and 𝑅 (right). The Python code given below plots a particular triangular
distribution with the given values of 𝐿, 𝑀 and 𝑅.
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
L, M, R = (10,20,60)
plt.figure()
x = np.arange(L-5,R+6)
y = stats.triang.pdf(x, c=(M-L)/(R-L), loc=L, scale=R-L)
plt.plot(x,y,'b-')
plt.grid()
plt.show()
(a) The mean of a triangular distribution is exactly (𝐿 + 𝑀 + 𝑅)/3. Calculate the mean,
the median, and the upper quartile of the particular triangular distribution above and
add them to the plot using vertical dashed lines. Include both Python code and
output in your answer.
(b) Generate a random sample of 10000 values from the particular triangular given
above. Plot a histogram of your sample using 50 bins. Calculate the mean, median,
and upper quartile from your sample and compare to the equivalent values from part
(a). Include both Python code, histogram and output in your answer.

Exercise 3. The Beta distribution is commonly used in Bayesian data analysis. A Beta
distribution is governed by two parameters: 𝑎 and 𝑏. The Python code below plots the
probability density function (pdf) of the particular Beta distribution with the given values of
𝑎 and 𝑏.
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
a = 2
b = 5
x = np.arange(0,1.01,0.01)
y = stats.beta.pdf(x, a, b)
plt.figure()
plt.plot(x,y,'b-')
plt.grid()
plt.show()
(a) The mean of a Beta distribution is exactly 𝑎/(𝑎 + 𝑏). Calculate the mean, and the
upper quartile (75% percentile) of the particular Beta distribution above and add
them to the plot using vertical dashed lines. Include both Python code and output in
your answer.
(b) It is claimed that the following Python code generates a sample from a Beta
distribution.
sample = []
for i in range(100000):
 A = np.random.random(a+b-1)
 A.sort()
 sample.append(A[a-1])
Plot a histogram (using 50 bins) of the sample produced using the Python code
above. Calculate the mean and upper quartile from this sample and compare to the
equivalent values from part (a). Does the sample appear to be random values from
the particular Beta distribution from part (a)? Justif




"""