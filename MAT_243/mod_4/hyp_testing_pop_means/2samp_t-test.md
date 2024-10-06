# Two-sample t-test

The t-test discussed analyzes the difference between the sample mean and the hypothesized value of the population mean. A similar method exists to compare the means of two different populations. The **two-sample t-test** is used to determine if a statistically significant difference exists between two population means. Two types of two-sample t-tests exist: paired and unpaired.

In a **paired t-test** or **dependent t-test**, a sample taken from one population is exposed to two different treatments. The main idea is that measurements are recorded from the same group, usually before and after a treatment is applied or when each of two treatments is applied. Ex: A group of professional cycling athletes is selected for a study on the effects of caffeine dosage on exhaustion times. The populations are the cyclists for each of two dosages. The samples are the measured exhaustion times for each dosage, which implies dependence because the measurements were taken from the same group.

In an **unpaired t-test** or **independent t-test**, a sample taken from one population is not related to a different sample taken from another population. In contrast to the paired t-test, measurements from an unpaired t-test are recorded from different groups when exposed to the same treatment. Ex: The effect of caffeine intake on exhaustion times is studied by measuring the exhaustion times of a randomly selected group of 9professional cyclists taking caffeine pills and another group of 9 cyclists not taking caffeine pills. The two populations are all cyclists taking caffeine pills and those who are not taking the pills. The samples are the measured exhaustion times from the two groups, each with 9 cyclists, which implies independence because the times are for two different groups of cyclists.

## Identifying the Type of t-test

1. A study involving children from a preschool compares the median times to recite words with two and three syllables.

    - **Paired t-test**: The same group of children is tested for reciting words with two and three syllables.

2. A study involving children from a preschool compares the median times to recite words with two and three syllables with children from a different preschool.

    - **Unpaired t-test**: The children from one preschool are tested for reciting words with two syllables, and the children from a different preschool are tested for reciting words with three syllables.

## Paired t-test

To obtain probabilities for a paired t-test, the paired t-statistic is needed. The formula involves finding the mean and standard deviation of the differences between corresponding measurements :

```math
t = \dfrac{\overline{d} - \mu_d}{\frac{s_d}{\sqrt{n}}}
```

where:
s_d = standard deviation of the differences
\overline{d} = mean difference between the two samples
n = sample size

The most common scenario is that the hypothesized mean difference is 0. However, this scenario is not necessary. Ex: To continue the development of a new drug, a measurable improvement in the condition of the subjects must be seen. In this situation, the null hypothesis would be that the mean difference is the minimum amount of improvement set by the manufacturer in order to continue developing the drug. The differences are assumed to come from a normal distribution. Thus, the differences can be seen as a single sample following a t-distribution, which means that a paired t-test is equivalent to a one-sample
t-test.

### Procedure for Hypothesis Testing for Paired t-test

Given two randomly selected samples of size n taken from each of two populations with unknown population standard deviation o,

1. Set the null and alternative hypotheses, H0 and Ha.

      ```math
      \begin{align}
      H_0: \mu_d &= 0\\
      H_a: \mu_d &> 0 \hspace{1pc} \text{ (right-tailed)}\\
      H_a: \mu_d &< 0 \hspace{1pc} \text{ (left-tailed)}\\
      H_a: \mu_d &\neq 0 \hspace{1pc} \text{ (two-tailed)}
      \end{align}
      ```

      where:
      \mu_d = mean difference between the two samples

2. Use statistical software to calculate the test statistic, t. and the degrees of freedom, df.

    ```math
    t = \displaystyle\frac{\overline{d} - \mu_d}{\frac{s_d}{\sqrt{n}}}

    df = n - 1
    ```

    where:
    \overline{d} = mean difference between the two samples
    s_d = standard deviation of the differences
    n = sample size

3. Determine the critical value, t_{\alpha/2}, or p-value.

    ```python
    from scipy.stats import t

    # Find the critical value
    t.ppf(1 - \alpha/2, df)
    ```

4. Make a decision to reject or fail to reject the null hypothesis.

    - If the p-value is less than the popular significance levels 0.05, 0.1, reject the null hypothesis.
    - If the p-value is greater than the popular significance levels 0.05, 0.1, fail to reject the null hypothesis.
    - **NOTE:** A small p-value indicates that the null hypothesis is unlikely to be true, or SHOULD be rejected.

### Paired t-test python

The st.ttest_rel(x, y) function takes two arrays or DataFrame columns x and y with the same length as inputs and returns the t-statistic and the corresponding two-tailed p-value as outputs.

The code below loads the exam scores data and uses a paired t-test for the hypotheses H0: ud = 0 and Ha: ud ≠ 0, where ud is the average difference in students' exam 1 and exam 2 scores.

```python
import scipy.stats as st
import pandas as pd
df = pd.read_csv('ExamScores.csv')
print(st.ttest_rel(df['Exam1'],df['Exam2']))
```

## Unpaired t-test

The unpaired t-test is used to determine if a statistically significant difference exists between two population means. The formula for the unpaired t-test is:

```math
t = \dfrac{\overline{x}_1 - \overline{x}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}
```

where:
\overline{x}_1 and \overline{x}_2 = sample means of the two populations
s_1 and s_2 = standard deviations of the two populations

The degrees of freedom are the sum of the degrees of freedom of each population. The critical value is found using the degrees of freedom and the desired level of significance.

To find the test statistic for an unpaired two-tailed t-test, in python use the following code:

```python
import scipy.stats as st
import pandas as pd
df = pd.read_csv('data.csv')
print(st.ttest_ind(df['Group1'],df['Group2']))
```

If we are given the sample means, and population standard deviations, we can calculate the test statistic as follows:

```python
import numpy as np
x1 = 119
x2 = 118
s1 = 1
s2 = 5
n1 = 100
n2 = 100

t = (x1 - x2) / np.sqrt((s1**2/n1) + (s2**2/n2))
print(t)
```

To find the test statistic for a two-tailed z-test, when the population standard deviations are known, use the following code:

```python
import numpy as np
mean1 = 123
mean2 = 122
std_dev1 = 1
std_dev2 = 5
n1 = 107
n2 = 107

z = (mean1 - mean2) / np.sqrt((std_dev1**2/n1) + (std_dev2**2/n2))
print(z)
```

