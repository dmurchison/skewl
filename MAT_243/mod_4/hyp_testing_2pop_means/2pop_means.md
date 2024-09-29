# Hypothesis Testing for Two Population Means

## Comparing Two Population

Hypothesis testing involving a one-sample test determines whether an observed value differs statistically from a hypothesized population value. Sometimes, differences between two populations are studied instead. Ex: Pollsters often look at issues in which the opinions of two different groups may vary wildly, such as political preferences of men compared to those of women.

Hypothesis tests involving two samples follow the same steps. A survey is conducted and statistics are calculated. The standard error for the difference between populations is the square root of the sum of the squares of the standard errors of each population. The test statistic is the difference between the observed and hypothesized value divided by the standard error. Mathematically,

```math
sqrt((s1^2/n1) + (s2^2/n2))
```

where `s1` and `s2` are the standard deviations of the two populations, and `n1` and `n2` are the sample sizes. The degrees of freedom are the sum of the degrees of freedom of each population. The critical value is found using the degrees of freedom and the desired level of significance.

## Two-sample z-test for Population Means

The z-test can also be used to determine whether the means of two independent populations are the same when the population standard deviations are known. When performing a hypothesis test involving the means of two independent populations, the distribution of the z-test

The formula for the z-test is:

```math
z = (x1 - x2) / sqrt((s1^2/n1) + (s2^2/n2))
```

where `x1` and `x2` are the means of the two populations, `s1` and `s2` are the standard deviations of the two populations, and `n1` and `n2` are the sample sizes. The degrees of freedom are the sum of the degrees of freedom of each population. The critical value is found using the degrees of freedom and the desired level of significance.

### Procedure for Hypothesis Testing for Two Population Means

*Given two randomly selected samples each taken from an independent population where the standard deviations of each population is known,*

1. State the null and alternative hypotheses, H0 and Ha.
2. Determine the level of significance, α.
3. Calculate the test statistic, z.
4. Determine the critical value, zα/2, "p-value"
5. Make a decision to reject or fail to reject the null hypothesis.
    - If the test statistic is greater than the critical value, reject the null hypothesis.
    - If the test statistic is less than the critical value, fail to reject the null hypothesis.
6. Interpret the results of the hypothesis test.

### Example 1

The mean burn time of two brands of 11-ounce candles are compared by a home safety magazine. The burn times of 100 candles of each brand are measured. The results are given in the table below.

| Candle | Sample mean burn time (hours) | Population standard deviation |
|--------|-------------------------------|-------------------------------|
| A      | 27.5                          | 2.5                           |
| B      | 26                            | 3.5                           |

Does sufficient evidence exist supporting the claim that the mean burn time of candle 1 is greater than the mean burn time of candle 2 at the 0.05 significance level?

**Solution:**
The null hypothesis is that the two mean burn times for both brands of candles are the same. Since the question asks if the mean burn time of candle 1 is greater than the mean burn time of candle 2, the hypothesis test is right-tailed. Mathematically,

```math
H0: μ1 = μ2 (null hypothesis)
Ha: μ1 > μ2 (right-tailed test)
Ha: μ1 < μ2 (left-tailed test)
Ha: μ1 ≠ μ2 (two-tailed test)
```

where `μ1` and `μ2` are the mean burn times of candles 1 and 2, respectively.

The level of significance is 0.05. The test statistic is calculated as:

```math
z = (27.5 - 26) / sqrt((2.5^2/100) + (3.5^2/100)) = 1.25
```

The critical value for a right-tailed test at the 0.05 significance level is 1.645. Since the test statistic is less than the critical value, we fail to reject the null hypothesis. There is not sufficient evidence to support the claim that the mean burn time of candle 1 is greater than the mean burn time of candle 2 at the 0.05 significance level.

### Example 2

A factory claims that the proportion of ball bearings with diameter values less than 2.20 cm in the existing manufacturing process is the same as the proportion in the new process. At alpha = 0.05, is there enough evidence to support the factory's claim?

