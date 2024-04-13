INSERT INTO users (first_name, last_name, userPassword, email, phone, accountType)
VALUES
    ('John', 'Doe', 'password123', 'john.doe@example.com', '1234567890', 1),
    ('Jane', 'Smith', 'p@ssw0rd', 'jane.smith@example.com', '0987654321', 1),
    ('Michael', 'Johnson', 'securepass', 'michael.johnson@example.com', '5555555555', 1),
    ('Regina', 'George', 'password123', 'john.doe@example.com', '12343244433', 2),
    ('Janis', 'Ian', 'p@ssw0rd', 'jane.smith@example.com', '2347753344', 2),
    ('Cady', 'Heron', 'securepass', 'michael.johnson@example.com', '3315532255', 2),
    ('Admin', 'Admin', 'admin', 'admin@voorefitness.com', '0000000000', 3);
    
INSERT INTO biodata (userId, userHeight, userWeight, userRHR, date)
VALUES
    (1, 180, 75, 60, '2024-04-01'),
    (2, 165, 70, 65, '2024-04-02'),
    (3, 175, 80, 70, '2024-04-03'),
    (1, 180, 75, 55, '2024-04-04'),
    (2, 165, 60, 60, '2024-04-05'),
    (3, 175, 80, 65, '2024-04-06'),
    (1, 180, 55, 50, '2024-04-07'),
    (2, 165, 60, 75, '2024-04-08'),
    (3, 175, 80, 70, '2024-04-09'),
    (1, 180, 85, 55, '2024-04-10'),
    (2, 165, 60, 95, '2024-04-11'),
    (3, 175, 50, 50, '2024-04-12');

INSERT INTO goals (userId, goalType, goalValue, goalResult)
VALUES
    (1, 'Weight Loss', 5, true),
    (1, 'Squat PR (lbs)', 315, false),
    (1, 'Endurance (cardio time)', 20, true),
    (1, 'Bench PR (kg)', 50, false),
    (2, 'Biking (km)', 10, false),
    (2, 'Swim (Hours)', 20, true),
    (2, 'Stretch and Mobility (hours)', 5, true),
    (2, 'Weight Loss', 5, false),
    (3, 'Squat PR (lbs)', 315, false),
    (3, 'Endurance (cardio time)', 20, true),
    (3, 'Bench PR (kg)', 50, true),
    (3, 'Biking (km)', 10, false),
    (3, 'Swim (Hours)', 20, false),
    (3, 'Stretch and Mobility (hours)', 5, false);

INSERT INTO routines (userId, routineName, routineDescription)
VALUES
    (1, 'Morning Stretch', 'Stretching exercises to start the day feeling refreshed'),
    (1, 'Evening Yoga', 'Yoga poses for relaxation and flexibility'),
    (1, 'Cardio Workout', 'High-intensity cardio exercises for fitness'),
    (2, 'Strength Training', 'Weightlifting routine for building muscle strength'),
    (2, 'Lunchtime Walk', 'Brisk walk during lunch break for a midday energy boost'),
    (2, 'Core Strengthening', 'Exercises targeting abdominal and lower back muscles'),
    (3, 'Flexibility Focus', 'Stretching routine to improve overall flexibility'),
    (3, 'Circuit Training', 'Rotating through different exercises for a full-body workout'),
    (3, 'Meditation', 'Mindfulness practice for relaxation and mental clarity');

INSERT INTO equipment (equipmentName, quantity, maintenenceDate, freq)
VALUES
    ('Treadmill', 5, '2023-12-01', 30),
    ('Dumbbells', 20, '2023-11-15', 60),
    ('Yoga Mats', 15, '2023-12-05', 90),
    ('Elliptical Machine', 3, '2024-01-10', 45),
    ('Exercise Balls', 10, '2023-11-30', 60),
    ('Resistance Bands', 25, '2023-12-20', 90),
    ('Rowing Machine', 2, '2024-02-05', 60),
    ('Stationary Bike', 4, '2023-12-15', 90),
    ('Barbell Set', 10, '2023-11-20', 90),
    ('Jump Ropes', 15, '2024-01-25', 30),
    ('Pull-Up Bar', 3, '2024-02-10', 60),
    ('Kettlebells', 8, '2023-12-10', 90);

