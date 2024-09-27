import pandas as pd
import scipy.stats as st

# In a survey of 1200 randomly selected registered voters,
# 348 were in favor of banning public smoking. Find the 95%
# conﬁdence interval for the proportion of voters in favor
# of banning public smoking.

# Let n be the number of voters surveyed.
n = 1200

# Let p be the proportion of voters that voted in favor
p = 348.0/1200.0

# The standard error is sqrt(p * (1-p)/n)
stderr = (p * (1 - p)/n) ** 0.5

print(st.norm.interval(0.95, p, stderr))


# In the Exam Scores data set, find a 99% confidence interval
# for the proportion of students who scores more than 90 in Exam 1.
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Let n be the number of students who took Exam 1.
n = scores[['Exam1']].count()

# Let x be the total of all Exam 1 scores greater than 90
x = (scores[['Exam1']] > 90).values.sum()

# Let p be x/n, the proportion of all students that scored over 90 on Exam 1
# Multiplying by 1.0 is needed for correct floating point arithmetic
p = x/n*1.0

# The standard error is sqrt(p * (1-p)/n)
stderr = (p * (1 - p)/n) ** 0.5

print(st.norm.interval(0.99, p, stderr))


# 1000 random voters, 571 against new law.
# What is the sample proportion?
n = 1000
p = 571.0/1000.0
print(p)

# To find the margin of error at a 90% confidence level, we can use the formula:
# margin of error = z_star * sqrt(p * (1-p)/n)
z_star = 2.576
stderr = (p * (1 - p)/n) ** 0.5
moe = z_star * stderr
print(moe)

# The 99% confidence interval is:
print(st.norm.interval(0.99, p, stderr))



# A poll reports 43% support with a margin of error of 1.54 percentage points.
## How many voters should be sampled for a 95% confidence interval?
## We use our chart to find the z_star for a 95% confidence level:
z_star = 1.960
## We are given the margin of error
moe = 1.54
## We are given the proportion
p = 0.43
## We can now calculate the sample size
n = (z_star**2*p*(1-p))/moe**2
print(n)



# Poll has a margin of error of 4.78.
# How many voters should be sampled for a 95% confidence interval?

z_star = 1.645
moe = 4.78

# To find the sample size, we can use the formula:
# n = (z_star^2 * p * (1-p))/moe^2
# We are given the margin of error
moe = 4.65
# We are given the proportion
p = 0.5
# We can now calculate the sample size
n = (z_star**2*p*(1-p))/moe**2
print(n)


