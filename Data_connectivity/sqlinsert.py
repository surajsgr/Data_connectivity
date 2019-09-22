# insert records in database "employee"
# import skript

from ScriptCommonSqlConnectivity import sqlConnection
import pymysql

class insert(sqlConnection):
    def insert_query(self,query):
        db = pymysql.connect(self.hostname, self.username, self.password, self.database)  # Open database connection
        # print(self.hostname)
        cursor = db.cursor()
        cursor.execute(query)
        # employee_record = ["insert into employee values('1', 'Jefery', '40000', 'devloper')", "insert into employee values('2', 'Tom', '35000', 'devloper')","insert into employee values('3', 'Jack', '10000', 'devloper')","insert into employee values('4', 'Jill', '20000', 'tester')",
        #                    "insert into employee values('5', 'Marry', '25000', 'tester')", "insert into employee values('6', 'Jason', '30000', 'tester')",
        #                    ]
        # for i in employee_record:
        #     cursor.execute(i)
        #query="INSERT INTO employee (employee_ID, employee_name,employee_salary, designation) VALUES (\"3\",\"Albert\",\"20000\",\"tester\")"
        #cursor.execute(query)
        print("inserted")
        db.commit()
        db.close()

#
# q=insert()
# #query="",
# #q.insert_query()
#
# select_query="select * from employee Order by employee_ID"
# q.script(select_query)


