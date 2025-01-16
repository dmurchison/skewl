# The

import pandas as pd
import statsmodels.formula.api as sms

fat = pd.read_csv('https://static-resources.zybooks.com/static/fat.csv')

# Response variable
Y = fat['body_fat_percent']

# Generates the linear regression model
# Multiple predictor variables are joined with +
model = sms.ols('Y ~ triceps_skinfold_thickness_mm + midarm_circumference_cm + thigh_circumference_cm', data = fat).fit()

# Prints the summary
print(model.summary())

# The values in the coef column in the output correspond to the B population regression parameters of the multiple regression model.
# The Intercept coef is B0. The subsequent entries in the coef column correspond to B coefficients of each predictor variable in the order entered in the ols() function.
# So to find the sample regression equation, we can plug in the values of the coefficients into the equation: Y = B0 + B1X1 + B2X2 + B3X3
# where B0 is the Intercept, B1 is the coefficient of triceps_skinfold_thickness_mm, B2 is the coefficient of midarm_circumference_cm, and B3 is the coefficient of thigh_circumference_cm.
# The sample regression equation is: Y = -27.5 + 0.22(triceps_skinfold_thickness_mm) + 0.23(midarm_circumference_cm) + 0.24(thigh_circumference_cm).

#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      0.5382      0.473      1.137      0.273      -0.471       1.547
# Speed         -1.9046      0.176    -10.834      0.000      -2.279      -1.530
# Angle          4.0280      0.178     22.574      0.000       3.648       4.408

X1 = 5
X2 = 6

Y = 0.5382 + (-1.9046 * X1) + (4.0280 * X2)
print(Y)


x = (384.279719 + 111.109781)
print(x)

x_ = 37.1016 + (-3.9248 *  2.78) + (-0.0320 * 225)
print(x_)

# The residual is if the actual value is 18. and the predicted value is 19.30
residual = 18 - x_
print(residual)
