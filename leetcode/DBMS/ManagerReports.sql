-- 570. Managers with at Least 5 Direct Reports


SELECT e.name
FROM Employee e
JOIN Employee x
ON e.id = x.managerId
GROUP BY e.id, e.name
HAVING COUNT(*) >= 5;