import psycopg2

 
 
def write_blob(id_category, category_name, category_image):
    """ insert a BLOB into a table """
    
    try:
        # read data from a picture
        drawing = open('Users/L30809.NYPSIT.000/Pictures/wtf', 'rb').read()
        # read database configuration
        
        # connect to the PostgresQL database
        conn = psycopg2.connect(user = "postgres",
                                  password = "123",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "test")
        # create a new cursor object
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")

        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO test(id_category,category_name, category_image) " +
                    "VALUES(%s,%s,%s)",
                    (id_category, category_image, psycopg2.Binary(drawing)))
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    
    def read_blob(id_category, category_image):
        """ read BLOB data from a table """
    
        try:
            # read database configuration
            
            # connect to the PostgresQL database
            
            # create a new cursor object
            cur = conn.cursor()

            print ( conn.get_dsn_parameters(),"\n")
            # execute the SELECT statement
            cur.execute(""" SELECT id_category, category_name, category_image
                            FROM test
                             """
                       )
    
            blob = cur.fetchone()
            open('C:/Users/L30809.NYPSIT.000/Documents/GitHub/FYP-PROJECT/dataset + blob[0]' + '.' + blob[1], 'wb').write(blob[2])
            # close the communication with the PostgresQL database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL",error)
        finally:
            if conn is not None:
                conn.close()      

       

    if __name__ == '__main__':
        write_blob(1, 'C:/Users/L30809.NYPSIT.000/Pictures/wtf.png', 'jpg')
        write_blob(2, 'C:/Users/L30809.NYPSIT.000/Pictures/wtf.png', 'jpg')            