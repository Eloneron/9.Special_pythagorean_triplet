"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for i in range(1, 1001):
    for j in range(i, 1001):
        for k in range(j, 1001):
            if i**2 + j**2 == k**2:
                print(i, j, k)
                if i + j + k == 1000:
                    print(f'Product of {i, j, k} = {i * j * k}')