from psycopg import connect, DatabaseError, OperationalError

def validateUser(userId, password):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        cursor.execute("""
        SELECT accounttype FROM users WHERE userId = %s AND userpassword = %s
        """,
        (userId,password,))
        conn.commit()
        data = cursor.fetchall()
        if data is not None:
            cursor.close()
            conn.close()
            return data[0][0]
        cursor.close()
        conn.close()
        return False
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def getAllMembers():
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM users WHERE accountType = %s
        """,
        (1,))

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

#get user by id
def getUserByID(userId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM users WHERE userId = %s
        """,
        (userId,))

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

#get user by last name
def getUserIdByName(phone):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM users WHERE last_name = %s
        """,
        (phone,))

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()


def getUserIdByPhone(phone):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT userId FROM users WHERE phone = %s
        """,
        (phone,))

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data[0][0]
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

# to add a user
def addUser(first_name, last_name, email, password, phone, accountType):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO users (first_name, last_name, userPassword, email, phone, accountType)
        VALUES (%s, %s, %s, %s, %s, %s);
        """,
        (first_name, last_name, password, email, phone, accountType))
        
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()
    
# to update a user's information
def updateUser(userId, first_name, last_name, email, password, phone):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE users SET first_name = %s, last_name = %s, email = %s, userpassword =  %s, phone = %s WHERE userId = %s
        """,
        (first_name, last_name, email, password, phone, userId,))
    
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

# to delete a student from the table
def deleteUser(userId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM users WHERE userId = %s""",
        (userId,))

        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()