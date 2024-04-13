from psycopg import connect, DatabaseError, OperationalError

def getBioData(userId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM biodata WHERE userId = %s
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


def getMostRecentData(userId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM biodata WHERE userId = %s
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

def addBioData(userId, userHeight, userWeight, userRHR, date):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO biodata (userId, userHeight, userWeight, userRHR, date)
        VALUES (%s, %s, %s, %s, %s);
        """,
        (userId, userHeight, userWeight, userRHR, date,))
        
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def updateBioData(userId, userHeight, userWeight, userRHR, date):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE biodata SET userHeight = %s, userWeight = %s, userRHR = %s, date = %s WHERE userId = %s
        """,
        (userHeight, userWeight, userRHR, userId, date,))
    
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def deleteBioData(userId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM biodata WHERE userId = %s""",
        (userId,))

        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()
