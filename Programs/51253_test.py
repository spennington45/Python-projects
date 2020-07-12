k = int(input("value for k "))
m = int(input("m must be greater then k "))
q = 0
i = k
import math
while i <= m:
        if i % math.sqrt(i) == 0:
                q += 1
                i += 1
        else: i += 1
print(q)
