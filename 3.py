import pandas as pd
import numpy as np

data = pd.read_csv('grades.txt', sep = ',')
data.set_index('rollno', inplace = True)
cols = data.columns

# task 1
for col in cols:
  print("{} => Mean = {}, STD = {}".format(col, data[col].mean(), data[col].std()))

# task 2
data['total'] = data['assignment_1'] + data['assignment_2'] + data['assignment_3'] + \
                data['assignment_4'] + data['labs'] + data['lab_exam'] + \
                data['midsem_1'] + data['midsem_2'] + data['end_sem']
print("total => Mean = {}, STD = {}".format(data['total'].mean(), data['total'].std()))

# task 3
print(data[data['total'] == data['total'].max()])