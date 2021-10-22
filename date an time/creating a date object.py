# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.

import datetime

x = datetime.datetime(2021, 10, 2)
print(x)
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, (None for timezone).

y = datetime.datetime(2021, 10, 2, 17, 41, 20, 304007)
print(y)
