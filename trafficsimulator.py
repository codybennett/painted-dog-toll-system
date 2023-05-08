import mysql.connector
import os

distance = 5

def main():
    ident = input("Indentifier:\t")
    operation = input("Incoming (I) or Exiting (E):\t")
    if operation.upper() == "I":
        incoming(ident)
    if operation.upper() == "E":
        exiting(ident)

def db_connection():
    host = os.environ['db_host']
    name = os.environ['db_name']
    user = os.environ['db_user']
    passwd = os.environ['db_pass']

    try:
        return mysql.connector.connect(
            host=host, 
            user=user, 
            passwd=passwd, 
            database=name
            )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials for DB")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Incorrect/Invalid database")
        else:
            print(err)


def incoming(identifier):
    db = db_connection()

    if db:
        cursor = db.cursor()
        cursor.execute(f"SELECT MAX(id) from users WHERE name='{identifier}'")
        un = cursor.fetchone()
        print(cursor.rowcount)
        if un[0] is None:
            cursor.execute(f"INSERT INTO users (name, rfid_uid) VALUES ('{identifier}','123')")
            db.commit()
            cursor.execute(f"SELECT MAX(id) from users WHERE name='{identifier}'")
            un=cursor.fetchone()
        
        #print(f"INSERT INTO tollbooth (user_id) VALUES ({un[0]}));")
        cursor.execute(f"INSERT INTO tollbooth (user_id) VALUES ({un[0]});");
        db.commit()
        db.close()

def exiting(identifier):
    db = db_connection()

    if db:
        cursor = db.cursor()
        cursor.execute(f"SELECT id from users WHERE name='{identifier}'")
        un=cursor.fetchone()
        cursor.execute(f"SELECT max(id) from tollbooth where user_id={un[0]}")
        most_recent = cursor.fetchone()
        print(un[0],most_recent[0])
        
        cursor.execute(f"UPDATE tollbooth SET clock_out=NOW() where user_id='{un[0]}' AND id={most_recent[0]};");
        db.commit()
        cursor.execute(f"UPDATE tollbooth SET duration=TIMEDIFF(clock_out,clock_in),estimated_speed={distance}/(TIME_TO_SEC(TIMEDIFF(clock_out,clock_in)/3600)) where user_id='{un[0]}' AND id={most_recent[0]};")
        
        db.commit()
        db.close()

if __name__ == "__main__":
    main()
    

    
