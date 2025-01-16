import scipy.stats as stats
import pandas as pd
import numpy as np


treat = 95/5000
ctrl = 125/5000
p = (95 + 125) / (5000 + 5000)

print(treat, ctrl)
print(p)

# Standard Error
se = np.sqrt(p * (1 - p) * (1/5000 + 1/5000))
print(se)

# Z-score
z = (treat - ctrl) / se
print(z)

# One Tailed P-value
p_val = stats.norm.cdf(z)
print(p_val)

# Another way to get the (TWO TAILED) p-value and the z-score is to use the proportions_ztest().
from statsmodels.stats.proportion import proportions_ztest

count = [95, 125]
nobs = [5000, 5000]
z, p_val = proportions_ztest(count, nobs)
print(z, p_val)



city_1 = 505/800
city_2 = 572/1000
print(city_1, city_2)
p = (505 + 572) / (800 + 1000)
print(p)

# Since we are checking if city 1 has more support than city 2, we use the 'smaller' alternative. Larger makes this tailed to the right.
t, pp = proportions_ztest([505, 572], [800, 1000], alternative='smaller')
print(t, pp)





