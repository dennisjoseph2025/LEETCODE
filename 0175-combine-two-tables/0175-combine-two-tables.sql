# Write your MySQL query statement below
SELECT P.firstname, P.lastname,a.city,a.state FROM Person AS p LEFT JOIN Address AS A ON p.personID = A.personID;