INSERT INTO Student (StudentID, StudentName, Email)
VALUES (8, 'Priya', 'priya@email.com');

/*
Expected Output:
1 row(s) affected.

SELECT * FROM Student WHERE StudentID = 8;
+-----------+-------------+-----------------+
| StudentID | StudentName | Email           |
+-----------+-------------+-----------------+
|     8     |    Priya    | priya@email.com |
+-----------+-------------+-----------------+
*/

INSERT INTO Club (ClubID, ClubName, ClubRoom, ClubMentor)
VALUES ('C05', 'Art Club', 'R404', 'Ms. Lata');

/*
Expected Output:
1 row(s) affected.

SELECT * FROM Club WHERE ClubID = 'C05';
+--------+----------+----------+------------+
| ClubID | ClubName | ClubRoom | ClubMentor |
+--------+----------+----------+------------+
|  C05   | Art Club |   R404   |  Ms. Lata  |
+--------+----------+----------+------------+
*/

SELECT * FROM Student;

/*
Expected Output:
+-----------+-------------+-------------------+
| StudentID | StudentName | Email             |
+-----------+-------------+-------------------+
|     1     |    Asha     | asha@email.com    |
|     2     |   Bikash    | bikash@email.com  |
|     3     |    Nisha    | nisha@email.com   |
|     4     |    Rohan    | rohan@email.com   |
|     5     |    Suman    | suman@email.com   |
|     6     |    Pooja    | pooja@email.com   |
|     7     |    Aman     | aman@email.com    |
|     8     |    Priya    | priya@email.com   |
+-----------+-------------+-------------------+
8 rows in set
*/

SELECT * FROM Club;

/*
Expected Output:
+--------+-------------+----------+------------+
| ClubID | ClubName    | ClubRoom | ClubMentor |
+--------+-------------+----------+------------+
|  C01   | Music Club  |   R101   | Mr. Raman  |
|  C02   | Sports Club |   R202   |  Ms. Sita  |
|  C03   | Drama Club  |   R303   | Mr. Kiran  |
|  C04   | Coding Club |   Lab1   |  Mr. Anil  |
|  C05   | Art Club    |   R404   |  Ms. Lata  |
+--------+-------------+----------+------------+
5 rows in set
*/

SELECT
    s.StudentName,
    c.ClubName,
    m.JoinDate
FROM Student s
JOIN Membership m ON s.StudentID = m.StudentID
JOIN Club c       ON m.ClubID    = c.ClubID
ORDER BY s.StudentName, m.JoinDate;

/*
Expected Output:
+-------------+-------------+------------+
| StudentName | ClubName    | JoinDate   |
+-------------+-------------+------------+
|    Aman     | Coding Club | 2024-01-30 |
|    Asha     | Music Club  | 2024-01-10 |
|    Asha     | Sports Club | 2024-01-15 |
|   Bikash    | Sports Club | 2024-01-12 |
|   Bikash    | Drama Club  | 2024-01-25 |
|    Nisha    | Music Club  | 2024-01-20 |
|    Nisha    | Coding Club | 2024-01-28 |
|    Pooja    | Sports Club | 2024-01-27 |
|    Rohan    | Drama Club  | 2024-01-18 |
|    Suman    | Music Club  | 2024-01-22 |
+-------------+-------------+------------+
10 rows in set
*/

SELECT
    c.ClubName,
    COUNT(m.StudentID) AS TotalMembers
FROM Club c
JOIN Membership m ON c.ClubID = m.ClubID
GROUP BY c.ClubName
ORDER BY TotalMembers DESC;

/*
Expected Output:
+-------------+--------------+
| ClubName    | TotalMembers |
+-------------+--------------+
| Music Club  |      3       |
| Sports Club |      3       |
| Drama Club  |      2       |
| Coding Club |      2       |
+-------------+--------------+
4 rows in set
*/

SELECT
    s.StudentName,
    COUNT(m.ClubID) AS ClubsJoined
FROM Student s
JOIN Membership m ON s.StudentID = m.StudentID
GROUP BY s.StudentName
HAVING COUNT(m.ClubID) > 1
ORDER BY ClubsJoined DESC;

/*
Expected Output:
+-------------+-------------+
| StudentName | ClubsJoined |
+-------------+-------------+
|    Asha     |      2      |
|   Bikash    |      2      |
|    Nisha    |      2      |
+-------------+-------------+
3 rows in set
*/
