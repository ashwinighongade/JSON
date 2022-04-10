import json


list1=[["neelam","programer","24","24000"],["komal","trainer","24","20000"],["anuradha","HR","25","40000"],["Abhishek","manager","29","63000"]]
list2=[["name","degination","age","salary"],["name","degination","age","salary"],["name","degination","age","salary"],["name","degination","age","salary"]]
list3=["emp1","emp2","emp3","emp4"]
dict={}
for i in range(len(list1)):
    dict1={}
    for j in range(len(list1[i])):
        dict1.update({list1[i][j]:list2[i][j]})
    dict.update({list3[i]:dict1})
# print(dict)
outfile=open("empolyee_detail.json","w")
json.dump(dict,outfile,indent=4)
print(outfile)
