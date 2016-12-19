from scipy import *

def f(x):
  return 2*x + 1

z = []
for x in range(10):
  if f(x) > pi:
    z.append(x)
  else:
    z.append(-1)
print(z)
