# University Database Normalization (1NF–3NF) using MySQL

## Objective
The objective of this assignment is to normalize an unnormalized
university registration dataset into First Normal Form (1NF),
Second Normal Form (2NF), and Third Normal Form (3NF), and implement
the final schema using MySQL.

---

## Identified Functional Dependencies
- StudentID → Name, Email, Major
- Major → Advisor
- CourseID → CourseTitle, Credits, Building, Room
- (StudentID, CourseID) → Grade

---

## Normalization Process

### First Normal Form (1NF)
All attributes contain atomic values and there are no repeating groups.
Therefore, the given table already satisfies 1NF.

### Second Normal Form (2NF)
Partial dependencies were removed by separating attributes that
depend only on part of the composite key (StudentID, CourseID).
The table was decomposed into Students, Courses, and Enrollments.

### Third Normal Form (3NF)
Transitive dependency StudentID → Major → Advisor was removed by
creating a separate Majors table.

---

## Final Tables (3NF)
- Majors (Major, Advisor)
- Students (StudentID, Name, Email, Major)
- Courses (CourseID, CourseTitle, Credits, Building, Room)
- Enrollments (StudentID, CourseID, Grade)

---

## MySQL Implementation Shown Step by Step 

### 1.Create Database
```sql
CREATE DATABASE university_db;
USE university_db;
```

### 2.Create Majors Table
```sql
CREATE TABLE Majors (
    Major VARCHAR(50) PRIMARY KEY,
    Advisor VARCHAR(50) NOT NULL
);
```
### 3.Create Student Table
```sql
CREATE TABLE Students (
    StudentID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Major VARCHAR(50),
    FOREIGN KEY (Major) REFERENCES Majors(Major)
);
```
### 4.Create Courses Table
```sql
CREATE TABLE Courses (
    CourseID VARCHAR(10) PRIMARY KEY,
    CourseTitle VARCHAR(100) NOT NULL,
    Credits INT NOT NULL,
    Building VARCHAR(50),
    Room VARCHAR(10)
);
```
### 5.Create Enrollments Table
```sql
CREATE TABLE Enrollments (
    StudentID VARCHAR(10),
    CourseID VARCHAR(10),
    Grade CHAR(1),
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
```
### 6. Inserting Sample Values
```sql
INSERT INTO Majors VALUES
('CS', 'Dr. Smith'),
('Physics', 'Dr. Lee');

INSERT INTO Students VALUES
('S101', 'Alice', 'alice@uni.edu', 'CS'),
('S102', 'Bob', 'bob@uni.edu', 'CS'),
('S103', 'Carol', 'carol@uni.edu', 'Physics');

INSERT INTO Courses VALUES
('CS301', 'Algorithms', 4, 'Science', '205'),
('MATH201', 'Linear Algebra', 3, 'Math Wing', '101'),
('PHYS101', 'Mechanics', 4, 'Science', '301');

INSERT INTO Enrollments VALUES
('S101', 'CS301', 'A'),
('S101', 'MATH201', 'B'),
('S102', 'CS301', 'C'),
('S103', 'PHYS101', 'A');
```
### Verification Query 
This sql query reconstucts the original table.
```sql
SELECT
    s.StudentID,
    s.Name,
    s.Email,
    s.Major,
    m.Advisor,
    c.CourseID,
    c.CourseTitle,
    c.Credits,
    e.Grade,
    c.Building,
    c.Room
FROM Students s
JOIN Majors m ON s.Major = m.Major
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID;
```
## Author 
Sachit Karki
