# Z-test for Population Mean

A z-test is a hypothesis test in which the z-statistic follows a normal distribution. The z-test for a population mean can be used to determine whether the population mean is the same as the hypothesized mean m, assuming that the population standard deviation std is known. When performing a hypothesis test involving the mean of a single population with a known population standard deviation.

The z-test for a population mean is used to test the null hypothesis that the population mean is equal to a specified value m. The alternative hypothesis can be either two-tailed, left-tailed, or right-tailed, depending on the nature of the difference from the null hypothesis.

more useful test involves the t-distribution, which is used when the population standard deviation is unknown. The t-distribution is similar to the normal distribution but has heavier tails, which makes it more appropriate for small sample sizes.

## Conditions for the Z-Test for Population Mean

1. **Random Sampling**: The sample data must be obtained through a random sampling method.
2. **Independent Sampling**: The sample data must be independent of each other.
3. **Normal Population Distribution**: The population from which the sample is drawn must be normally distributed or the sample size must be sufficiently large (n > 30).

## Procedure for the Z-Test for Population Mean

1. **Set Null and Alternative Hypotheses**: Define the null hypothesis Ho and the alternative hypothesis Ha.
2. **Use Statistical Software to find the test statistic**: Calculate the z-statistic from the sample data.
3. **Determine the P-Value**: Calculate the p-value from the z-statistic.

### Example

A popular electronics website wants to determine whether a smartphone has an 7.8 hour battery life as claimed by the manufacturer in response to user complaints of poor battery life. The website sampled 10 smartphones with a mean battery life of 7.6 hours. The population standard deviation of the battery life is std=0.57 hours. Does sufficient evidence exist that the battery life of the smartphone is actually lower than the manufacturer's claim at a significance level of a=0.05 ?

**Solution:**

The null hypothesis is that the smartphone's mean battery life is Ho=7.8 hours. Because customers believe that the mean battery life is lower, the hypothesis test is left-tailed. That is, the alternative hypothesis is that the smartphone's mean battery life is less than 7.8 hours. Mathematically, Ho: mean = 7.8 and Ha: mean < 7.8.

Since m=7.6, n=10, and std=0.57, the z-statistic is calculated as follows:

```python
z = (m - mean) / (std / sqrt(n))
  = (7.6 - 7.8) / (0.57 / sqrt(10))
  = -1.0526
```

The p-value is calculated using statistical software, like so:

```python
p = norm.cdf(z)
  = norm.cdf(-1.0526)
  = 0.146
```

Since the p-value is greater than the significance level a=0.05, insufficient evidence exists to support the hypothesis that the mean battery life of the smartphone is less than the manufacturer's claim.

**Analysis:**
Although the mean battery life of the 10 sampled smartphones is less than the manufacturer's claim, the lower mean could have occurred due to chance. However, the probability that the sample mean battery life is at most 7.6 hours is 13.3%, which is much higher than the probability of incorrectly rejecting the manufacturer's claim that the smartphone has a mean battery life of 7.8 hours. Thus, the lower sample mean can be most likely be attributed to chance.
