import scipy.stats as st
from statsmodels.stats.weightstats import ztest


sample_size = 50
pop_mean = 2.30
z_stat = 2.72

# If the population standard deviation is unknown and the sample size is not sufficiently large, would you still use
# the Normal distribution to calculate these confidence intervals, or would you choose another distribution?
# If the latter, which distribution would you choose?
# No, We would use the t-distribution to calculate the confidence intervals.
