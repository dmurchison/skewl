# The necessary packages are imported
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# The ExamScores dataset is loaded
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Creates a linear regression model
results = ols('Exam4 ~ Exam1', data=scores).fit()

# Creates an analysis of variance table
aov_table = sm.stats.anova_lm(results, typ=2)

# To find the total variance, using the aov table we can find the sum of the squared differences between each data point and the mean of the data set
total_variance = aov_table['sum_sq'].sum()

# The explained variance is the first value in the aov table
explained_variance = aov_table['sum_sq'][0]
print('Explained variance:', explained_variance)

# Coefficient of determination
r_squared = explained_variance / total_variance
print('Coefficient of determination:', r_squared)


print(0.008725/0.01153)
