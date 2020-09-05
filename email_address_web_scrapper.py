import re

'''
#find in this
text ="any random string "
 
#match to this
pattern = re.compile("any random string")

result = pattern.search(text)

print(result)
######################################## ONLY FIRST MATCH WILL BE FOUND 
pattern = re.compile("[rdn]+")

result = pattern.search(text)

print(result)

print("done")
'''
#\is added to escape the space or to differentiate
text= "random string . sabya.mohanty12@gmail.com fahdgfj asfjgasj asfjgasjgf kasgfkahs  sbm.34@gmail.com"
pattern = re.compile("[a-zA-Z0-9\.\-\_]+\@[a-zA-Z0-9\.\-\_]+\.[a-zA-Z0-9]+")
result =pattern.findall(text)
print(result)