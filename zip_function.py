list1 =[1,2,3]
list2 =["one","two","three"]

zipped = list(zip(list1,list2))

print(zipped)
print("####################")
unzipped =list(zip(*zipped))
print(unzipped)
print("####################")



for (l1, l2) in zip(list1,list2):
    print(l1)
    print(l2)
print("####################")

items = ["apples" ,"banana " , "orange"]
counts =[13,12,11]
prices =[20,30,40]

sentences =[]
for (items,counts,prices) in zip (items,counts,prices):
    items,counts,prices = str(items),str(counts),str(prices)
    sentence = "i bought "+ counts + "  " + items + "at"  +  prices + "." 
    sentences.append(sentence)


print (sentences)

print("done")