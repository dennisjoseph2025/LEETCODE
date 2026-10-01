# Write your MySQL query statement below
SELECT c.name AS Customers FROM Customers AS c LEFT JOIN Orders AS O ON c.id = o.CustomerId WHERE o.customerId IS NULL;