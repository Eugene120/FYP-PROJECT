import psycopg2
from config import Config


def write_blob(id_category, category_name, category_image):
    """ insert a BLOB into a table """
    
    try:
        # read data from a picture
        drawing = open('C:/Users/L30809.NYPSIT.000/Desktop/maxx.jpg', 'rb').read()
        # read database configuration
        params = Config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(user = "postgres",
                                  password = "123",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "test")
        # create a new cursor object
        cur = conn.cursor()
        cur.execute("SELECT version();")
        record = cur.fetchone()
        print("You are connected to - ", record,"\n")

        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO Category(id_category, category_name, category_image) " +
                    "VALUES(%s,%s,%s)",
                    (id_category, category_name, psycopg2.Binary(drawing)))
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
        write_blob(1, 'C:/Users/L30809.NYPSIT.000/Desktop/maxx.jpg', 'jpg')
        write_blob(2, 'C:/Users/L30809.NYPSIT.000/Desktop/maxx.jpg', 'jpg')                

    
def read_blob(id_category, category_image):
        """ read BLOB data from a table """
    
        try:
            # read database configuration
            
            # connect to the PostgresQL database
            conn = psycopg2.connect(user = "postgres",
                                  password = "123",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "test")
            # create a new cursor object
            cur = conn.cursor()

            print ( conn.get_dsn_parameters(),"\n")
            # execute the SELECT statement
            cur.execute(""" SELECT ID, Name, Face_Data
                            FROM StudentsData
                             """
                       )
    
            blob = cur.fetchone()
            open('C:/Users/L30809.NYPSIT.000/Desktop/maxx.jpg + blob[5]' + '.' + blob[6], 'wb').write(blob[7])
            # close the communication with the PostgresQL database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL",error)
        finally:
            if conn is not None:
                conn.close()      

       

        