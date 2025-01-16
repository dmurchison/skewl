import scipy.stats as st
from math import sqrt

# For a normal distribution, if the mean is 55 and
# the standard deviation is 7.5, what is x* if P(x < x*) = 0.8247?
print(st.norm.ppf(0.40, 150, 8.75))

# For a normal distribution, if the mean is 55 and
# the standard deviation is 7.5, what is x* if P(x > x*) = 0.95?
print(st.norm.isf(0.20, 150, 8.75))

print(st.norm.sf(7, 5, 2))
print(st.norm.cdf(7, 5, 2))

print(29/sqrt(36))
