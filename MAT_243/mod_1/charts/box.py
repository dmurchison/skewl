import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# reads the mtcars.csv file into a dataframe called mtcars
mtcars = pd.read_csv("https://s3-us-west-2.amazonaws.com/data-analytics.zybooks.com/mtcars.csv")

# prints the first few lines of mtcars
print(mtcars.head())

# prints the five-number summary of the wt column of mtcars
print(mtcars.wt.describe())

# prints a box plot of the wt column of mtcars
sns.boxplot(y = mtcars.wt)

# saves the image
plt.savefig("carsboxplot.png")
