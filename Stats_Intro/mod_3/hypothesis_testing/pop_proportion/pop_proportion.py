import math
import scipy.stats as st
from statsmodels.stats.proportion import proportions_ztest


# Calculate all variables
sample_size = 114
count = 72
sample_proportion = round(count / sample_size,3)
pop_proportion = 0.56

# Calculate the z-statistic
z_statistic = (sample_proportion - pop_proportion) / math.sqrt((pop_proportion * (1 - pop_proportion)) / sample_size)
print("Z Statistic: ", z_statistic)

# The poportion z-test is a one-tailed test
# Calculate the z-test
# count = number of successes
# nobs = sample size
# value = population proportion
# alternative = 'larger' because we are testing if the sample proportion is greater than the population proportion
z_test = proportions_ztest(count = count, nobs = sample_size, value = pop_proportion, alternative = 'larger')

# Calculate the p-value
p_value = 1 - st.norm.cdf(z_statistic)

# If it is a two-tailed test, we need to multiply the p-value by 2
p_value *= 2
print("P Value: ", p_value)

# Should we reject the null hypothesis at a 0.05 significance level?
sig_lvl = 0.1
if p_value < sig_lvl:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

# If the pop standard deviation is unknown, which of the following python methods is used to perform hypothesis testing?
# A. ttest_1samp()
# B. ztest()
# C. prop_1samp_hypothesis_test()
# D. ttest()

