h = input("Input for h ")
i = 1
q = 0
import math
while int(i) < int(h):
        if int(i) % math.sqrt(int(i)) == 0:
                q += i
                i += 1
                print(q)
        else: i += 1



print(q)
