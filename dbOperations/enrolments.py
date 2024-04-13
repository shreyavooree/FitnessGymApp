from psycopg import connect, DatabaseError, OperationalError

def getEnrolments():
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM enrolments""")

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def getEnrolmentsByUser(userId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM enrolments WHERE userId = %s
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

def getEnrolmentsBySession(sessionId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM enrolments WHERE sessionId = %s
        """,
        (sessionId,))

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def addEnrolment(userId, sessionId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO enrolments (sessionId, userId)
        VALUES (%s, %s);
        """,
        (sessionId, userId,))
        
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def deleteEnrolment(userId, sessionId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM enrolments WHERE userId = %s AND sessionId = %s""",
        (userId, sessionId,))

        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def deleteEnrolmentBySession(sessionId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM enrolments WHERE sessionId = %s""",
        (sessionId,))

        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()