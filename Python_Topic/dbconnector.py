import mysql.connector as db

def create_engine(query):
    try:
        mydb = db.connect(host='localhost',user = 'root',password = 'root')
        cursor = mydb.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except:
        print("QUERY ERROR")



def insert_data(query):
    mydb = db.connect(host='localhost',user = 'root',password = 'root')
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    return cursor.fetchall()
