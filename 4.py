# read the file into list
text_file = open('first-names.txt', 'r')
dictionary = [i.lower() for i in text_file.read().split('\r\n')]

search_str = "ar"

# search measure 1: the search_str sequence is present in the name, for ex: if we search for 'ar', then return values will be
# ['aaren', 'aarika', ...., 'barbie', 'barbra', ..., 'zarah', 'zaria', 'zarla'] i.e. ar is present squentially in the 
# results
print([i for i in dictionary if search_str in i])

# search measure 2: 

text_file.close()