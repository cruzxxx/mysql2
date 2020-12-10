import os
import datetime
import pymysql

# Get username from Gitpod workspace
# modify this variable if running on another environment
username = os.getenv('Stef')

# Connect to the DB
connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['grace']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends Where name in ({});".format(format_strings), 
        list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was sucessfull
    connection.close
