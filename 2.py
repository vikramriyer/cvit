# read input from standard i/p
print("Enter the string")
#p_str = input()
p_str = "(){}{}[][]()"
p_dict = {'opening': 0, 'closing': 0}
paranthesis = {"opening": ['(', '{', '['], "closing": [')', '}', ']']}

def total_no_of_paranthesis_are_even():

  if len(p_str) % 2 != 0:
    print("NO")
    exit(0)
  print("Length is even and hence further checks can be applied")

def equal_number_of_paranthesis():

  for p in p_str:
    if p in paranthesis['opening']:
      p_dict['opening'] += 1
    else:
      p_dict['closing'] += 1

  if p_dict['opening'] != p_dict['closing']:
    print("NO")
    exit(0)

  print("Both the opening and paranthesis are in equal numbers. We will finally check if an open is enclosed with a close.")

def validate_paranthesis():

  p_stack = [] # stack that maintains the paranthesis, brackets and braces
  for p in p_str:
    if p in paranthesis['opening']:
      p_stack.append(p)
    else:
      if p_stack:
        if p_stack[-1] in paranthesis['opening']:
          p_stack.pop()
        else:
          p_stack.append(p)

  if len(p_stack) != 0:
    print("\nNO\n")
    exit(0)

  print('\nYES\n')

def main():

  # first check if the total number of paranthesis is even, else it is unbalanced
  total_no_of_paranthesis_are_even()

  # now loop over and update the dictionary such and verify if the opening
  # and closing paranthesis are in equal numbers,
  # else it is unbalanced
  equal_number_of_paranthesis()
  
  # final check, an opening paranthesis should have a corresponding closing one
  validate_paranthesis()

if __name__ == '__main__':
  main()
