import matplotlib.pyplot as plt
import matplotlib.markers as markers

x = [0,2,7,10]
y = [5,5,27,31]

plt.plot(x, y, marker=markers.TICKUP, markersize=10)
# plt.show()

# Compute the sum of squared errors for the regression equation y=4+6x
x = [0,1,3,6,6,8]
y = [6,12,18,33,42,57]

y_pred = [4 + (6*i) for i in x]
erros = [y[i] - y_pred[i] for i in range(len(y))]
squared_errors = [e**2 for e in erros]
sse = sum(squared_errors)

print(y_pred)
print(erros)
print(squared_errors)
print(sse)

# To find the residual sum of squares

# Use the sse variable from the previous code snippet
n = len(x)
k = 2
rss = sse / (n - k)
print(rss)

# The residual standard error is the square root of the residual sum of squares
residual_standard_error = rss ** 0.5
print(residual_standard_error)


