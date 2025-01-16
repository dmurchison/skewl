import pandas as pd
import statsmodels.formula.api as smf
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

model = smf.ols('Exam4 ~ Exam2', scores).fit()
print(model.summary())


# The ExamScores dataset is a record of 4 exam scores for 50 students.
# Y=Exam4 is the response variable and X=Exam2 is the predictor variable.
# The teacher believes that a linear relationship exists between Exam4 scores and Exam2 scores.
# Does sufficient evidence exist to support the teacher's claim at the
# alpha=0.05 significance level?

# First set the null and alternative hypotheses:

# Ho = "There is no linear relationship between Exam4 scores and Exam2 scores."
# Ho = B1 = 0
# Ha = "There is a linear relationship between Exam4 scores and Exam2 scores."
# Ha = B1 != 0

# Determine what type of test to perform:

# The teacher believes that a linear relationship exists between Exam4 scores and Exam2 scores.
# This is a two-tailed test because the teacher is interested in determining if a relationship exists in either direction.

# Find the p-value and the t-statistic using the OLS model:
p_value = model.pvalues['Exam2']
t_statistic = model.tvalues['Exam2']

print('p-value:', p_value)
print('t-statistic:', t_statistic)

if p_value < 0.05:
    print('Reject the null hypothesis.')
else:
    print('Fail to reject the null hypothesis.')

# To find the area under the probability curve, or the other tail in a two-tailed test, subtract the p-value of the intercept from 1:
p_value_intercept = 1 - model.pvalues['Intercept']
print('p-value for intercept:', p_value_intercept)

# The confidence interval for the slope coefficient is given by the model's conf_int() method:
conf_int = model.conf_int().loc['Exam2']


# To find the degrees of freedom, subtract the number of predictors from the number of observations:
df = model.df_resid
print('Degrees of freedom:', df)

# The predictor variable, denoted by X
# The response variable, denoted by Y
