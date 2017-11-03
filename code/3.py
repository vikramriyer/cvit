import pandas as pd

# read the data and set roll number as the index
data = pd.read_csv('grades.txt', sep = ',')
data.set_index('rollno', inplace = True)
cols = data.columns

# task 1: print the mean and standard deviation for all the columns
print("Task 1\n")
for col in cols:
  print("{} => Mean = {}, STD = {}".format(col, data[col].mean(), data[col].std()))

# task 2: print the mean and standard deviation for aggegate marks of the student
print("\nTask 2\n")
data['total'] = data['assignment_1'] + data['assignment_2'] + data['assignment_3'] + \
                data['assignment_4'] + data['labs'] + data['lab_exam'] + \
                data['midsem_1'] + data['midsem_2'] + data['end_sem']
print("total => Mean = {}, STD = {}".format(data['total'].mean(), data['total'].std()))

# task 3: print details of the student who scored max marks
print("\nTask 3\n")
print("Roll number of student with max marks: {}".format(data.index[data['total'] == data['total'].max()].tolist()[0]))