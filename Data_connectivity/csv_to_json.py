import csv
import json

csvfile = open('SqlData.csv', 'r')
jsonfile = open('Sqljson.json', 'w')

fieldnames = ("employee_ID","employee_name","employee_salary","designation")
reader = csv.DictReader( csvfile, fieldnames)
print(reader)
result=[]
for row in reader:
    print(row)
    result.append(row)
result=result[1:]
json.dump(result, jsonfile)
jsonfile.write('\n')