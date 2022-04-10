# Q.1 Json data ko python object main convert karne ka program likho?.

import json
json_obj = '{ "Name":"David", "details":{"Class":"I", "Age":6} }'

python_obj = json.loads(json_obj)
print(python_obj["details"])
print(type(python_obj))
# print(python_obj["Name"])
# print(python_obj["Class"])
# print(python_obj["Age"])




# print("JSON data:{}".format(python_obj))
# for key in python_obj:
# print("{}: {} ".format(key, python_obj[key]))


