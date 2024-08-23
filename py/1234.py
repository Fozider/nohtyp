import math
import time

s0=0.000290888
c0=math.sqrt(1-s0*s0)
print(c0)
s=s0
c=c0
for n in range(2,54002):
    s=s*c0+c*s0
    c=math.sqrt(1-s*s)
    print(s)

time.sleep(60)
