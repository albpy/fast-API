#----------------------------------------------------------------------------------------------------------------------
#                                       DATABASE FETCHING and routed to (JSON) output
#______________________________________________________________________________________________________________________


import psycopg2
from config import config # Database configuration file
import sys # to access command-line arguments



def connect():
    conn =None
    try:
        params = config()
        conn = psycopg2.connect("host = localhost dbname=supp_json_queries port=6000 user=postgres password=root") # create new database session
        # conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
    except(Exception.psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            print("Database connection terminalted...")

def Databases():
    conn =None
    try:
        params = config()
        conn = psycopg2.connect("host = localhost dbname=supp_json_queries port=6000 user=postgres password=root") # create new database session
        # conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # execute a statement
        print('PostgreSQL all databases list:')
        cur.execute('SELECT datname FROM pg_database')
        tables = cur.fetchall()
        print(tables)
    except(Exception.psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            print("Database connection terminalted...")


def create_table():
    conn =None
    try:
        params = config()
        conn = psycopg2.connect("host = localhost dbname=supp_json_queries port=6000 user=postgres password=root") # create new database session
        # conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # execute a statement
        print('PostgreSQL table creating...:')
        cur.execute("""CREATE TABLE IF NOT EXISTS Teachers
              (parent_id int PRIMARY KEY, 
              name VARCHAR(40) NOT NULL, 
              class int, 
              dept VARCHAR(255))""")
        conn.commit()
    except(Exception.psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            print("Database connection terminalted...")


def Insert_Teacher(parent_id, teacher_name, class_, dept):
    params = config()
    """ insert a new teacher into the teachers table """
    sql = """INSERT INTO Teachers(parent_id, name, class, dept)
             VALUES (%s, %s, %s, %s) RETURNING parent_id;"""
    conn = None
    new_parent_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (parent_id, teacher_name, class_, dept))
        # get the generated id back
        new_parent_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return new_parent_id



# FastAPI: A modern, fast (high-performance), web framework for building APIs with Python
# HTMLResponse: Response class of fastapi for rendering HTML content

# JSONResponse: Response class of fastapi for returning JSON content
# Jinja2Templates: Template engine for rendering HTML templates
# datetime: Module for working with dates and times
# Union: Type hint for specifying a variable with multiple possible types


from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates

from datetime import datetime
from typing import Union

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory= "templates")



if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--connect":
        connect()
    if len(sys.argv) == 2 and sys.argv[1] == "--present_databases":
        Databases()
    if len(sys.argv) == 2 and sys.argv[1] == "--create_table":
        create_table()
    if len(sys.argv) == 2 and sys.argv[1] == "--populate":
        Insert_Teacher(1, "ASDAS", 10, "science")
        Insert_Teacher(2, "MISIA", 12, "history")
        Insert_Teacher(3, "M", 12, "history")
        Insert_Teacher(4, "MISIA", 12, "history")
        Insert_Teacher(5, "MISIA", 12, "history")
        Insert_Teacher(6, "Sophia", 12, "Chemistry")
        Insert_Teacher(7, "Daniel", 10, "Biology")
        Insert_Teacher(8, "Emma", 11, "Geography")
        Insert_Teacher(9, "Oliver", 12, "Computer Science")
        Insert_Teacher(10, "Ava", 10, "Physical Education")
        Insert_Teacher(11, "William", 11, "Music")
        Insert_Teacher(12, "Mia", 12, "Art")
        Insert_Teacher(13, "James", 10, "Drama")
        Insert_Teacher(14, "Charlotte", 11, "French")
        Insert_Teacher(15, "Liam", 12, "Spanish")
        Insert_Teacher(16, "Sophie", 10, "German")
        Insert_Teacher(17, "Henry", 11, "Italian")
        Insert_Teacher(18, "Amelia", 12, "Chinese")
        Insert_Teacher(19, "Lucas", 10, "Japanese")
        Insert_Teacher(20, "Ella", 11, "Korean")
        Insert_Teacher(21, "Alexander", 12, "Russian")
        Insert_Teacher(22, "Grace", 10, "Arabic")
        Insert_Teacher(23, "Benjamin", 11, "Swedish")
        Insert_Teacher(24, "Zoe", 12, "Dutch")
        Insert_Teacher(25, "Leo", 10, "Portuguese")
        Insert_Teacher(26, "Lily", 11, "Turkish")
        Insert_Teacher(27, "Mason", 12, "Finnish")
        Insert_Teacher(28, "Aria", 10, "Hungarian")
        Insert_Teacher(29, "Logan", 11, "Polish")
        Insert_Teacher(30, "Scarlett", 12, "Czech")
        Insert_Teacher(31, "Owen", 10, "Slovak")
        Insert_Teacher(32, "Aurora", 11, "Romanian")
        Insert_Teacher(33, "Jackson", 12, "Greek")
        Insert_Teacher(34, "Penelope", 10, "Hebrew")
        Insert_Teacher(35, "Wyatt", 11, "Hindi")
        Insert_Teacher(36, "Nora", 12, "Indonesian")
        Insert_Teacher(37, "Luke", 10, "Malay")
        Insert_Teacher(38, "Sofia", 11, "Vietnamese")
        Insert_Teacher(39, "Carter", 12, "Bengali")
        Insert_Teacher(40, "Madison", 10, "Tagalog")
        Insert_Teacher(41, "Grayson", 11, "Thai")
        Insert_Teacher(42, "Layla", 12, "Mandarin")
        Insert_Teacher(43, "Olivia", 10, "Cantonese")
        Insert_Teacher(44, "Ethan", 11, "Telugu")
        Insert_Teacher(45, "Lillian", 12, "Tamil")
        Insert_Teacher(46, "Sebastian", 10, "Urdu")
        Insert_Teacher(47, "Hannah", 11, "Punjabi")
        Insert_Teacher(48, "Isaac", 12, "Malayalam")
        Insert_Teacher(49, "Abigail", 10, "Kannada")
        Insert_Teacher(50, "Nicholas", 11, "Odia")
    if len(sys.argv) < 2:
        print(f"try py database_fetch.py --help for more options")

    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print("Options for 'database_fetch.py' are:")
        print("  --connect             Connect to the database.")
        print("  --present_databases  List all present databases.")
        print("  --create_table        Create a new table in the database.")
        print("  --populate            Populate the table with data.")
        print("  --uvicorn_run         run fastapi uvicorn server.")
    import uvicorn
    if len(sys.argv) == 2 and sys.argv[1] == "--uvicorn_run":
            import nest_asyncio
            nest_asyncio.apply()
            uvicorn.run("fetch_database:app", host="localhost", port=8000, reload=True)


def fetch_row_as_dict(table_name, row_id):
    conn =None
    try:
        params = config()
        # Establish a database connection
        conn = psycopg2.connect(**params)

        # Create a cursor
        cur = conn.cursor()

        # Execute the SELECT query to fetch a specific row
        cur.execute(f"SELECT * FROM {table_name} WHERE parent_id = %s", (row_id,))

        # Fetch the row
        row = cur.fetchone()

        # Get the column names
        col_names = [desc[0] for desc in cur.description]

        # Create a dictionary using column names and row values
        row_dict = dict(zip(col_names, row))

        return row_dict

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # Close the cursor and connection
        if conn is not None:
            cur.close()
            conn.close()

# Example: Fetch row with parent_id = 1 from Teachers table
result = fetch_row_as_dict("teachers", 1)

if result:
    print(result)
else:
    print("Row not found.")



# import json
# psql_str = json.dumps(result, indent= 4)
# psql_json_obj = json.loads(psql_str)
# type(psql_json_obj)



class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None




@app.get("/")
async def send_user(request : Request):
    
    return templates.TemplateResponse("fetch_postgres.html", {"request": request})





import json
@app.get("/from_db.json")
async def send_user(msg : int):
    data = fetch_row_as_dict("teachers", msg)
    psql_str = json.dumps(data, indent= 4)
    psql_json_obj = json.loads(psql_str)
    return {"response": str(psql_str)}




"""HTTP REQs"""

# GET Requests are intended to retrieve(request) data from a server(do not modify servers state)
#       |__Limited to max number of chatecters
#       |__Supports only string datatypes
#       |__Can be bookmarked
#       |__Remain in browser history
#       |__ Nonsensitives data only
#       |__Only ASCII charecters allowed
# POST Requests are intended to send sata to the server for processing and may modify server's state
#       |__supports different datatypes(string, binary ...)
#       |__ Never cached
#       |__ Not remain in the browser history
#       |__ Cannot be bookmarked
#       |__ No restrictions on the data length
#       |__ Data will be resubmitted on reloading
#       |__ Data not displayed in url
# PUT Requests intended to send data to the server
#       |__ Idempotent
# Connect method intended for 2 way communications(tunnel) with requested resources



# HTMLResponse class of fastapi.responses
#       |__ Pre-built HTML Content:HTML content that is predefined and doesn't change based on user input or other dynamic factors.
#           |__Use Case: You use HTMLResponse when the HTML structure is fixed and doesn't depend on dynamic data.
#               |__ Example : Returning a simple HTML page that displays static information.

# Jinja2Templates class of fastapi.templating
#       |__  HTML content that is generated dynamically based on variables, user input, or other dynamic factors.
#           |__ use Jinja2Templates when you want to render HTML templates with dynamic data. 
#               |__ The HTML structure can change based on the data provided.




# The Union type hint in Python's typing module is used to indicate that a function or variable can accept values of multiple types. 
# It provides flexibility when the actual type may vary, allowing you to specify a broader range of possibilities.
# eg : int, str, bool etc 



# import uvicorn
# import nest_asyncio
# nest_asyncio.apply()
# uvicorn.run(app, host="localhost", port=9000)

