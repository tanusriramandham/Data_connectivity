import mysql.connector
import pandas as pd
from mysql.connector import Error

# Step 1: Connect to the MySQL server
connection = mysql.connector.connect(
    host='localhost',         
    user='root',     
    password='Tanu@123',    
    auth_plugin='mysql_native_password'  
)

if connection.is_connected():
    print("Successfully connected to the database server")

# Create a cursor to execute queries
cursor = connection.cursor()

# Step 2: Create a new database
#cursor.execute('CREATE DATABASE IF NOT EXISTS data_the_upload')
cursor.execute('USE data_the_upload')

# Step 3: Create the table in the database
# Ensure the ID column is the first column
# create_table_query = """
#   CREATE TABLE IF NOT EXISTS employee_data (
#     Education VARCHAR(50),
#     JoiningYear INT,
#     City VARCHAR(100),
#     PaymentTier INT,
#     Age INT,
#     Gender VARCHAR(10),
#     EverBenched VARCHAR(3),
#     ExperienceInCurrentDomain INT,
#     LeaveOrNot INT
# );
# """
# cursor.execute(create_table_query)

# Step 4: Load the data from the CSV file into a DataFrame
df = pd.read_csv('Employee.csv')  # Replace with your file path
df = df.dropna()  # Drop rows with null values
df = df.head(30)  # Use the first 30 rows

print(df)

# for i, row in df.iterrows():
#     # Ensure data_to_insert matches the expected number of columns in the table
#     data_to_insert =tuple(row)  # Include the index as ID

#     insert_query = """
#     INSERT INTO employee_data (Education,JoiningYear,City,PaymentTier,Age,Gender,EverBenched,ExperienceInCurrentDomain,LeaveOrNot)
#     VALUES (%s,%s, %s, %s, %s, %s, %s, %s,%s)
#     """
#     cursor.execute(insert_query, data_to_insert)

# Commit the transaction to save the data
connection.commit()

print("Data inserted successfully into employee_data table!")
print("queries to execute on database ")
#1st query
cursor.execute('select * from employee_data')
records=cursor.fetchall()
for record in records:
    print(record)
print("query 1 complete data is executed")
#2nd query
cursor.execute('select * from employee_data where Education="Masters"')
records=cursor.fetchall()
for record in records:
    print(record)
print("query 2 only masters students data is executed")

#3rd query
cursor.execute('SELECT COUNT(*) FROM employee_data WHERE Education = "Masters"')
records=cursor.fetchall()
print(records)
print(f"therefore {records} are there studying masters ")
# Step 6: Close the cursor and connection
cursor.close()
connection.close()
