DROP TABLE IF EXISTS Membership;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Club;

CREATE TABLE Student (
    StudentID   INT          NOT NULL,
    StudentName VARCHAR(100) NOT NULL,
    Email       VARCHAR(150) NOT NULL UNIQUE,
    PRIMARY KEY (StudentID)
);

CREATE TABLE Club (
    ClubID      VARCHAR(10)  NOT NULL,
    ClubName    VARCHAR(100) NOT NULL,
    ClubRoom    VARCHAR(50)  NOT NULL,
    ClubMentor  VARCHAR(100) NOT NULL,
    PRIMARY KEY (ClubID)
);

CREATE TABLE Membership (
    StudentID   INT         NOT NULL,
    ClubID      VARCHAR(10) NOT NULL,
    JoinDate    DATE        NOT NULL,
    PRIMARY KEY (StudentID, ClubID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClubID)    REFERENCES Club(ClubID)
);

INSERT INTO Student (StudentID, StudentName, Email) VALUES
(1, 'Asha',   'asha@email.com'),
(2, 'Bikash', 'bikash@email.com'),
(3, 'Nisha',  'nisha@email.com'),
(4, 'Rohan',  'rohan@email.com'),
(5, 'Suman',  'suman@email.com'),
(6, 'Pooja',  'pooja@email.com'),
(7, 'Aman',   'aman@email.com');

INSERT INTO Club (ClubID, ClubName, ClubRoom, ClubMentor) VALUES
('C01', 'Music Club',  'R101', 'Mr. Raman'),
('C02', 'Sports Club', 'R202', 'Ms. Sita'),
('C03', 'Drama Club',  'R303', 'Mr. Kiran'),
('C04', 'Coding Club', 'Lab1', 'Mr. Anil');

INSERT INTO Membership (StudentID, ClubID, JoinDate) VALUES
(1, 'C01', '2024-01-10'),
(2, 'C02', '2024-01-12'),
(1, 'C02', '2024-01-15'),
(3, 'C01', '2024-01-20'),
(4, 'C03', '2024-01-18'),
(5, 'C01', '2024-01-22'),
(2, 'C03', '2024-01-25'),
(6, 'C02', '2024-01-27'),
(3, 'C04', '2024-01-28'),
(7, 'C04', '2024-01-30');

SELECT 'Student Table' AS TableName, COUNT(*) AS TotalRows FROM Student
UNION ALL
SELECT 'Club Table',       COUNT(*) FROM Club
UNION ALL
SELECT 'Membership Table', COUNT(*) FROM Membership;
