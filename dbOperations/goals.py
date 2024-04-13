from psycopg import connect, DatabaseError, OperationalError

#get goals by id
def getGoalsbyUserId(userId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM goals WHERE userId = %s
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


def getGoalById(goalId):
    try:
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM goals WHERE goalId = %s
        """,
        (goalId,))

        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

# to add a goal
def addGoal(userId, goalType, goalValue, goalResult):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO goals (userId, goalType, goalValue, goalResult)
        VALUES (%s, %s, %s, %s);
        """,
        (userId, goalType, goalValue, goalResult,))
        
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()
    
# to update a goal's information
def updateGoal(goalId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE goals SET goalResult = TRUE WHERE goalId = %s
        """,
        (goalId,))
    
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

# to delete a goal from the table
def deleteGoal(goalId):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=fitnessGym user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM goals WHERE userId = %s""",
        (goalId,))

        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()