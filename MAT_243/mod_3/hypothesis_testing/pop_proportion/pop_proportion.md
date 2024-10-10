# Hypothesis test for a Population Proportion

A hypothesis test for a population proportion is a statistical test used to determine whether a population proportion is equal to a hypothesized value. The test compares the sample proportion to the hypothesized proportion and determines whether the difference between the two is statistically significant.

The z-test can also be used to determine whether the population proportion is the same as the hypothesized proportion Po. When performing a hypothesis test involving the proportion of a single population.

- **Distribution of the z-test statistic**

  ```math
  N(Po, sqrt(Po(1-Po)/n))
  ```

## Conditions and Procedure for the Z-Test for Population Proportion

**Normality Condition** is the most important condition for the z-test for population proportion. The sample proportion must be approximately normally distributed. The normality condition is satisfied when the sample size is sufficiently large, typically when np >= 5 and n(1-p) >= 5.

### Given a randomly selected sample taken from a population

- 1 **Set the Null and Alternative Hypotheses**: Define the null hypothesis Ho and the alternative hypothesis Ha. Ho: p = Po and Ha: p != Po, p < Po, or p > Po. where p is the sample proportion and Po is the hypothesized population proportion.
- 2 **Calculate the Test Statistic**: Calculate the z-statistic from the sample data.

  ```py
  z = (p - Po) / sqrt(Po(1-Po)/n)
  ```

- 3 **Determine the P-Value**: Calculate the p-value from the z-statistic.

  ```py
  p = norm.cdf(z)
  ```

- 4 **Make a Decision**: Compare the p-value to the significance level alpha to determine whether to reject the null hypothesis.
  - If p-value < alpha, reject the null hypothesis.
  - If p-value >= alpha, fail to reject the null hypothesis.

### Example

The human sex ratio is the ratio of the number of males to the number of females within a certain age group. According to a 2002 study on sex ratios1, the expected ratio of males to females is 106 to 100 or 0.515. Because of cultural norms and national health policies, some nations may have a much higher or much lower sex ratio. In a random sample of 189 people, 85 people are males. Does sufficient evidence exist that the sex ratio of males to females in the population is different than expected at the a=0.05 significance level?

**Solution:**

Since the dataset contains binary categorical data, the hypothesis test involves population proportion rather than population mean.
The null hypothesis is that the sex ratio of males to females 0.515. Since the question asks if the ratio is different, the hypothesis test is two tailed with an alternative hypothesis that sex ratio of males to females is NOT 0.515. Mathematically, Ho: p = 0.515 and Ha: p != 0.515.

85 of the 189 people are males, so the sample proportion is p = 85/189 = 0.450. The sample size is n=189. Since Po=0.515, the z-statistic is calculated as follows:

```python
import math

# Calculate the z-statistic
z_stat = (0.45 - 0.515) / math.sqrt(0.515 * (1 - 0.515) / 189)
print("Z Statistic: ", z_stat)
# Output: Z Statistic: -1.788
```

The p-value is calculated using statistical software, as long as we have the variables for the z-statistic and the sample size,
like so:

```python
import math
import scipy.stats as st

# Calculate the z-statistic
z_stat = (0.45 - 0.515) / math.sqrt(0.515 * (1 - 0.515) / 189)
print("Z Statistic: ", z_stat)
# Output: Z Statistic: -1.788

# Calculate the p-value
# Since this is a two-tailed test, we need to multiply the p-value by 2
p_value = 2 * st.norm.cdf(z_stat)
print("P Value: ", p_value)
# Output: P Value: 0.074
```

**Analysis:** Since the p-value is greater than the significance level a=0.05, insufficient evidence exists to support the hypothesis that the population sex ratio of this specific age group is different than the expected ratio of 0.515.

### Python Functions for Z-Test for Population Proportion

The proportions_ztest(count, nobs, value, prop_var = value) function is used to perform a one-sample z-test for proportions. The function requires the statsmodels.stats.proportion library to be imported, and takes four inputs. The first input count is the number of observations meeting some condition, the second input nobs is the total number of observations, the third input is the hypothesized value of the population proportion, and the fourth is the hypothesized value of the population proportion which is used to calculate the variance of the estimate.

```python
from statsmodels.stats.proportion import proportions_ztest
counts = 31
nobs = 50
value = 0.50
print(proportions_ztest(counts, nobs, value, prop_var = value))
# Output: (1.697056274847714, 0.08968602177036457)
```

the Knicks scored just above, just below, or equal to 100 points, about 35 times would be an example of a one-sample z-test for proportions. The null hypothesis would be that the proportion of times the Knicks scored 100 points is 0.50, and the alternative hypothesis would be that the proportion is not 0.50. The p-value of 0.0897 is greater than the significance level of 0.05, so there is insufficient evidence to reject the null hypothesis that the proportion of times the Knicks scored 100 points is 0.50.
