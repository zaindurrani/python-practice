# pythn has many function to deal with files and manipulate files, opening reading writing files

#we will be working with large amount of data,
#there are 2 file handling funcion open and close
#open function
#open(<filename> <file location > ,<mode=>)
# so it has 2 arguments file name location and mode

# mode specifies wht to do with the file read write or creating also specifies if it should be text or binary
# mode types
"""
'r': open and read in text format
'rb' opens and read file in binary format
'r+' for both
w will over wrifht
    'a' opens file for editing and appending

one more way to openn and close file is with funcion
"""

#close function


file = open('zai.txt', mode='rb')
data = file.readline
print(data)
file.close