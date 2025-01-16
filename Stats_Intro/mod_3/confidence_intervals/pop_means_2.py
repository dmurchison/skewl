import math
from numpy import std
import scipy.stats as st

# A tax assessor assesses the mean property tax bill for all property owners in a certain city.
# A recent survey obtained a sample mean of 1400 dollars. The population standard deviation is known to be 1000 dollars.

# How many tax records should be obtained at a 90% confidence level if the margin of error is 100 dollars?

# We use our chart to find the z_star for a 90% confidence level:
z_star = 1.645

# We are given the population standard deviation
pop_std = 1000

# We are given the sample mean
sample_mean = 1400

# To find out how many tax records should be obtained, we need to find the sample size
# We can use the formula for margin of error to find the sample size
# margin_of_error = z_star*pop_std/np.sqrt(sample_size)
# We can rearrange the formula to solve for sample_size
# sample_size = (z_star*pop_std/margin_of_error)**2
# We can now plug in the values to find the sample size
margin_of_error = 100
sample_size = (z_star*pop_std/margin_of_error)**2
print("The number of tax records that should be obtained is: ", sample_size)


# The weight (in pounds) of 6 pumpkins are 5,7,7.5,8,8.5, and 8.75. The weights of the sample have a mean of 7.458
# and a standard deviation of 1.364.

# What is the degree of freedom for the t-distribution?
# The degree of freedom for the t-distribution is the sample size minus 1
sample_size = 6
degree_of_freedom = sample_size - 1

# What is the critical value when the significance level is 0.1?
# We can use the t.ppf function from the scipy library to find the critical value
# The t.ppf function takes in the significance level, the degree of freedom, and the mean and standard deviation
sample = [5,7,7.5,8,8.5,8.75]
sig_level = 0.1
df = len(sample) - 1
mean = st.norm.mean(sample)
std_dev = 1.364
## The standard_error is the standard deviation divided by the square root of the sample size
std_error = std_dev/math.sqrt(sample_size)
## The critical value
critical_val = 2.015
## Now we can find the margin of error
margin_of_error = critical_val*std_dev/math.sqrt(sample_size)
print("The margin of error at a 90% confidence level is: ", margin_of_error)


# What is the 90% t-confindence interval?
# We can use the t.interval function from the scipy library to find the confidence interval
# The t.interval function takes in the significance level, the degree of freedom, the mean and standard error
# The t.interval function returns the confidence interval
conf_interval = st.t.interval(0.90, 5, 7.458, std_error)
print("The 90% confidence interval is: ", conf_interval)

n = 100

# Degrees of freedom is number of samples minus 1
df = n - 1

mean = 219

# The standard error is standard deviation/sqrt(number of samples)
stderr = 35.0/(n ** 0.5)

print(st.t.interval(0.95, df, mean, stderr))





moe = 2.1
conf = 0.90
samp_std = 7.3

# We use our chart to find the z_star for a 90% confidence level:
z_star = 1.645

# We are given the standard deviation
samp_std = samp_std

# Calc the prelimary estimate of the sample size
n = (z_star*samp_std/moe)**2
print("The preliminary estimate of the sample size is: ", n)

# if df is 32 and critical_val is 1.694 what is sample size
df = 32
critical_val = 1.694
moe = 2.1
samp_std = 7.3
n = (critical_val*samp_std/moe)**2
print("The preliminary estimate of the sample size is: ", n)



## Suppose the mean height in inches of all 9th graders is estimated. The population standard deviation is 3 inches.
## The heights of 7 randomly selected 9th graders are 62,61,68,63,63,71,67.

sam = [62,61,68,63,63,71,67]
sam_size = len(sam)
sam_mean = sum(sam)/sam_size

print("The sample mean is: ", sam_mean)
sam_std = 3

# To find the margin of error at a 99% confidence level, we can use the formula:
# margin_of_error = z_star*pop_std/np.sqrt(sample_size)

# We use our chart to find the z_star for a 99% confidence level:
z_star = 2.576

m = z_star*sam_std/math.sqrt(sam_size)
print("The margin of error at a 99% confidence level is: ", m)

# The 99% confidence interval is
conf_int = st.norm.interval(0.99, loc=sam_mean, scale=sam_std/math.sqrt(7))
print("The 99% confidence interval is: ", conf_int)

sample_size = 6
degree_of_freedom = sample_size - 1
sig_lvl = 0.05
std_dev = 3
t_star = st.t.ppf(1-0.05/2, 5)
print("The critical value is: ", t_star)
mean = 10
std_error = std_dev/math.sqrt(sample_size)
conf_int = st.t.interval(0.95, 5, 10, std_error)
mrgin = t_star*std_dev/math.sqrt(sample_size)

print("The margin of error at a 95% confidence level is: ", mrgin)
print("The 95% confidence interval is: ", conf_int)
