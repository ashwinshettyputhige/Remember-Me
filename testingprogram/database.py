import mysql.connector
def check_user(name,password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="chat"
    )
    cursor = mydb.cursor()
    query = "SELECT COUNT(*) FROM users WHERE name = %s and password = %s"
    cursor.execute(query, (name,password))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Check if the name exists
    if result > 0:
       return 1
    else:
        return  0

    mydb.close()


def create_user(name , password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="chat"
    )
    cursor = mydb.cursor()
    query = "INSERT INTO users(name,password) VALUES(%s,%s)"
    cursor.execute(query, (name, password))

    # Fetch the result
    # Fetch the response
    response = cursor.lastrowid  # Returns the ID of the last inserted row
    print("Inserted with ID:", response)

    # Check if the name exists
    # if result > 0:
    #     return 1
    # else:
    #     return 0

    mydb.commit()

    # Close the cursor and the database connection
    cursor.close()
    mydb.close()


