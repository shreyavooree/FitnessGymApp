import dbOperations.users as users
import dbOperations.sessions as sessions
import dbOperations.equipment as equipment
import datetime

def Trainer(user):
    while(True):
        print("----------------------------------------------------------------------------------------")
        print("Welcome to the Trainer site. Please follow the instructions below to perform actions:\n")
        print("Please choose which page to go to: (To log out, please enter ctrl+C at any point)")
        print("-> Search")
        print("-> Schedule")
        page = input("\nYour choice: ")
        if page == "Search":
            MembersView(user)
        elif page == "Schedule":
            ScheduleView(user)
        else:
            Trainer(user)

def ScheduleView(user):
    print("Trainer Schedule")
    print("-----------")
    print("Your Schedule:")
    trainerSchedule(user)
    print("-----------")
    print("To add a new session, enter 1")
    print("To update a session, enter 2")
    print("To go back to the Trainer homepage, enter 3")
    choice = input("Your choice: ")
    if choice == str(1):
        createSchedule(user)
    elif choice == str(2):
        sessionId = input("Enter Id of session to update: ")
        updateSession(sessionId)
    elif choice == str(3):
        Trainer(user)
    else:
        ScheduleView(user)
    return

def MembersView(user):
    print("Member Search")
    print("-----------")
    print("To search by last name, enter 1")
    print("To search by ID, enter 2")
    print("To view all members, enter 3")
    print("To go back to the Trainer homepage, enter 4")
    choice = input("Your choice: ")
    if choice == str(1):
        last_name = input("Enter user last name: ")
        searchForMemberLastName(last_name)
    elif choice == str(2):
        id = input("Enter user Id: ")
        searchForMembersID(id)
    elif choice == str(3):
        getAllMembers()
    elif choice == str(4):
        Trainer(user)
    else:
        ScheduleView()
    return

def trainerSchedule(user):
    sesses = sessions.getSessionByTrainer(user)
    for sess in sesses:
        sessionId = sess[0]
        sessionTime = sess[1]
        sessionDate = sess[2]
        sessionName = sess[3]
        sessionType = sess[5]
        if sessionType == False:
            sessionType = "Group"
        else:
            sessionType = "Personal"
        sessionRoom = sess[6]
        print("Session Id: " + str(sessionId) + " || Name: " + sessionName + " || Date and Time: " + str(sessionDate) + " " + str(sessionTime) + " || Session Type: " + sessionType + " || Room: " + str(sessionRoom))
    return

def createSchedule(user):
    sessionTime = input("Enter new session time (hh:mm): ")
    sessionDate = input("Enter new session date (yyyy-mm-dd): ")
    sessionName = input("Enter new session name: ")
    sessionType = input("Enter session type (P for personal or G for group): ")
    if sessionType == "P":
        sessionType = True
    else:
        sessionType = False
    viewEquipment()
    equipmentId = input("Enter new session equipment id: ")
    sessions.addSession(datetime.datetime.strptime(sessionTime, '%H:%M').time(), datetime.datetime.strptime(sessionDate, '%Y-%m-%d').date(), sessionName, user, sessionType, None, equipmentId)
    return

def updateSession(sessionId):
    sessionTime = input("Enter new session time (hh:mm): ")
    sessionDate = input("Enter new session date (yyyy-mm-dd): ")
    viewEquipment()
    equipmentId = input("Enter new session equipment id: ")
    sessions.updateSession(sessionId, datetime.datetime.strptime(sessionTime, '%H:%M').time(), datetime.datetime.strptime(sessionDate, '%Y-%m-%d').date(), equipmentId)
    "Session updated"
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

def searchForMemberLastName(last_name):
    members = users.getUserIdByName(last_name)
    for member in members:
        printMember(member)
    return

def searchForMembersID(id):
    members = users.getUserByID(int(id))
    for member in members:
       printMember(member)
    return

def getAllMembers():
    members = users.getAllMembers()
    for member in members:
        printMember(member)
    return

def printMember(member):
    userId = member[0]
    first_name = member[1]
    last_name = member[2]
    email = member[4]
    phone = member[5]
    print("Member Id: " + str(userId) + " || Name: " + first_name + " " + last_name + " || Email: " + email + " || Phone: " + phone)