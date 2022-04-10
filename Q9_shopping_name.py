import json
shopping_dict={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

c= input("Enter your element name :")
e=int(input("Enter your number of element :"))
dict1={}
dict2={}
for k in shopping_dict:
    # print(shopping_dict[k])
    for p in shopping_dict[k]:
        print(shopping_dict[k][p])
        if c==p:
            dict1.update({p:int(shopping_dict[k][p])-e})
        else:
            dict2.update({p:int(shopping_dict[k][p])})
    dict1.update(dict2)
# print(dict2)
print(dict1)
out_file=open("shopping_list.json","w")
json.dump(dict1,out_file,indent=6)
out_file.close()
