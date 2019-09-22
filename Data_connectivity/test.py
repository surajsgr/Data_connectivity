import json

with open("Sqljson.json",'r') as f:

    data=json.load(f)




print(type(data))


for i in data:
    print(type(i))

