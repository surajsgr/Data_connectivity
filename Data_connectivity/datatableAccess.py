# insert records in database "employee"
# import skript

from ScriptCommonSqlConnectivity import sqlConnection
import pymysql

class DBaccess(sqlConnection):
    def data_json(self):
        db = pymysql.connect(self.hostname, self.username, self.password, self.database)  # Open database connection
        # print(self.hostname)
        cursor = db.cursor()
        # employee_record = ["insert into employee values('1', 'Jefery', '40000', 'devloper')", "insert into employee values('2', 'Tom', '35000', 'devloper')","insert into employee values('3', 'Jack', '10000', 'devloper')","insert into employee values('4', 'Jill', '20000', 'tester')",
        #                    "insert into employee values('5', 'Marry', '25000', 'tester')", "insert into employee values('6', 'Jason', '30000', 'tester')",
        #                    ]
        # for i in employee_record:
        #     cursor.execute(i)

        # query="INSERT INTO employee (employee_ID, employee_name,employee_salary, designation) VALUES (\"3\",\"Albert\",\"20000\",\"tester\")"
        query="select * from employee"
        cursor.execute(query)
        data=cursor.fetchall()
        l=[]
        for i in data:
            d={}
            d['id']=i[0]
            d['name']=i[1]
            d['salary']=i[2]
            d['designation']=i[3]
            # print(d)
            l.append(d)


        db.commit()
        db.close()
        return l

    def average(self):

        result_list=DBaccess.data_json(self)
        sum=0
        for i in result_list:
            sum+=int(i['salary'])
        average_value=sum/len(result_list)

        return average_value

#
d=DBaccess()
#query="",
#q.insert_query()

"""query 1"""
# for i in d.data_json():
#
#     if  int(i['salary'])>20000:
#         print(i['name'])


"query 2"
# sum=0
# for i in d.data_json():
#     sum+=int(i['salary'])
# average=sum/len(d.data_json())
# print(average)

#----------------
# d.data_json()
# print(d.average())




