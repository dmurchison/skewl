# Coefficient of Multiple Determination

In the simple linear regression chapter, the coefficient of determination was defined as the percent variance in the response variable explained by the predictor variable. A similar quantity called the coefficient of multiple determination exists for models with two or more predictor variables. The **coefficient of multiple determination**, denoted by R2, measures the ratio of total variance in the response variable, Y, that is explained by the predictor variables X1..Xn.

## Adjusted Coefficient of Multiple Determination

The **adjusted coefficient of multiple determination**, denoted by R2adj, is a modified version of the coefficient of multiple determination, R2 that adjusts for the number of predictor variables in the model. The adjusted coefficient of multiple determination is used to compare models with different numbers of predictor variables.

### Finding the adjusted coefficient of determination

#### Question1

Consider a simple case of the body fat model with 1 predictor variable X1=triceps skinfold thickness. The coefficient of determination for this model is
R2=0.711. Find the adjusted coefficient of determination using the formula above given that the sample size is 20.

#### Solution

* The formula for the adjusted coefficient of determination is given by

```math
R_{adj}^2 = 1 - (1-R^2)\left[ \dfrac{N-1}{N-(k+1)}\right]
```

* where n is the sample size and k is the number of predictor variables. In this case, n=20 and p=1. Substituting these values into the formula gives

```math
R_{adj}^2 = 1 - (1-0.711)\left[ \dfrac{20-1}{20-(1+1)}\right] = 0.695
```

* Thus, the adjusted coefficient of determination is 0.695.
