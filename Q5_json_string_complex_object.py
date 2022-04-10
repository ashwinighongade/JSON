# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?
import json
a='{"a": 3+4j,"b":3,"c":5}'
b=json.loads(a)
print(b)


