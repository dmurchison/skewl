# T-Test

Because the population standard deviation is rarely known, the t-test is commonly used to compare the observed sample mean to a hypothesized mean. The following conditions must be met to use the t-distribution.

## Conditions for the T-distribution

1. **Random Sampling**: The sample data must be obtained through a random sampling method.
2. **Independent Sampling**: The sample data must be independent of each other.
3. **Normal Population Distribution**: The population from which the sample is drawn must be normally distributed or the sample size must be sufficiently large (n > 30).

## Procedure for the T-Test

1. **Set Null and Alternative Hypotheses**: Define the null hypothesis Ho and the alternative hypothesis Ha.
2. **Calculate the Test Statistic**: Use statistical software to calculate the t-statistic and the degrees of freedom.
3. **Determine the P-Value**: Calculate the p-value from the t-statistic.
4. **Make a Decision**: If the p-value is less than the significance level, reject the null hypothesis. Otherwise, fail to reject the null hypothesis.

    The scipy.stats.ttest_1samp(a, popmean) function takes in an array or a column of a DataFrame and the hypothesized population mean as inputs and gives the t-statistic and two-tailed p-value as outputs.

### Example

```python
import pandas as pd
import scipy.stats as st
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
print(st.ttest_1samp(scores['Exam1'], 82))
```

Procedure for hypothesis testing two population means using the t-test:

1. **State the null and alternative hypotheses, H0 and Ha.**
    - H0: μ1 = μ2 (null hypothesis)
    - Ha: μ1 ≠ μ2 (two-tailed test)
    - Ha: μ1 > μ2 (right-tailed test)
    - Ha: μ1 < μ2 (left-tailed test)
    - In a test for two population means, the null hypothesis states that the means of the two populations are equal, while the alternative hypothesis states that the means are not equal, greater than, or less than each other.
