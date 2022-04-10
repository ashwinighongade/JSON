import json


a = """Name Abhishek abc
 Designation CEO of navgurukul
 Gender male asd
 Age 29 dsdf"""
 
file = open("text.txt","w")
file.write(a)
file.close()
s_file="text.txt"
dict={}
with open (s_file) as f:
    for d in f:
        #print(d)
        b,a=d.strip().split(None,1)
        dict[b]=a.strip()
        k,desc=d.strip().split(None,1)
        
        dict[k]=desc.strip()
print(dict)
print(type(dict))


o=open("j_text.json","w")
json.dump(dict,o,indent=6)
o.close()