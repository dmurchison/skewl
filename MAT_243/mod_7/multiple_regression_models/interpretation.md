# Interpreting Multiple Regression Models

## Interpreting Multiple Regression Parameters

For the function...

```math
\hat{Y} = b_0 + b_1 X_1 + b_2 X_2 + \ldots + b_n X_n
```

...the parameters are interpreted as follows:

- `b_0` is the `Y`-intercept of a sample multiple regression function.
Which is fitted value of `Y` when...

```math
X_1 = X_2 = \ldots = X_n = 0
```

- `b_1,b_2,...b_n` each represent the slope with respect to a particular predictor variable of a sample multiple
regression function.

A consideration when constructing multiple regression models is *multicollinearity*, which occurs when two or more
predictors in the model are so highly correlated that regression parameter estimates become unreliable with inflated
standard errors. Interpreting a regression parameter in the presence of *multicollinearity* can be challenging and is
beyond the scope of this material.

### Example

For a multiple regression function...

```math
\hat{Y} = 6.792 + 1.001 X_1 - 0.431 X_2
```

1. What is the estimate for the intercept parameter?
    - The estimate for the intercept parameter is `6.792`. However, this value is not meaningful in this context because
    the predictor variables are not centered. The intercept parameter is the estimated value of `Y` when `X_1 = X_2 = 0`.
2. What is the estimate for the slope parameter with respect to `X_1`?
    - The estimate for the slope parameter with respect to `X_1` is `1.001`. This value represents the change in the
    estimated value of `Y` for a one-unit change in `X_1`, holding all other predictor variables constant.

#### Analysis

- If the `b_1` and `b_2` are too highly correlated, then increasing `X_1` by one unit, and keeping `X_2` fixed, might be
impractical. This difficulty in interpreting regression parameters in the presence of multicollinearity means that
multicollinearity is generally avoided when parameter interpretation is important for the application at hand.

##### Bonus Questions

1. What is the estimated slope with respect to `X_2`?
    - The estimated slope with respect to `X_2` is `-0.431`. This value represents the change in the estimated value
    of `Y` for a one-unit change in `X_2`, holding all other predictor variables constant.
2. What is the interpretation of `-0.431` in the sample regression function?
    - The interpretation of `-0.431` is that for each one-unit increase in `X_2`, the estimated value of `Y` decreases
    by `0.431`, holding all other predictor variables constant.
    - The change in the fitted value of `Y` for a one-unit change in `X_2` when `X_1` is fixed.

### Python-Practice Multiple Regression Models

**Visit [Python-Page](./mrm.ipynb) to practice interpreting multiple regression models using Python.**

## Interpreting Residual Standard Error

- As with simple linear models, several quantities in multiple regression models use the residuals.

  ```math
  \text{Actual Response Value: } Y_i \newline
  \text{Fitted Response Value: } \hat{Y}_i \newline
  \text{Sample Mean of Response Values: } \overline{Y} \newline
  \text{Residual Standard Error: } e_i = Y_i - \hat{Y}_i \newline
  - \newline
  - \newline
  \text{Quantities:} \newline
  \text{Regression Sum of Squares: } SSR = \sum_{i=1}^{N} (\hat{Y}_i - \overline{Y})^2 \newline
  - \newline
  \text{Residual Sum of Squares: } SSE = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2 \newline
  - \newline
  \text{Total Sum of Squares: } SSTO = \sum_{i=1}^{N} (Y_i - \overline{Y})^2
  ```

- Intuitively, the magnitude of the residuals indicate the strength of the model. The closer the residuals are to zero, the more effective the model is in predicting the values of the dependent variable. Since residuals can be positive or negative and the mean of the residuals is zero, computing the square root of the mean squared residual is sometimes more useful.
- The residual mean square error (residual standard error), denoted by RMSE, is the square root of the mean squared residual, which estimates the standard deviation of the residuals. The residual standard error is obtained using the formula

  ```math
  \text{Residual Mean Square Error: } RMSE = \sqrt{MSE} = \sqrt{\dfrac{SSE}{N-p}}
  ```

  where:
  - `N` is the number of observations
  - `k` is the number of predictor variables in the model.
- The measurement unit of the residual standard error is the same as the measurement unit of the response `Y` variable. The residual standard error is a measure of the precision of a model prediction. The sample multiple regression function can be used to predict a future value of `Y` for fixed values of `X_1,X_2,..X_n`. A relatively small residual standard error indicates that the actual future value of `Y` is likely to be relatively close to the predicted value. Therefore, less residual standard error is better.

### Analysis of Variance Table

See [Python-Page](./mrm.ipynb) for an example of how to obtain the mean standard error and standard residual error using an analysis of variance table.

The mean standard error and standard residual error can be obtained using an analysis of variance table. Consider the body fat dataset and a model where the response variable
 is percent body fat and the two predictor variables are
 is triceps skinfold thickness (mm) and
 midarm circumference (cm).
