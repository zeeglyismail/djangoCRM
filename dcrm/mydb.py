#Install Mysql on Computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
)

#Prepare a cursor object

cursorObject = database.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")