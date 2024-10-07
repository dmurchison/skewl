# Correlation and Coefficient of Determination

## Correlation

**Correlation** describes the association or dependence between two variables. A positive correlation between two variables means that as one variable increases, the other variable increases as well. A negative correlation between two variables means that as one variable increases, the other variable decreases. The strength of correlation between a predictor variable and a response variable can be measured by the correlation coefficient. The population correlation coefficient is denoted by p and the sample correlation coefficient is denoted by R.

The strength of correlation can be described by the absolute value of R. The table below gives a rough guideline.

| Strength of Correlation | Absolute Value of R |
|-------------------------|---------------------|
| Weak                    | 0.1 - 0.3           |
| Moderate                | 0.3 - 0.5           |
| Strong                  | 0.5 - 1.0           |

## Correlation Matrix

Often, applications deal with more than one variable. A correlation matrix is a table that shows the correlation coefficients between each pair of variables. A correlation matrix for a collection of n variables X1...Xn is an NxN matrix where the ijth entry is the correlation coefficient of Xi and Xj. Note that the diagonal entries are always 1 because the correlation between a variable and itself is 1. Further, the correlation matrix is symmetric. That is, the ijth entry is the same as the jith entry.

### Corr() Function in Python

The correlation function DataFrame.corr() calculates the pairwise correlation of the columns in the dataframe and outputs a correlation matrix.

The code below uses the Exam1 and Exam2 columns of the ExamScore dataset and produces a 2x2 correlation matrix.

The code below uses the Exam1, Exam2, Exam3, and Exam4 columns of the ExamScore dataset and produces a 4x4 correlation matrix.

```python
import pandas as pd
scores = pd.read_csv("ExamScores.csv")
print(scores[['Exam1','Exam2']].corr())
print(scores[['Exam1','Exam2','Exam3','Exam4']].corr())
```
