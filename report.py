import mysql.connector
import csv

# DB Credentials for your MySQL query
# Put your host, database. user, and password into the fields below
conn = mysql.connector.connect(host='$HOST',database='$DATABASE',user='$USER',password='$PASSWORD')

cursor = conn.cursor()
query = "$QUERY"
cursor.execute(query)
rows = cursor.fetchall()

# Put the path where you want to generate the report below in the
# with open() section 
with open('/Path/To/Generate/Report/$NAMEofReport.csv', 'wb') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow([i[0] for i in cursor.description])
	csv_writer.writerows(rows)
