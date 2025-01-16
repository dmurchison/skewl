import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t < -0.25)?
print(st.t.cdf(2.558, 14, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t < 1.5)?
print(st.t.cdf(1.5, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t > -0.25)?
print(st.t.sf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t > 1.5)?
print(st.t.sf(1.5, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(-0.25 < t < 1.5)?
print(st.t.cdf(1.5, 30, 0, 1) - st.t.cdf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(1.5 < t < 2.85)?
print(st.t.cdf(2.85, 30, 0, 1) - st.t.cdf(1.5, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 59, the mean is 55,
# and the standard deviation is 7.5, what is P(t < 62)?
print(st.t.cdf(62, 59, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 34, the mean is 55,
# and the standard deviation is 7.5, what is P(t > 51)?
print(st.t.sf(51, 34, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 59, the mean is 55,
# and the standard deviation is 7.5, what is P(49 < t < 60)?
print(st.t.cdf(2.56, 14, 0, 1) - st.t.cdf(1.57, 14, 0, 1))

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and
# the standard deviation is 1, what is t* if P(t < t*) = 0.135?
print(st.t.ppf(0.135, 49, 0, 1))

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and
# the standard deviation is 1, what is t* if P(t < t*) = 0.135?
print(st.t.ppf(0.135, 49, 0, 1))

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and
# the standard deviation is 1, what is t* if P(t > t*) = 0.405?
print(st.t.isf(0.405, 49, 0, 1))


# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and
# the standard deviation is 7.5, what is t* if P(t < t*) = 0.8247?
print(st.t.ppf(0.6, 4, 0, 1))

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and
# the standard deviation is 7.5, what is t* if P(t > t*) = 0.95?
print(st.t.isf(0.95, 24, 55, 7.5))
