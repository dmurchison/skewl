# Testing Multiple Regression Parameters

## Hypthesis Tests for Multiple Regression

In a multiple regression model, if a parameter is zero, then the corresponding predictor is redundant. To keep the model as simple, interpretable, and generalizable as possible, predictors with a regression parameter of zero should be removed.

Consider the model...

```math
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \ldots + \beta_n X_n + \epsilon
```

Two types of hypothesis tests are available to determine whether the estimator is sufficiently close enough to zero to warrant the removal of the corresponding predictor variable.

### Individual Hypothesis Tests

|    Test           |  Research Question                                                                   | Null Hypothesis               | Alternative Hypothesis                |
| ----------------- | ------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------- |
| Overall F-test    |  Determine whether a linear relationship exists with at least one predictor variable | H0: β1 = β2 = ... = βn = 0    | Ha: At least one βi ≠ 0 for i=1,2..,n |
| Individual t-test | Determine whether a single variable has an effect                                    | H0: βi = 0 for some i=1       | Ha: βi ≠ 0                            |
|                   |                                                                                      |                               |                                       |

#### Overall F-test

The overall F-test considers ALL the regression parameters other than the intercept parameter, β0. The **multiple regression overall F-test** is a method for testing H0: β1 = β2 = ... = βn = 0 against Ha: At least one βi ≠ 0 for i=1,2..,n.

##### Steps for Overall F-test

- Set the null hypothesis, H0: β1 = β2 = ... = βn = 0, and the alternative hypothesis, Ha: At least one βi ≠ 0 for i=1,2..,n.
- Use statistical software to find the F-statistic which is the regression mean square divided by the residual mean square.
- Use statistical software to find the p-value associated with the F-statistic. The p-value is the probability of observing an F-statistic at least as far from 0 as the one observed, if the null hypothesis were true.
- Make a decision based on the significance level (α) and the p-value.
  - If the p-value is less than α, reject the null hypothesis. H0: β1 = β2 = ... = βn = 0, in favor of the alternative hypothesis, Ha: At least one βi ≠ 0 for i=1,2..,n. Conclude that at least one, B_k is significantly different from 0.
    - This means that a significant linear relationship exists between Y and the set {X1, X2, ..., Xn}.
  - If the p-value is greater than or equal to α, do not reject the null hypothesis. H0: β1 = β2 = ... = βn = 0, in favor of the alternative hypothesis, Ha: At least one βi ≠ 0 for i=1,2..,n. Conclude that there is not enough evidence to suggest that at least one of the regression parameters is different from 0.
    - This means that there is not enough evidence to suggest that a significant linear relationship exists between Y and the set {X1, X2, ..., Xn}.

```python
                            OLS Regression Results

==============================================================================
Dep. Variable:                      Y   R-squared:                       0.801
Model:                            OLS   Adj. R-squared:                  0.764
Method:                 Least Squares   F-statistic:                     21.52
Date:                Mon, 15 Jul 2019   Prob (F-statistic):           7.34e-06
Time:                        18:46:57   Log-Likelihood:                -44.312
No. Observations:                  20   AIC:                             96.62
Df Residuals:                      16   BIC:                             100.6
Df Model:                           3
Covariance Type:            nonrobust
=================================================================================================

                                    coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------

Intercept                       117.0847     99.782      1.173      0.258     -94.445     328.614
triceps_skinfold_thickness_mm     4.3341      3.016      1.437      0.170      -2.059      10.727
midarm_circumference_cm          -2.1861      1.595     -1.370      0.190      -5.568       1.196
thigh_circumference_cm           -2.8568      2.582     -1.106      0.285      -8.330       2.617
==============================================================================

Omnibus:                        1.200   Durbin-Watson:                   2.243
Prob(Omnibus):                  0.549   Jarque-Bera (JB):                0.830
Skew:                          -0.085   Prob(JB):                        0.660
Kurtosis:                       2.016   Cond. No.                     1.15e+04
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.15e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
```

