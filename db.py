import psycopg2

try:
 connection = psycopg2.connect(
    database="expenzo",
    user="admin",
    host="oregon-postgres.render.com",
    password="38X9LayFxLO0XpHX1nZq2rcOKbHzqeXS")

 cursor = connection.cursor()
 print("Connection with DB Done")

except(Exception, psycopg2.Error) as error:
    print("Error while connecting DB")
    print(error)
