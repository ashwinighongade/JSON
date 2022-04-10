# Python object key unique key value ko access karne ka program likho?
import json

json_file='{"a":1,"a":2,"a":3, "a":4,"b":1,"b":2}'
python_obj=json.loads(json_file)
print(python_obj)

