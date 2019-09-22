from sqlinsert import insert
import json

def extract_json(jsonfile=None):
    with open (jsonfile,'r') as f:
        return f.read()



employee_list=extract_json('Sqljson.json')

for e in employee_list:
    print(type(e))
    d=eval(e)
    print(type(d))
    insert.script("insert into Employee values (%s,%s,%s,%s)",e["employee_ID"],e["employee_name"],e["employee_salary"],e["designation"])
    print("inserted into DB")