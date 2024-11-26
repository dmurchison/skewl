names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']

num = 5
for i in range(len(names)):
    if i == num:
        break # the reason for the break is to stop the loop when the condition is met
    print(names[i], end= ' ')
else:
    print('All names printed.')

