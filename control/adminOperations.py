import dbOperations.equipment as equipment
import dbOperations.sessions as sessions
import dbOperations.transactions as transactions
import dbOperations.enrolments as enrolments
import datetime

def Admin():
    while(True):
        print("----------------------------------------------------------------------------------------")
        print("Welcome to the Admin site. Please follow the instructions below to perform actions:\n")
        print("Please choose which page to go to: (To log out, please enter ctrl+C at any point)")
        print("-> Sessions")
        print("-> Equipment")
        print("-> Transactions")
        page = input("\nYour choice: ")
        if page == "Sessions":
            SessionView()
        elif page == "Equipment":
            EquipmentView()
        elif page == "Transactions":
            TransactionView()
        else:
            Admin()

def SessionView():
    print("Sessions")
    print("-----------")
    viewSessions()
    print("-----------")
    print("To book rooms for sessions, enter 1")
    print("To update a session, enter 2")
    print("To cancel a session, enter 3")
    print("To go back to the Admin homepage, enter 4")
    choice = input("Your choice: ")
    if choice == str(1):
        sessionId = input("Enter Id of session to book a room for: ")
        roomNo = input("Enter room number for booking: ")
        bookRoomForSession(sessionId, roomNo)
    elif choice == str(2):
        sessionId = input("Enter Id of session to update: ")
        updateSession(sessionId)
    elif choice == str(3):
        sessionId = input("Enter Id of session to cancel: ")
        cancelSession(sessionId)
    elif choice == str(4):
        Admin()
    else:
        SessionView()
    return

def EquipmentView():
    print("Equipment")
    print("-----------")
    viewEquipment()
    print("-----------")
    print("To update equipment, enter 1")
    print("To add equipment, enter 2")
    print("To remove equipment, enter 3")
    print("To go back to the Admin homepage, enter 4")
    choice = input("Your choice: ")
    if choice == str(1):
        equipmentId = input("Enter Id of equipment update: ")
        updateEquipment(equipmentId)
    elif choice == str(2):
        addEquipment()
    elif choice == str(3):
        equipmentId = input("Enter Id of equipment remove: ")
        removeEquipment(equipmentId)
    elif choice == str(4):
        Admin()
    else:
        EquipmentView()
    return

def TransactionView():
    print("Transactions")
    print("-----------")
    viewTransactions()
    print("-----------")
    print("To process a transaction, enter 1")
    print("To go back to the Admin homepage, enter 2")
    choice = input("Your choice: ")
    if choice == str(1):
        transId = input("Enter transaction id to process: ")
        processPayment(transId)
    elif choice == str(2):
        Admin()
    else:
        TransactionView()
    return

def viewSessions():
    allSessions = sessions.getAllSessions()
    for session in allSessions:
        sessionId = session[0]
        sessionTime = session[1]
        sessionDate = session[2]
        sessionName = session[3]
        trainerId = session[4]
        sessionType = session[5]
        if sessionType == False:
            sessionType = "Group"
        else:
            sessionType = "Personal"
        sessionRoom = session[6]
        equipmentId = session[7]
        print("Session Id: " + str(sessionId) + " || Name: " + sessionName + " || Date and Time: " + str(sessionDate) + " " + str(sessionTime) + " || Trainer Id: " + str(trainerId) + " || Session Type: " + sessionType + " || Room: " + str(sessionRoom) + " || Equipment Id: " + str(equipmentId))
    return

def bookRoomForSession(sessionId, roomNo):
    sessions.updateSessionRoom(sessionId, roomNo)
    print("Updated room")
    return

def updateSession(sessionId):
    sessionTime = input("Enter new session time (hh:mm): ")
    sessionDate = input("Enter new session date (yyyy-mm-dd): ")
    sessionRoom = input("Enter new session room: ")
    viewEquipment()
    equipmentId = input("Enter new session equipment id: ")
    sessions.updateSessionAdmin(sessionId, datetime.datetime.strptime(sessionTime, '%H:%M').time(), datetime.datetime.strptime(sessionDate, '%Y-%m-%d').date(), sessionRoom, equipmentId)
    "Session updated"
    return

def cancelSession(sessionId):
    enrolments.deleteEnrolmentBySession(int(sessionId))
    transactions.deleteTransactionBySession(int(sessionId))
    sessions.deleteSession(int(sessionId))
    return

def viewEquipment():
    equips = equipment.getEquipment()
    for equip in equips:
        equipmentId = equip[0]
        equipmentName = equip[1]
        quantity = equip[2]
        maintenenceDate = equip[3]
        freq = equip[4]
        print("Equipment Id: " + str(equipmentId) + " || Name: " + equipmentName + " || Quantity: " + str(quantity) + " || Last Maintenance Date: " + str(maintenenceDate) + " || Frequency of maintenance (Days): " + str(freq))
    return

def updateEquipment(equipmentId):
    equipmentName = input("Enter new equipment name: ")
    quantity = input("Enter new equipment quantity: ")
    maintenanceDate = input("Enter new maintenance date (yyyy-mm-dd): ")
    freq = input("Enter new frequency of update: ")
    equipment.updateEquipment(equipmentId, equipmentName, int(quantity), datetime.datetime.strptime(maintenanceDate, '%Y-%m-%d'), int(freq))
    print("Updated equipment")
    return

def addEquipment():
    equipmentName = input("Enter new equipment name: ")
    quantity = input("Enter new equipment quantity: ")
    maintenanceDate = input("Enter new maintenance date (yyyy-mm-dd): ")
    freq = input("Enter new frequency of update: ")
    equipment.addEquipment(equipmentName, int(quantity), datetime.datetime.strptime(maintenanceDate, '%Y-%m-%d'), int(freq))
    print("Added equipment")
    return

def removeEquipment(equipmentId):
    if len(sessions.getSessionByEquipmentId(equipmentId)) > 0:
        print("This equipment is scheduled to be used by these sessions:")
        sesss = sessions.getSessionByEquipmentId(equipmentId)
        for sess in sesss:
            print(sess)
        print("To remove anyways, enter 1")
        print("To cancel corresponding sessions and remove equipment, enter 2")
        print("To nullify operation, enter 3")
        choice = input("Your choice: ")
        if choice == str(1):
            equipment.deleteEquipment(equipmentId)
        elif choice == str(2):
            for sess in sesss:
                cancelSession(sess[0])
                equipment.deleteEquipment(equipmentId)
        else:
            return
    equipment.deleteEquipment(equipmentId)
    return

def viewTransactions():
    trans = transactions.getAllTransactions()
    for tran in trans:
        transactionId = tran[0]
        userId = tran[1]
        sessionId = tran[2]
        creditCard = tran[3]
        transactionDate = tran[4]
        transactionTime = tran[5]
        print("Transaction Id: " + str(transactionId) + " || User Id: " + str(userId) + " || Session Id: " + str(sessionId) + " || Credit Card: " + creditCard + " || Transaction Date: " + str(transactionDate) + " || Transaction Time: " + str(transactionTime))
    return

def processPayment(transactionId):
    transactions.processTransaction(transactionId, datetime.date.today(), datetime.datetime.now().time())
    print("Transaction processed")
    return