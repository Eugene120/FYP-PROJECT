import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "123",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "test")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from category"
    
    cursor.execute(postgreSQL_select_Query)
    print(" selecting rows from table")
    category_records= cursor.fetchall()

    print("Print each row and it's columns values")
    for row in category_records:
        print("id_category= " ,row[0],)
        print("category_name =" ,row [1])
        print("categpry_image =" ,row[2])

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
                
