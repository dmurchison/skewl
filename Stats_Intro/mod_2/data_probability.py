from scipy.stats import rv_discrete

# Defines a list containing the outcomes in the sample space
x = [0,1,2,3,4,5,6]

# Defines a list containing the probabilities for each outcome
p = [0.1,0.2,0.3,0.1,0.1,0.0,0.2]

# Links the values in x to the probabilities in p
discvar = rv_discrete(values=(x,p))

print(discvar.mean())

