# Introduction to Simple Linear Regression (SLR)

## Regression Lines

A **simple linear regression** is a way to model the linear relationship between two quantitative variables, using a line drawn through those variables' data points, known as a **regression line**.

    Ex: The animation below shows a scatterplot with several data points that represent house price and house size for 5 houses in Eugene, Oregon (Source: Victoria Whitman's 2005 house sales), with a regression line drawn through the points. A common use of a regression line is to make predictions.

- Method of Least Squares: The regression line is calculated using the method of least squares, which minimizes the sum of the squared differences between the observed values and the predicted values.

- Sample Simple Linear Regression Function: The sample simple linear regression function is given by the equation: y = b0 + b1x, where y is the dependent variable, x is the independent variable, b0 is the y-intercept, and b1 is the slope of the line.

- Simple Linear Regression Fitted Value: The fitted value for a given x value is the predicted value of y on the regression line.

- Simple Linear Regression Residual: The residual is the difference between the observed value of y and the fitted value of y for a given x value.

## Python Code for Simple Linear Regression

The `linregress(x,y)` function from the `scipy.stats` module in Python can be used to perform simple linear regression. The function returns the slope, intercept, correlation coefficient, p-value, and standard error of the regression.
Ex: The code snippet below demonstrates how to use the `linregress(x,y)` function to perform simple linear regression on house price and house size data.

```python
# The numpy library is imported to build two arrays
import numpy as np
import scipy.stats as st

x = np.array([0, 3, 7, 10])
y = np.array([5, 5, 27, 31])

print(st.linregress(x,y))
```

The output of the code snippet will display the slope, intercept, correlation coefficient, p-value, and standard error of the regression.

## Conclusion

Simple linear regression is a powerful tool for modeling the relationship between two quantitative variables. By fitting a regression line to the data, we can make predictions and understand the strength and direction of the relationship between the variables.
