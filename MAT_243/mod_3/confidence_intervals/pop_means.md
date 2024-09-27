# Confidence Intervals

## Estimation

Estimation is the process of obtaining information about a parameter by using a statistic. An ESTIMATOR is a statistical method used to calculate an estimate based on observable data. A good ESTIMATOR gives estimates that are both accurate and precise. Accuracy is measured in terms of bias. Numerically, bias is the distance between the mean of the sampling distribution and the population mean. Precision is measured in terms of standard error. Numerically, standard error is the standard deviation of the sampling distribution.

**Two types of estimates exist: POINT ESTIMATES and INTERVAL ESTIMATES.**

- A **POINT ESTIMATE** is a single value estimate for a parameter.
- An **INTERVAL ESTIMATE** is a range of values that is likely to contain the parameter being estimated. Combined with a probability    statement, an **INTERVAL ESTIMATE** is called a **CONFIDENCE INTERVAL**. The percentage in which the **CONFIDENCE INTERVAL** contains the parameter is called the **CONFIDENCE LEVEL**, which is denoted by "c".

## Types of Confidence Intervals

A **CONFIDENCE INTERVAL** is accurate if the **CONFIDENCE INTERVAL** contains the true population parameters. A **CONFIDENCE INTERVAL**'s precision refers to the width of the **CONFIDENCE INTERVAL**.

A **CONFIDENCE INTERVAL** is constructed by looking at the sample statistic and margin of error. A margin of error, denoted by
"m", is the range of values above and below the point estimate. Numerically,

    m = (critical_value)(standard_error)

where the critical value, which depends on and the underlying distribution of the statistic, is the number of standard errors to be added to the point estimate. Thus,

    estimate +- m = estimate +- (critical_value)(standard_error)

Where critical_value is the number of standard errors to be added to the point estimate.
and standard_error is the standard deviation of the sampling distribution.

### QUESTION_1

Visit [./confidence_intervals/pop_means_1.py](pop_means_1.py) and complete the following code:
    Suppose the mean final grade is estimated for all introductory statistics classes taught at a particular college.
    The population standard deviation is 4.
    The final grades for a randomly selected statistics class with people are:
    76,80,82,83,83,85,85,87,88
    Find the 0.95 **confidence interval** for the mean final grade.
