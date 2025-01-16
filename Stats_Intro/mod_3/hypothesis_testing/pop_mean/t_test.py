import scipy.stats as st

sample_size = 54
sample_mean = 12.03
pop_std = 0.11
pop_mean = 12

# Calculate what the sample_std should be so we have it for other calculations
sample_std = pop_std / (sample_size ** 0.5)
print("Sample Standard Deviation: ", sample_std)

# Calculate the z-statistic
z_statistic = (sample_mean - pop_mean) / (pop_std / (sample_size ** 0.5))
print("Z Statistic: ", z_statistic)

# Calculate the p-value
p_value = 1 - st.norm.cdf(z_statistic)
print("P Value: ", p_value)

# Should we reject the null hypothesis at a 0.1 significance level?
## NOTE: Rejecting the null hypothesis is accepting the alternative hypothesis
sig_lvl = 0.01
if p_value < sig_lvl:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")


