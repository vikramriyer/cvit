# accept range from the user
print("enter 2 numbers separated by space between which the armstrong numbers are to be calculated.")
l, r = input().split(' ')

# raise a number to the desired power
def no_raised_to_power(numbers):
  powered_number = 0
  power = len(numbers)
  for i in numbers:
    powered_number += int(i)**power
  return powered_number

# validates if a number is armstrong
def is_armstrong(number):
  numbers = [i for i in number]
  if int(number) == no_raised_to_power(numbers):
    return True
  return False

def main():
  
  for i in range(int(l), int(r)+1):
    if is_armstrong(str(i)):
      print(i)

if __name__ == "__main__":
  main()