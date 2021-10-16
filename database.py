'''
    Python is very easy to connect to a database. It uses Python database API for the connection and to provide the
    methods to perform operation on our database. It is not limited to any certain database, we can connect to any 
    database of our choice such as Oracle, MySQL, PostgerSQL, MongoDB, SQLite and any other follwing the same steps.

    1. Import the module of the respective database.
    2. Open a connection to a database (methods are provided by the Python Database API)
    3. Create a cursor, this helps in executing the query and stores the result of the query.
    4. Execute the SQL query.
    5. Fetch the result returned by SQL query.
    6. Close the cursor and connection to the database.
'''

# Importing the database module
import sqlite3

conn = None

try :
    
    # Opening a connection to the database
    conn = sqlite3.connect('sqlite_database.db')
    print('Connected successfully to the databases')

    # creating a cursor
    cur = conn.cursor()
    print('Created a cursor')

    # creating a query
    # the string can also directly be passed to the execute method.
    query = '''
        CREATE TABLE IF NOT EXISTS students (
            id integer PRIMARY KEY,
            name text NOT NULL,
            course text NOT NULL
        )
    '''
    cur.execute(query)

    # query to insert data into created table
    insert_query = '''
        INSERT INTO students(name, course) VALUES
        ( 'Ankit', 'CSE' ),
        ( 'Prateek', 'CSE' ),
        ( 'Sushant', 'CSE' );
    '''
    cur.execute(insert_query)

    # getting the row count inserted in the table
    print(cur.rowcount)

    # commiting changes to the database.
    conn.commit()


except sqlite3.DatabaseError() as e:
    print(e)

finally:
    if conn is not None:
        cur.close()
        conn.close()



