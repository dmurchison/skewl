import scipy.stats as st

# For a normal distribution, if the mean is 55 and
# the standard deviation is 7.5, what is P(x <= 62)?
print(st.norm.cdf(3.8, 3.57, 0.098) - st.norm.sf(150, 150, 8.75))


# For a normal distribution, if the mean is 55 and
# the standard deviation is 7.5, what is P(x >= 51)?
print(st.norm.cdf(3.8, 3.57, 0.098))


# For a normal distribution, if the mean is 55 and
# the standard deviation is 7.5, what is P(49 <= x <= 60)?
# print(st.norm.cdf(x, mean, std) - st.norm.cdf(49, 55, 7.5))


def z_score(x,mean,std):
    return (x-mean)/std

print(z_score(3.8,3.57,0.098))
