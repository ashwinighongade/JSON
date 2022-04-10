# Write a Python program to convert Python object to JSON data.
import json


dic={"name": "David", "class": "I", "age": 6}

out_file=open("myfile.json","w")
json.dump(dic,out_file,indent=6)
out_file.close()

# a={"a":1,"b":2,"c":3}
# with open("file.json","w") as file:
#     json.dump(a,file,indent=2)
