CREATE TABLE users
    (   userId serial,
        first_name  varchar(255) not null,
        last_name   varchar(255) not null,
        userPassword text,
        email text,
        phone varchar(15),
        accountType integer,
	primary key (userId)
    );

CREATE TABLE biodata
    (   bioId serial,
        userId integer,
        userHeight integer,
        userWeight integer,
        userRHR integer,
	 	date DATE,
    primary key (bioId),
    foreign key (userId) references users
    );

CREATE TABLE goals
    (   goalId serial,
        userId integer, 
        goalType text,
        goalValue integer,
        goalResult BOOLEAN,
    primary key (goalId),
    foreign key (userId) references users
    );

CREATE TABLE routines
    (   routineId serial,
        userId integer, 
        routineName varchar(255) not null,
        routineDescription text,
    primary key (routineId),
    foreign key (userId) references users
    );

CREATE TABLE equipment
    (   equipmentId serial,
        equipmentName varchar(255) not null,
        quantity integer,
        maintenenceDate DATE,
        freq integer,
	 primary key (equipmentId)
    );

CREATE TABLE sessions
    (   sessionId serial,
        sessionTime TIME,
        sessionDate DATE,
        sessionName varchar(255) not null,
        trainerId integer,
        sessionType BOOLEAN,
        sessionRoom integer,
	 	equipmentId integer,
    primary key (sessionId),
    foreign key (trainerId) references users,
    foreign key (equipmentId) references equipment
    );

CREATE TABLE enrolments
    (   enrolmentId serial, 
        sessionId integer, 
        userId integer,
    primary key (enrolmentId),
    foreign key (sessionId) references sessions,
    foreign key (userId) references users
    );

CREATE TABLE transactions
    (   transactionId serial, 
        userId integer, 
        sessionId integer,
        creditCard varchar(255) not null,
        transactionDate DATE,
        transactionTime TIME, 
    primary key (transactionId),
    foreign key (userId) references users
    );
