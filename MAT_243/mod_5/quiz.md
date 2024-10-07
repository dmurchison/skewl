# Python Functions Quiz

## Question 1

How can we figure out what the correct regression equation to use, based on a model summary from the ols function?
How can we figure out if the model is significant?

## Answer 1

The regression equation is given by the coefficients of the independent variables. The model is significant if the p-value of the F-statistic is less than 0.05 To get the p-value of the F-statistic, we can use the `f_pvalue` attribute of the model summary.

The different types of regression equations are:

- Simple linear regression: y = mx + b
- Multiple linear regression: y = m1x1 + m2x2 + ... + b

## Question 2

The height and gpa of 50 random people were recorded. Does this instance have a reponse variable and predictor variable? If so, what are they?

## Answer 2

No, these would both be considered response variables. A response variable is the variable that is being predicted or explained by the predictor variable(s). In this case, the height and GPA are both being measured and are not being used to predict anything.

## Question 3

Does the corr function perform simple linear regression?

## Answer 3


