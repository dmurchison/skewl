import pandas as pd

df1 = pd.DataFrame([1,2,3,4])
df2 = pd.DataFrame([1,3,5,7])

print(df1[df1, df2].corr())
