# read input from standard i/p
print("Enter the string")
#p_str = input()
p_str = "(){}{}[]][()"

paranthesis = {"opening": ['(', '{', '['], "closing": [')', '}', ']']}

# first check if the total number of paranthesis is even, else it is unbalanced
if len(p_str) % 2 != 0:
  print("Length is not even, and hence string is unbalanced")
  exit(0)
print("Length is even and hence further checks can be applied")

p_dict = {'opening': 0, 'closing': 0}
# now loop over and update the dictionary such that opening and closing are equal, else it is unbalanced
for p in p_str:
  if p in paranthesis['opening']:
    p_dict['opening'] += 1
  else:
    p_dict['closing'] += 1

if p_dict['opening'] != p_dict['closing']:
  print("Opening and closing paranthesis are not equal and hence unbalanced.")
  exit(1)

print("Both the opening and paranthesis are in equal numbers. We will finally check if an open is enclosed with a close.")

p_stack = []
# final check, an opening paranthesis should have a closing one
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
  print("\nThe string is not balanced!\n")
  exit(0)

print('\nThe String is balanced!\n')
