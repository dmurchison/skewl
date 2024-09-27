import scipy.stats as st
from statsmodels.stats.weightstats import ztest
import pandas as pd


# This is a snippet from MAT_243/mod_3/hypothesis_testing/t_test.py
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
print(ztest(x1 = scores['Exam1'],  value = 86))



# Intelligence quotient (IQ) test scores are believed to have a mean of 100 and a population standard deviation of 15.
# In a random sample of 36 students in a high school, the mean IQ test score is 105.
# Researchers claim that the mean IQ test scores at this high school is statistically higher than 100.

pop_mean = 100
pop_std = 15
sample_size = 36
sample_mean = 105

# Calculate the z-score
z_score = (sample_mean - pop_mean) / (pop_std / (sample_size ** 0.5))
print("Z Score: ", z_score)

# Calculate the p-value
p_value = 1 - st.norm.cdf(z_score)
print("P Value: ", p_value)

# Calculate the z-test
# x1 = sample mean
# value = population mean
# alternative = 'larger' because we are testing if the sample mean is greater than the population mean
# z_test = ztest(x1 = sample_mean, value = pop_mean, alternative = 'larger')


# Should we reject the null hypothesis at a 0.05 significance level?
sig_lvl = 0.05
if p_value < sig_lvl:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

