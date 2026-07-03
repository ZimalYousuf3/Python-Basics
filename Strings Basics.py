# 3 WAYS OF DECLARING STRINGS
str1 = "Zimal"
str2 = 'Yousuf'
str3 = """Siddiqui"""
print(str1)
print(str2)
print(str3)

# STRING CONCATENATION
result = (str1 +" "+ str2 +" "+ str3)
print(result)

# STRING LENGTH
len1 = len(str1)
print(len1)

# INDEXING
print (str1[0]) # Can only access the value. Cannot modify.

# SLICING
# Positive Slicing
str4 = "Taylor Swift"
print ( str4 [0:6] ) # [start_indx : end_indx] (end_indx not included)
print ( str4 [:6] )
print ( str4 [0:] ) 

# Negative Slicing
str4 = "Taylor Swift"
print ( str4 [-12:-6] ) # [start_indx : end_indx] (end_indx not included)
print ( str4 [:-6] )
print ( str4 [-12:] ) 



