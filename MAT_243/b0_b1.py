
# Compute the sum of squared errors for the regression equation y=7+2x
x = [0,3,7,10]
y = [5,5,27,31]

y_pred = [2 + (3*i) for i in x]
erros = [y[i] - y_pred[i] for i in range(len(y))]
squared_errors = [e**2 for e in erros]
sse = sum(squared_errors)

print(y_pred)
print(erros)
print(squared_errors)
print(sse)
