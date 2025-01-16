# An electrician wants to know whether batteries made by two manufacturers have significantly different valtages.
# The voltage of 100 batteries from each manufacturer were measured. The population standard deviations are known.
# Manufacturer A: Sample mean = 119, Population standard deviation = 1
# Manufacturer B: Sample mean = 118, Population standard deviation = 5

# What type of hypothesis test should be used?
# Two-tailed test should be used because we want to know if the population means are significantly different.

# What is the null hypothesis?
# H0: μ1 = μ2 (The population means are equal)

# What is the test statistic?
# The test statistic is the z-score. which is calculated as follows:
# z = (x̄1 - x̄2) / √((σ1^2 / n1) + (σ2^2 / n2))
# With python, we can calculate the z-score as follows:
from statsmodels.stats.weightstats import ztest

sample_mean_a = 174
sample_mean_b = 173
pop_std_a = 1
pop_std_b = 4
n_a = 150 # sample size for manufacturer A
n_b = 150 # sample size for manufacturer B

print(ztest([sample_mean_a, sample_mean_b], value=0, alternative='two-sided'))


# A transportation commission studies driving times between two cities to determine whether the construction of a new highway reduced commute times.
# Times for 40 cars driving on the old highway and times for 50 cars driving on the new highway are obtained. A summary of the data obtained from the study is given below.

# Old Highway: Sample mean = 5.35, Population standard deviation = 0.5
# New Highway: Sample mean = 4.95, Population standard deviation = 0.8

# What is the standard error of the difference between the sample means?
# The standard error of the difference between the sample means is calculated as follows:
# SE = √((σ1^2 / n1) + (σ2^2 / n2))
# With python, we can calculate the standard error as follows:
import scipy.stats as stats

sm_old = 5.35
sm_new = 4.95
pop_std_old = 0.5
pop_std_new = 0.8
n_old = 40
n_new = 50

se = ((pop_std_old ** 2 / n_old) + (pop_std_new ** 2 / n_new)) ** 0.5
print(se)

# What is the z-score for the difference between the sample means?
# The z-score for the difference between the sample means is calculated as follows:
# z = (x̄1 - x̄2) / SE
# With python, we can calculate the z-score as follows:
z = (sm_old - sm_new) / se
print(z)

# What is the p-value for the z-score?
# Since we are looking to see if commute times have been reduced, we are interested in the left tail of the distribution. P(z >= 2.898) which is 0.0019.
p_value = 1 - stats.norm.cdf(z) # we use the 1 - cdf() function to calculate the p-value for the z-score when the alternative hypothesis is less than.
print(p_value)

# Should the null hypothesis be rejected at a 0.05 significance level?
# Since the p-value is less than 0.05, we reject the null hypothesis. There is enough evidence to suggest that commute times have been reduced.






# The ztest(x1, x2, value = 0) function can also be used to perform a two-sample z-test for means. However, the value parameter should be set to 0.
# The function requires the statsmodels.stats.weightstats library to be imported and takes two inputs.
# The first input x1 is an array containing sample observations from one population and the second input is also an array containing sample observations from another population.

# The function returns the z-score and the two tailed p-value.
sample1 = [21, 28, 40, 55, 58, 60]
sample2 = [13, 29, 50, 55, 71, 90]
print(ztest(x1 = sample1, x2 = sample2))

