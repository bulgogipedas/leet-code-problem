SELECT 
    E.name,
    CASE WHEN B.bonus < 1000 THEN B.bonus ELSE NULL END AS bonus
FROM 
    Employee E
LEFT JOIN 
    Bonus B ON E.empId = B.empId
WHERE 
    B.bonus < 1000 OR B.bonus IS NULL;
