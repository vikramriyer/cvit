import random

# read the file into list
text_file = open('first-names.txt', 'r')

# convert all to lower case so that search becomes easier
dictionary = [i.lower() for i in text_file.read().split('\r\n')]

search_str = "ar"
#search_str = input()

# search measure 1: the search_str sequence is present in the name, 
# for ex: if we search for 'ar', then return values will be
# ['aaren', 'aarika', ...., 'barbie', 'barbra', ..., 'zarah', 'zaria', 'zarla']
# i.e. ar is present squentially in the results
similar_matches = [i for i in dictionary if search_str in i]

# randomly pick 5 values from the total matches
top_5_results = random.sample(similar_matches, 5)

print(top_5_results)

text_file.close()