INSERT INTO sessions (sessionTime, sessionDate, sessionName, trainerId, sessionType, sessionRoom, equipmentId)
VALUES
    ('10:00', '2024-04-15', 'Morning Yoga', 4, TRUE, 101, 3),
    ('15:30', '2024-04-17', 'Cardio Blast', 4, FALSE, 103, 1),
    ('18:00', '2024-04-19', 'Strength Training', 4, TRUE, 102, 2),
    ('12:30', '2024-04-21', 'Flexibility Workshop', 4, TRUE, 104, 4),
    ('09:00', '2024-04-23', 'HIIT Circuit', 4, FALSE, 105, 6),
    ('16:45', '2024-04-25', 'Functional Fitness', 4, TRUE, 106, 5),
    ('17:30', '2024-04-27', 'Core Conditioning', 4, TRUE, 107, 3),
    ('14:00', '2024-04-16', 'Pilates Fusion', 5, TRUE, 108, 7),
    ('11:30', '2024-04-18', 'Beginner Strength', 5, FALSE, 109, 8),
    ('19:00', '2024-04-20', 'Zumba Party', 5, TRUE, 110, 9),
    ('08:45', '2024-04-22', 'Morning Stretch', 5, TRUE, 111, 10),
    ('17:15', '2024-04-24', 'Bodyweight Bootcamp', 5, FALSE, 112, 11),
    ('13:20', '2024-04-26', 'Meditation & Mindfulness', 5, TRUE, 113, 12),
    ('16:00', '2024-04-28', 'Cycling Challenge', 5, FALSE, 114, 1),
    ('10:30', '2024-04-29', 'Functional Training', 5, TRUE, 115, 4),
    ('18:45', '2024-04-30', 'Yoga for Relaxation', 5, TRUE, 116, 5),
    ('15:20', '2024-05-01', 'Cardio Kickboxing', 5, FALSE, 117, 6),
    ('12:10', '2024-05-02', 'Interval Training', 6, TRUE, 118, 7),
    ('08:00', '2024-05-03', 'Morning Run Group', 6, FALSE, 119, 8),
    ('19:30', '2024-05-04', 'Powerlifting Workshop', 6, TRUE, 121, 9),
    ('16:50', '2024-05-05', 'Tai Chi Practice', 6, TRUE, 121, 2),
    ('14:40', '2024-05-06', 'HIIT Challenge', 6, FALSE, 122, 1),
    ('11:00', '2024-05-07', 'Beginner Yoga', 6, TRUE, 123, 12),
    ('18:20', '2024-05-08', 'Strength & Conditioning', 6, TRUE, 124, 10),
    ('13:45', '2024-05-09', 'Pilates Matwork', 6, FALSE, 125, 11),
    ('17:00', '2024-05-10', 'Functional Movement', 6, TRUE, 126, 5),
    ('10:15', '2024-05-11', 'Morning Circuit', 6, TRUE, 127, 7);

INSERT INTO enrolments (sessionId, userId)
SELECT 
    floor(random() * 20) + 1 as sessionId,
    floor(random() * 3) + 1 as userId
FROM generate_series(1, 50) s;

INSERT INTO transactions (userId, sessionId, creditCard, transactionDate, transactionTime)
SELECT 
    e.userId,
    e.sessionId,
    concat(floor(random() * 9999) + 1000, '-', floor(random() * 9999) + 1000, '-', floor(random() * 9999) + 1000, '-', floor(random() * 9999) + 1000) as creditCard,
    current_date - floor(random() * 365) * '1 day'::interval as transactionDate,
    (current_time - floor(random() * 86400) * '1 second'::interval)::time as transactionTime
FROM enrolments e;