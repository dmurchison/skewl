# One Way Analysis of Variance (One-Way ANOVA)

## Comparing three or more populations

The unpaired t-test determines whether a statistically significant difference exists between the means of two populations. However, many situations require that means be compared among three or more populations. Ex: A researcher wants to classify iris species based on sepal length by using a method called k-means clustering. As a first step, the researcher checks whether the mean sepal length differs among three species of iris: *setosa*, *virginica*, and versicolor. A possible method to compare the means is to perform three unpaired t-tests: one between *setosa* and *versicolor*, another between *setosa* and *virginica*, and finally between versicolor and *virginica*. Although the details are beyond the scope of the material, the probability of rejecting the null hypothesis that no significant difference in population means exists, when using multiple t-tests is 14%. Thus, a different approach is needed.

One-way analysis of variance (one-way ANOVA) controls for the errors associated with comparing multiple population means. **One-way analysis of variance (one-way ANOVA)** determines whether a statistically significant difference exists among the means of three or more populations. Equivalently, ANOVA tests for an association between a categorical predictor variable and a response variable. Ex: In the iris study, the predictor variable is the type of species and the response variable is sepal length. Data scientists and statisticians often refer to a categorical predictor variable as a factor and a possible value of a factor as a level. A factor can be a continuous variable partitioned into intervals commonly referred to as bins. Ex: The factor in the iris example, iris type, has three levels: setosa, virginica, and versicolor. If the factor only has two levels, then ANOVA is equivalent to a two-sample
-test with equal variances.

### Assumptions

- Independence. Samples should be independent and drawn randomly.
- Normality. The underlying distribution of the populations from which the samples are drawn should be approximately normal.
- Homogeneity. The variances of the population distributions should be equal.

### Procedure

Given `k` groups taken from independent populations,

1. Set the null and alternative hypotheses:
    - Null hypothesis: The means of the `k` populations are equal.
    - Alternative hypothesis: At least one population mean is different from the others.

    ```math
    H_0: \mu_1 = \mu_2 = \ldots = \mu_k \newline
    H_a: \mu_i \neq \mu_j \text{ for some } i \neq j
    ```

2. Use statistical software to calculate the test statistic.

    ```math
    F = \frac{MS_{\text{between group variance}}}{MS_{\text{within group variance}}}
    ```

3. Use statistical software to find the p_value that corresponds to F

4. Make a decision:
    - If the p_value is less than the significance level, reject the null hypothesis.
    - If the p_value is greater than the significance level, fail to reject the null hypothesis.

#### Python Practice ANOVA

The f_oneway() function performs a one-way ANOVA. The function takes a number of lists of data as parameters, and returns the F-statistic and the P-value. The scipy.stats and statsmodels.formula.api libraries must be imported to use f_oneway().

```python
# The Exam Score dataset includes scores obtained in 4 exams in a class.
# Perform a hypothesis test to determine if the mean scores of the exams
# are different. Use the 5% level of significance.

import pandas as pd
import scipy.stats as st
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Statistics of each exam
exam1_score = scores[['Exam1']]
exam2_score = scores[['Exam2']]
exam3_score = scores[['Exam3']]
exam4_score = scores[['Exam4']]

print(st.f_oneway(exam1_score, exam2_score, exam3_score, exam4_score))
```

If the data is labeled according to group, ols() can also be used to generate an ANOVA table, which also gives the F-statistic and the corresponding P-value.

```python
import statsmodels.api as sm
import pandas as pd
from statsmodels.formula.api import ols
df = pd.read_csv('http://data-analytics.zybooks.com/ExamScoresGrouped.csv')
mod = ols('Scores ~ Exam',data=df).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)
```

Generate the boxplots.

```python
import pandas as pd
import seaborn as sns
df = pd.read_csv('http://data-analytics.zybooks.com/ExamScoresGrouped.csv')
sns.boxplot(x="Exam", y="Scores", data=df)
```
