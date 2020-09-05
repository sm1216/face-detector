names =["sabya" , "sachi " , "mohanty"]

l=[]
for person in names:
    l.append(person)
print(l)

print([person for person in names])
###########################################
l=[]
for person in names:
    l.append(person + "xyz")
print(l)
print("done")
###############################
print([person + " xyz " for person in names])
##################################
movies_and_ratings={"interstellar":9,"50 shades" : 10, "dark knoght" : 3}
l=[]
for movie in movies_and_ratings:
    if movies_and_ratings[movie]>6:
        l.append(movie)
print(l)
######################################
print([movie for movie in movies_and_ratings if movies_and_ratings[movie]>6])
##########################################