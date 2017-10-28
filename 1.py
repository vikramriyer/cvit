# read input from standard i/p
print("Enter the string")
#p_str = input()
p_str = "())(()"

# first check if the total number of paranthesis is even, else it is unbalanced
if len(p_str) % 2 != 0:
  print("Length is not even, and hence string is unbalanced.")
  exit(0)
print("Length is even, let's verify if they are in equal numbers.")

p_dict = {'opening': 0, 'closing': 0}
# now loop over and update the dictionary such and verify if the opening
# and closing paranthesis are in equal numbers,
# else it is unbalanced
for p in p_str:
  if p == '(':
    p_dict['opening'] += 1
  else:
    p_dict['closing'] += 1

if p_dict['opening'] != p_dict['closing']:
  print("Opening and closing paranthesis are not equal and hence unbalanced.")
  exit(0)

print("Both the opening and paranthesis are in equal numbers. We will finally \
  check if an open is enclosed with a close.")

p_stack = []
# final check, an opening paranthesis should have a closing one
for p in p_str:
  if p == '(':
    p_stack.append('(')
  else:
    if p_stack:
      if p_stack[-1] == '(':
        p_stack.pop()
      else:
        p_stack.append(p)

if len(p_stack) != 0:
  print("\nThe string is not balanced!\n")
  exit(0)

print('\nThe String is balanced!\n')
