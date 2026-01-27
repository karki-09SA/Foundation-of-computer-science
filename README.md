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
