from math import pow
import math


def norm(v, p=2):
    summation = sum([pow(num, p) for num in v])
    pnorm = (summation ** (1/p))
    return pnorm


# Below call is for Euclidean norm with default p=2
print(norm([3, 4]))

# Below call is for pnorm for given v,p
print(norm([1, 1, 1], 3))
