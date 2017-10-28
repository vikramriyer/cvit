from math import sqrt

print('Enter 2 sides of the triangle separated by a comma')
s1, s2, s3 = input().split(',')

# find s first
s = 1/2.*(s1 + s2 + s3)

# find area, rounded to 2 decimal places
area = round(sqrt(s*(s-s1)*(s-s2)*(s-s3)), 2)

print(area)