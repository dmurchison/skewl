# PDF vs CDF

## PDF

A **probability density function** (pdf) describes the probability that a random variable takes on a certain value. The pdf is a function that is always non-negative and integrates to 1.

### Example of PDF

Casey is studying the time it takes to commute to work every day. Over a long period, Casey has observed that the commute time follows a normal distribution with a mean of 30 minutes and a standard deviation of 5 minutes.

**Question:**

  What is the probability that Casey's commute time on a given day is exactly 30 minutes?

**Explanation:**

  To find this probability, we use the probability density function (PDF) of the normal distribution. The PDF gives us the likelihood of the commute time being exactly 30 minutes. However, for continuous distributions like the normal distribution, the probability of the commute time being exactly any specific value (e.g., exactly 30 minutes) is technically zero. Instead, the PDF value at 30 minutes gives us the density of the probability around that point.

**Solution:**

  Using the PDF formula for a normal distribution:

  ```math
  [ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} ]
  ```

  where:

  ```math
  ( \mu = 30 ) (mean)
  ( \sigma = 5 ) (standard deviation)
  ( x = 30 ) (commute time)
  ```

**Calculation:**

  We can calculate the PDF value at ( x = 30 ) using Python:

  This PDF value represents the density of the probability at 30 minutes, not the actual probability of the commute time being exactly 30 minutes.import numpy as np

**Python Code:**

  ```python
  import numpy as np
  from scipy.stats import norm

  # Parameters for the normal distribution
  mean = 30
  std_dev = 5

  # Calculate the PDF value at x = 30
  pdf_value = norm.pdf(30, mean, std_dev)

  print(f"The PDF value at 30 minutes is: {pdf_value}")import numpy as np
  ```

## CDF

A **cumulative distribution function** (CDF) describes the probability that a random variable takes on a value less than or equal to a given value. The CDF is a function that ranges from 0 to 1.

### Example of CDF

Casey is studying the time it takes to commute to work every day. Over a long period, Casey has observed that the commute time follows a normal distribution with a mean of 30 minutes and a standard deviation of 5 minutes.

**Question:**

  What is the probability that Casey's commute time on a given day is less than or equal to 35 minutes?

**Explanation:**

  To find this probability, we use the cumulative distribution function (CDF) of the normal distribution. The CDF gives us the probability that the commute time is less than or equal to a specific value (e.g., 35 minutes).

**Solution:**

  Using the CDF formula for a normal distribution:

  ```math
  [ F(x) = \frac{1}{2} [1 + erf(\frac{x-\mu}{\sigma\sqrt{2}})] ]
  ```

  where:

  ```math
  ( \mu = 30 ) (mean)
  ( \sigma = 5 ) (standard deviation)
  ( x = 35 ) (commute time)
  ```

**Calculation:**

  We can calculate the CDF value at ( x = 35 ) using Python:

  This CDF value represents the probability that the commute time is less than or equal to 35 minutes.import numpy as np

**Python Code:**

  ```python
  import numpy as np
  from scipy.stats import norm

  # Parameters for the normal distribution
  mean = 30
  std_dev = 5

  # Calculate the CDF value at x = 35
  cdf_value = norm.cdf(35, mean, std_dev)

  print(f"The CDF value at 35 minutes is: {cdf_value}")import numpy as np
  ```
