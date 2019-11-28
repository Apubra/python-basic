# Absolute Values:
exNum1 = -5
exNum2 = 5
print(abs(exNum1))
if abs(exNum1) == exNum2:
    print('True!')

# The Help function:
# help()

import time
# will work in a typical installation of Python, but not in the embedded editor
# help(time)


# Max and Min:
exList = [5,2,1,6,7]
largest = max(exList)
print(largest)
smallest = min(exList)
print(smallest)

# Rounding:
x = 5.622
x = round(x)
print(x)

y = 5.256
y = round(y)
print(y)


# Converting data types:
# Converting a string to an integer:
intMe = '55'
intMe = int(intMe)
print(intMe)

# Converting and integer to a string:
stringMe = 55
stringMe = str(stringMe)
print(stringMe)


# Converting an integer to a float:
floatMe = 55
floatMe = float(floatMe)
print(floatMe)
