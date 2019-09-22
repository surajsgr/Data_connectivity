#!/usr/bin/python3

import pymysql
class sqlConnection:
  def __init__(self,hostname="localhost",username="root", password="Neetudon@123", database = "company"):
    self.hostname= hostname
    self.username= username
    self.password= password
    self.database=database

  def script(self, query):
    db = pymysql.connect(self.hostname, self.username, self.password, self.database)  # Open database connection
    cursor = db.cursor()  # prepare a cursor object using cursor() method
    cursor.execute(query)  # execute SQL query using execute() method.
    data = cursor.fetchall()   # Fetch a all rows using fetchone() method.

    for i in data:
      print(i)
      id=int(i[0])
    db.commit()
    db.close()    # disconnect from server



s=sqlConnection()
# query="alter table employee add primary key (employee_ID)"
# delete_query="Delete from employee"
# select_query="select * from employee"
# avg_query="select avg(employee_salary) from employee"
# s.script(avg_query)






