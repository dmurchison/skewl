# Multiple Regression Assumptions and Diagnostics

## Assumptions of Multiple Regression

A multiple regression model is considered valid only if the following assumptions can be made about the population. Since population regression errors are not observable, the sample residuals \(e_i = Y_i - \hat{Y}_i\) are used to determine whether each assumption is violated.

* **Mean of zero:** The mean of each residual for each set of values for the predictor variables is zero. Equivalently, this assumption says that the response variable is a linear function of each of the predictor variables.
* **Independence:** The residuals are independent. This condition can be difficult to assess. A common way to determine independence is by plotting residuals with respect to the time in which the data is collected. If a trend exists, then the independence assumption is potentially violated.
* **Normality:** The residuals of each set of values for the predictor variables form a normal distribution. If the plotted points lie reasonably close to the diagonal line on the plot then one can conclude that the normality assumption holds.
* **Constant variance:** The residuals of each set of values for the predictor variables should have equal or similar variance. A common term for this condition is homoscedasticity. If the variance does not remain constant throughout the plot, then the model exhibits heteroscedasticity.

## Assessing Regression Assumptions

* Mean of zero assumption: The mean of the residuals should be approximately zero for each fixed value on the horizontal axis, i.e., no strong trends.
  * Any clear linear or nonlinear trend indicates the mean of zero assumption may not hold. Ex: A strong nonlinear rising-falling trend indicates the assumption does not hold.
* Constant variance assumption: The variance of the residuals should be approximately constant for each fixed value on the horizontal axis, i.e., like a horizontal band.
  * Any clear change in variability indicates the constant variance assumption may not hold. Ex: A strong funnel pattern indicates the assumption does not hold.
  * An outlier is an observation with an extreme residual, which appears as an isolated point at the top or bottom of a residual plot.
* Independence assumption: the value of one error should be independent of the value of any other error. Ex: No patterns in a plot of residuals versus time should exist.
  * A strong relationship between one residual and the next indicates the independence assumption may not hold. Ex: Residuals that closely follow one another.
* Normality assumption: the errors are assumed to be normally distributed, which is assessed using a normal probability plot of the residuals, not a residual scatterplot.

### Validate Multiple Regression Assumptions

* Residual plots can be used to visually evaluate the assumptions of linearity and homoscedasticity.
  * A residual plot with a non-linear shape (u or n shape) suggests violation of the linearity assumption.
  * A residual plot with a fan-shaped distribution of data points suggests that some data points have a smaller variance than others. Since the variance is not constant, such a plot suggests violation of the homoscedasticity assumption.

* **Homoscedasticity:** The residuals have constant variance across all levels of the predictor variables. The residuals are equally spread across the range of the predictor variables.
* **Heteroscedasticity:** The residuals have non-constant variance across the range of the predictor variables. The residuals are not equally spread across the range of the predictor variables.
* **Linearity:** The relationship between the response variable and the predictor variables is linear. The residuals should be randomly scattered around the horizontal axis.
* **Nonlinearity:** The relationship between the response variable and the predictor variables is not linear. The residuals should not be randomly scattered around the horizontal axis.

#### Q-Q Plot

* A **Q-Q plot** is a graphical method for comparing two probability distributions by plotting their quantiles against each other. The Q-Q plot is used to determine if the residuals are normally distributed. If the residuals are normally distributed, the points on the Q-Q plot will fall approximately along a straight line.

## Care in Assessing Multiple Regression Assumptions

Care must be taken when checking the multiple regression assumptions graphically:

* Assessing whether a particular plot supports an assumption is subjective. One should question an assumption when a clear non-random pattern exists in a plot, but not be overly concerned with weak patterns.
* Checking assumptions graphically requires a reasonably large sample size, typically at least 30.
* Ideally, all four assumptions should hold for a model to be valid.
* That said, multiple regression models are reasonably robust to mild violations of the assumptions.
* Severe violations of the assumptions can be addressed through more complex models, some of which are considered in a later section.

## Issues with multiple regression models

Individual data observations can have a relatively strong influence on multiple regression models because of the presence of outliers and high-leverage observations.

An **outlier** is an observation in a multiple regression analysis that has an extreme residual. For an outlier to be extreme, the observation's Y value is either much larger than predicted by the model or much smaller than predicted by the model.

A **high leverage observation** is an observation in a multiple regression analysis that has an extreme combination of predictor values. An extreme combination of values might be particularly high or low values for all the predictors or a combination of predictor values that is relatively unusual. A high leverage observation has the potential to be highly influential on the results of the multiple regression analysis.

Another potential problem is the presence of multicollinearity. **Multicollinearity** occurs when two or more predictors in a multiple regression model are so highly correlated that the estimated model becomes unstable meaning that the regression parameter estimates become unreliable with inflated standard errors. Interpreting a multiple regression model in the presence of multicollinearity can be challenging. However, estimation and prediction for a multiple regression model in the presence of multicollinearity is relatively unaffected.