- Does a linear relationship exist with at least one variable?
  - The null hypothesis is that no relationship exists between any of the predictor variables X1,X2, and X3, and the response variable Y.
    - H0: β1 = β2 = β3 = 0
  - The alternative hypothesis is that a relationship exists with at least one variable.
    - Ha: At least one βi ≠ 0 for i=1,2,3
  - The overall F-test statistic is 21.52 with a p-value of 7.34e-06. Since the p-value is close to 0, sufficient evidence exists to reject the null hypothesis in favor of the alternative hypothesis. This means that at least one of X1, X2, or X3 is linearly related to Y.

#### Individual t-test

An individual t-test considers one of the regression parameters. A **multiple regression individual t-test** is a method for testing H0: βi = 0 against Ha: βi ≠ 0 for some i=1,2..,n. Ex. The body fat example has three regression parameters other than the intercept parameter. One individual t-test could test H0: β1 = 0. Other t-tests could be H0: β2 = 0 or H0: β3 = 0.

##### Steps for Individual t-test

- Set the null hypothesis, H0: βi = 0, and the alternative hypothesis, Ha: βi ≠ 0.
- Use statistical software to find the t-statistic which is b_i divided by the standard error of b_i.
- Use statistical software to find the p-value associated with the t-statistic. The p-value is the probability of observing a t-statistic at least as far from 0 as the one observed, if the null hypothesis were true. The reference t-distribution has n-p degrees of freedom.
- Make a decision based on the significance level (α) and the p-value.
  - If the p-value is less than α, reject the null hypothesis. H0: βi = 0, in favor of the alternative hypothesis, Ha: βi ≠ 0. Conclude that βi is significantly different from 0.
    - This means that a significant linear relationship exists between Y and X_i when the remaining predictor variables in the model are fixed.
  - If the p-value is greater than or equal to α, do not reject the null hypothesis. H0: βi = 0, in favor of the alternative hypothesis, Ha: βi ≠ 0. Conclude that there is not enough evidence to suggest that βi is different from 0.
    - This means that there is not enough evidence to suggest that a significant linear relationship exists between Y and X_i when the remaining predictor variables in the model are fixed. Thus, a new model should be investigated in which X_i is removed from the model but the remaining predictor variables are retained.

```python
                            OLS Regression Results
==============================================================================
Dep. Variable:                      Y   R-squared:                       0.786
Model:                            OLS   Adj. R-squared:                  0.761
Method:                 Least Squares   F-statistic:                     31.25
Date:                Tue, 16 Jul 2019   Prob (F-statistic):           2.02e-06
Time:                        00:12:50   Log-Likelihood:                -45.050
No. Observations:                  20   AIC:                             96.10
Df Residuals:                      17   BIC:                             99.09
Df Model:                           2
Covariance Type:            nonrobust
=================================================================================================
                                    coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------
Intercept                         6.7916      4.488      1.513      0.149      -2.678      16.261
triceps_skinfold_thickness_mm     1.0006      0.128      7.803      0.000       0.730       1.271
midarm_circumference_cm          -0.4314      0.177     -2.443      0.026      -0.804      -0.059
==============================================================================
Omnibus:                        1.363   Durbin-Watson:                   2.371
Prob(Omnibus):                  0.506   Jarque-Bera (JB):                0.873
Skew:                           0.068   Prob(JB):                        0.646
Kurtosis:                       1.985   Cond. No.                         304.
```

- **Does midarm circumference have a statistically significant effect on percent body fat according to the output**
  - The null hypothesis is that no relationship exists between the predictor variable X1 and the response variable Y.
    - H0: β1 = 0
  - The alternative hypothesis is that a relationship exists.
    - Ha: β1 ≠ 0
  - The individual t-test statistic for the midarm circumference is -2.443 with a p-value of 0.026. Since the p-value is less than 0.05, sufficient evidence exists to reject the null hypothesis in favor of the alternative hypothesis. This means that the midarm circumference is linearly related to Y when the triceps skinfold thickness is fixed.

