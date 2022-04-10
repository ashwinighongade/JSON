# Write a Python program to convert Python dictionary object (sort by key)
#  to JSON data. Print the object members with indent level 4.
import json

dict={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
# json_str=json.dumps(dict,sort_keys=True,indent=4)
# print(json_str)
# print(type(json_str))
list1=[]
for i in dict:
    list1.append(i)
print(list1)
i=0
while i<len(list1):
    j=0
    while j<len(list1):
        if list1[j]>list1[i]:
            temp=list1[j]
            list1[j]=list1[i]
            list1[i]=temp
        j+=1
    i+=1
print(list1)
new={}
for j in list1:
    for k in dict:
        if j==k:
            new[j]=dict[k]
print(new)

e=open("file_j.json","w")
json.dump(new,e,indent=6)
e.close()


