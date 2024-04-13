from psycopg import connect, DatabaseError, OperationalError

def getAllTransactions():
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM transactions""")

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def getTransactionByUser(userId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM transactions WHERE userId = %s
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

def getTransactionBySession(sessionId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM transactions WHERE sessionId = %s
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

def getTransactionById(transactionId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM transactions WHERE transactionId = %s
        """,
        (transactionId,))

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def addTransaction(userId, sessionId, creditCard, transactionDate, transactionTime):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO transactions (userId, sessionId, creditCard, transactionDate, transactionTime)
        VALUES (%s, %s, %s, %s, %s);
        """,
        (userId, sessionId, creditCard, transactionDate, transactionTime,))
        
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def processTransaction(transactionId, transactionDate, transactionTime):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE transactions SET transactionDate = %s, transactionTime = %s WHERE transactionId = %s
        """,
        (transactionDate, transactionTime, transactionId,))
    
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def deleteTransactionByUser(userId, sessionId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM transactions WHERE userid = %s AND sessionid = %s""",
        (userId, sessionId))
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def deleteTransactionBySession(sessionId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM transactions WHERE sessionid = %s""",
        (sessionId,))

        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

def deleteTransaction(transactionId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM transactions WHERE transactionId = %s""",
        (transactionId,))

        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()