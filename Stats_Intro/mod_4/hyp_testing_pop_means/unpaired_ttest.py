import scipy.stats as st
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest



df = pd.read_csv('https://data-analytics.zybooks.com/Memory.csv')
tstat, pval = st.ttest_ind(df['drug'], df['nodrug'], equal_var=False, alternative="less") # by setting alternative to "less", we are looking for a negative difference

print("t-statistic:", tstat)
print("p-value:", pval)

x1 = 120
x2 = 118
s1 = 2
s2 = 4
n1 = 17
n2 = 17

# Unpaired t-test
# Ho : u1 = u2
# Ha : u1 != u2

# The test statistic is the t-score, which is calculated as follows:
# t = (x̄1 - x̄2) / √((s1^2 / n1) + (s2^2 / n2))
# With python, we can calculate the t-score as follows:
t = (x1 - x2) / np.sqrt((s1 ** 2 / n1) + (s2 ** 2 / n2))
print(t)

df = n1 + n2 - 2
print(df)

# P-value
# The p-value is calculated as follows:
# p = 2 * (1 - stats.t.cdf(t, df))
# With python, we can calculate the p-value as follows:
p = 2 * (1 - st.t.cdf(t, df))
print(p)


n = 6
std_dev = 2
res_a = 98
res_b = 95
mean_diff = res_a - res_b

# Unpaired t-test
# Ho : u1 = u2
# Ha : u1 != u2

# The test statistic is the t-score, which is calculated as follows:
# t = (x̄1 - x̄2) / √((s1^2 / n1) + (s2^2 / n2))
# With python, we can calculate the t-score as follows:
t = mean_diff / (std_dev / np.sqrt(n))
print(t)

df = n -1
print(df)

# P-value
# The p-value is calculated as follows:
# p = 2 * (1 - stats.t.cdf(t, df))
# With python, we can calculate the p-value as follows:
p = 2 * (1 - st.t.cdf(t, df))
print(p)





