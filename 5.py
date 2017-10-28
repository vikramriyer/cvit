from math import sqrt

# read the sides of the triangle
print('Enter 2 sides of the triangle separated by a comma')
s1, s2, s3 = input().split(',')
#s1, s2, s3 = 2, 2.5, 6

# find s first
def find_s():
  return 1/2.*(s1 + s2 + s3)

def validate_if_triangle():

  if s1 + s2 > s3 and s1 + s2 > s2 and s2 + s3 > s1:
    return True
  return False

def main():
  
  if validate_if_triangle():
    s = find_s()
    area = round(sqrt(s*(s-s1)*(s-s2)*(s-s3)), 2)
    print(area)
  else:
    print("0")

if __name__ == '__main__':
  main()