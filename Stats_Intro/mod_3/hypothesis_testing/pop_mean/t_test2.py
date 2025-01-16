import scipy.stats as stats

# Calculate the t-statistic, degrees of freedom, and p-value
sample_size = 30
sample_mean = 14.06
sample_std = 0.13
pop_mean = 14

# Calculate the t-statistic
t_statistic = (sample_mean - pop_mean) / (sample_std / (sample_size ** 0.5))
print("T Statistic: ", t_statistic)

# What is the degrees of freedom?
degrees_of_freedom = sample_size - 1
print("Degrees of Freedom: ", degrees_of_freedom)

# Calculate the p-value
p_value = 1 - stats.t.cdf(t_statistic, df = degrees_of_freedom)
print("P Value: ", p_value)

# Should we reject the null hypothesis at a 0.05 significance level?
## NOTE: Rejecting the null hypothesis is accepting the alternative hypothesis
sig_lvl = 0.05
if p_value < sig_lvl:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

# NOTE: To know if we are doing a z-test or a t-test, we need to know if we have the population standard deviation or not.
    # If we have the population standard deviation, we can use the z-test.
    # If we do not have the population standard deviation, we can use the t-test.


