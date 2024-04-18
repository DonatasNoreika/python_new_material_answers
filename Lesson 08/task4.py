PIN = "0666"

for x in range(10000):
    result = str(x).zfill(4)
    print(result)
    if result == PIN:
        break

# Alternative 1:

import random

PIN = str(random.randint(1, 9999)).zfill(4)

for x in range(10000):
    result = str(x).zfill(4)
    print(result)
    if result == PIN:
        break

# Alternative 2:

i = 1
pin = "6789"

while i < 10000:
    result = (4 - len(str(i))) * "0" + str(i)
    print(result)
    if result == pin:
        break
    i += 1
