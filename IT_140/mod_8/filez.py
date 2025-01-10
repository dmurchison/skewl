import os
import datetime

curr_day = datetime.date(1997, 8, 29)

num_days = 30
for i in range(num_days):
    year = str(curr_day.year)
    month = str(curr_day.month)
    day = str(curr_day.day)

    # Build path string using current OS path separator
    file_path = os.path.join('lab.txt')

    f = open(file_path, 'r')
    print('{}: {}'.format(file_path, f.read()))
    f.close()

    curr_day = curr_day + datetime.timedelta(days=1)
