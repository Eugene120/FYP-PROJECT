from PIL import Image  
import PIL  
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=L30809\TESTSERVER;'
                      'Database=ok boomer;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("SELECT * FROM TEST")

for row in cursor:
    print(row)



