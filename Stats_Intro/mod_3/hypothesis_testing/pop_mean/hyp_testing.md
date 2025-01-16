# Hypothesis Testing

A hypothesis is a proposed explanation of a phenomenon, usually as a starting point for further analysis. Ex: If a lamp doesn't illuminate when turned on, one hypothesis is: "Lamp is not plugged in". Subsequent analysis may result in rejecting the hypothesis. Ex: Observing the lamp is indeed plugged into an electric outlet causes one to reject the "Lamp is not plugged in" hypothesis.

## Null and Alternative Hypotheses

In statistics, a hypothesis is a statement that makes a claim about the parameters of one or more populations. Hypothesis testing is the formal process by which a hypothesis is retained or rejected. Hypothesis testing compares two competing hypotheses about a population, the **Null Hypothesis** and the **Alternative Hypothesis**.

A **Null Hypothesis**, denoted "Ho", is a statement assumed to be true unless sufficient data indicates otherwise. Typically, a **Null Hypothesis** is a statement of equality between the true value of the population parameter and the hypothesized value or a statement of no difference between the parameters of two populations. Ex: The statement "The average salary of the residents of San Francisco is not different than the average salary of the residents of Austin" or "The average salary of the residents of San Francisco is the same as the average salary of the residents of Austin" is a **Null Hypothesis**.

In contrast, an **Alternative Hypothesis**, denoted "Ha", is a statement that contradicts "Ho". Typically, an **Alternative Hypothesis** asserts that the true value of the population parameter is not the same as the hypothesized value or that the parameters for two populations are different. Ex: The **Alternative Hypothesis** corresponding to the **Null Hypothesis** above is "The average salary of the residents of San Francisco is different from the average salary of the residents of Austin, Texas."

An **Alternative Hypothesis** may be **left-tailed**, **right-tailed**, or **two-tailed** depending on the nature of the difference from the **Null Hypothesis**.

### Types of Alternative Hypotheses

A **left-tailed** **Alternative Hypothesis** asserts that the value of a parameter is less than the value asserted in the **Null Hypothesis**.
A **right-tailed** **Alternative Hypothesis** asserts that the value of a parameter is greater than the value asserted in the **Null Hypothesis**.
A **two-tailed** **Alternative Hypothesis** asserts that the value of a parameter is not equal to, that is, either less than or greater than the value asserted in the **Null Hypothesis**.

## Comparative Experiments

Sometimes a person creates hypotheses and analyzes existing data, such as examining U.S. Census Bureau data to compare employment statistics between 1970 and 2010. However, other times a person poses a hypothesis and then conducts a study to generate data to be analyzed. In one kind of study, the sample is divided into a **treatment group** who was given a treatment being studied (like doing daily exercise), and a **control group** who was not (like not doing daily exercise), with individuals randomly assigned to a group.

## Test Statistic

The central goal of hypothesis testing is to determine whether "Ho" can be rejected in favor of "Ha" or whether "Ho" fails to be rejected based on evidence in the form of sample data. A **test statistic** is a value calculated from sample data during hypothesis testing that measures the degree of agreement between the sample data and the null hypothesis. Mathematically, the test statistic is the difference between the estimate and the value asserted in the null hypothesis divided by the standard error.

## P-Value and Statistical Significance

Intuitively, inferences cannot be made from a trivially small difference between populations or a difference between populations in which the sample sizes are very small, as differences can be observed by chance in such cases. The concept of statistical significance formalizes the intuition of making inferences about populations from observed sample statistics. A **statistically significant** result differs enough from a null hypothesis that a conclusion can be inferred about the population.

In hypothesis testing, the probability of obtaining a result that is as extreme or more extreme than the data if the null hypothesis were true is known as the p-value. The p-value of a result is determined from the test statistic. If the p-value is less than a specified significance level, denoted by a, then two possibilities exist.

- The null hypothesis is true and the observed data is relatively unusual with a sample statistic that is extreme simply due to chance.
- The null hypothesis is false and the alternative hypothesis provides a more reasonable explanation for the population parameter.

In most fields, a=0.05 is used most often as the significance level for hypothesis testing. Thus, the probability that a result with an extreme deviation from the null hypothesis is due to chance must be 5% or less for the result to be considered statistically significant.

A **practically significant** result implies that the magnitude of the difference between the hypothesized value of a parameter and the sample statistic is large enough to be meaningful in real life. Statistical significance does not necessarily imply practical significance of a result. Ex: A statistically significant difference in the number of employees at a company arriving to work at 8:00 am and the number of employees arriving at 7:59 am is likely of little practical significance.

## Type I and Type II Errors

In hypothesis testing, a researcher can decide to reject the null hypothesis or fail to reject the null hypothesis. In reality, the null hypothesis is either true or false. Thus, the researcher can make an error by rejecting a true null hypothesis or failing to reject a false null hypothesis. A **type I** error is the incorrect rejection of a true null hypothesis, and a **type II** error is the failure to reject a false null hypothesis. In other words, a type I error is a false positive and a type II error is a false negative.

The significance level of a hypothesis test, denoted a, is the probability of making a type I error. The probability of making a type II error is denoted B, and the probability 1-B of avoiding type II errors is the power of the hypothesis test.

## Hypothesis Testing Procedure

1. **State the Hypotheses**: Define the null and alternative hypotheses.
2. **Choose the Significance Level**: Select the significance level, a, for the hypothesis test.
3. **Calculate the Test Statistic**: Compute the test statistic from the sample data.
4. **Determine the P-Value**: Calculate the p-value from the test statistic.
5. **Make a Decision**: If the p-value is less than the significance level, reject the null hypothesis. Otherwise, fail to reject the null hypothesis.
6. **Interpret the Results**: State the conclusion in the context of the problem. Determine whether to reject the null hypothesis or fail to reject the null hypothesis.
