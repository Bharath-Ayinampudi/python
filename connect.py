import sqlite3

def create_table(db_name):
    conn=connect(web.db)
    
    conn.execute("CREATE TABLE IF NOT EXISTS Login_table(LOGIN TEXT, PASSWORD TEXT)")
    
    print("TABLE CRREATED SUCESSFULLY")
    
    conn.close()
    
def insert_table(db_name):
    conn=sqlite3.connect(web.db)
    
    conn.execute("INSERT INTO Login_table(LOGIN,PASSWORD) VALUES(LOGIN,PASSWORD)")
    conn.commit()
    connn.close()
    
def get_data(db_name):
    conn=sqlite3.connect("web.db")
    cur=conn.cursor()

    cur.execute("SELECT * FROM Login_table")

    table_data=cur.fetchall()

    for record in table_data:
       print(record)
       
    conn.close()
