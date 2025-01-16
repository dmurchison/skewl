import scipy.stats as st
import numpy as np
import pandas as pd
import math

# Suppose the mean final grade is estimated for all introductory statistics classes taught at a particular college.
# The population standard deviation is 4. The final grades for a randomly selected statistics class with people are:
# 76,80,82,83,83,85,85,87,88
# Find the 0.95 confidence interval for the mean final grade.


## Lets start by calculating what variables we know:
## We know the population standard deviation is 4
std_dev = 4
## We know the sample size is 9
sample_size = 9
## We calc the sample mean by creating a list of the grades and using the mean function from the numpy library
grades = [76,80,82,83,83,85,85,87,88]
sample_mean = np.mean(grades)
print("The sample mean is: ", sample_mean)

## First we use our chart to find the z_star for a 95% confidence level:
z_star = 1.960
print("The z_star, or critical_value is: ", z_star)

## Next we calculate the margin or error:
margin_of_error = z_star*std_dev/np.sqrt(sample_size)
print("The margin of error is: ", margin_of_error)

## Standard error is the standard deviation divided by the square root of the sample size
std_error = std_dev/np.sqrt(sample_size)

## Now we can calculate the confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print("The 95% confidence interval for the mean final grade is: ", [lower_bound, upper_bound])


array = [10,17,17.5,18.5,19.5]
pop_std = 1.25
def margin_of_error_90(array, pop_std):
    ## We use our chart to find the z_star for a 90% confidence level:
    z_star = 1.645
    ## We are given the population standard deviation
    pop_std = pop_std
    ## We calc the sample mean by creating a list of the grades and using the mean function from the numpy library
    sample_mean = np.mean(array)
    print("The sample mean is: ", sample_mean)
    ## We calc the sample size by using the len function
    sample_size = len(array)
    print("The sample size is: ", sample_size)
    ## Next we calculate the margin or error:
    margin_of_error = z_star*pop_std/np.sqrt(sample_size)
    return margin_of_error

print("The margin of error at a 90% confidence level is: ", margin_of_error_90(array, pop_std))


# What is the margin or error at a 99% confidence level?
def margin_of_error_99(array, pop_std):
    ## We use our chart to find the z_star for a 99% confidence level:
    z_star = 2.576
    ## We are given the population standard deviation
    pop_std = pop_std
    ## We calc the sample mean by creating a list of the grades and using the mean function from the numpy library
    sample_mean = np.mean(array)
    print("The sample mean is: ", sample_mean)
    ## We calc the sample size by using the len function
    sample_size = len(array)
    print("The sample size is: ", sample_size)
    ## Next we calculate the margin or error:
    margin_of_error = z_star*pop_std/np.sqrt(sample_size)
    return margin_of_error

print("The margin of error at a 99% confidence level is: ", margin_of_error_99(array, pop_std))


# What is the 90% confidence interval
def confidence_interval_90(array, pop_std):
    ## We use our chart to find the z_star for a 90% confidence level:
    z_star = 1.645
    ## We are given the population standard deviation
    pop_std = pop_std
    ## We calc the sample mean by creating a list of the grades and using the mean function from the numpy library
    sample_mean = np.mean(array)
    print("The sample mean is: ", sample_mean)
    ## We calc the sample size by using the len function
    sample_size = len(array)
    print("The sample size is: ", sample_size)
    ## Next we calculate the margin or error:
    margin_of_error = z_star*pop_std/np.sqrt(sample_size)
    ## Now we can calculate the confidence interval
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return [lower_bound, upper_bound]

print("The 90% confidence interval is: ", confidence_interval_90(array, pop_std))


# To find the 99% confidence interval, we can use the np.percentile function
def confidence_interval_99(array, pop_std):
    ## We calc the z_star for a 99% confidence level
    z_star = 2.576
    ## We are given the population standard deviation
    pop_std = pop_std
    ## We calc the sample mean by creating a list of the grades and using the mean function from the numpy library
    sample_mean = np.mean(array)
    print("The sample mean is: ", sample_mean)
    ## We calc the sample size by using the len function
    sample_size = len(array)
    print("The sample size is: ", sample_size)
    ## We now find the margin of error
    margin_of_error = z_star*pop_std/np.sqrt(sample_size)
    ## Now we can calculate the confidence interval
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return [lower_bound, upper_bound]

print("The 99% confidence interval is: ", confidence_interval_99(array, pop_std))


# To calculate the standard error, we can divide the population standard deviation by the square root of the sample size
def std_error(array,pop_std):
    ## We are given the population standard deviation
    pop_std = pop_std
    ## We calc the sample size by using the len function
    sample_size = len(array)
    ## We calc the standard error
    return pop_std/np.sqrt(sample_size)

print("The standard error is: ", std_error(array, pop_std))

# The st.norm.interval function can also be used to find the confidence interval if we have the standard error, mean, and confidence level
print(st.norm.interval(0.99, loc=np.mean(array), scale=std_error(array, pop_std)))


scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
sigma = 2.5
mean = scores['Exam1'].mean()
stderr = sigma/math.sqrt(len(scores['Exam1']))
print(st.norm.interval(0.99, mean, stderr))

