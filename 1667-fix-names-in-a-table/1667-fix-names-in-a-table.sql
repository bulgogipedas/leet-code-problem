# Write your MySQL query statement below
select 
    users.user_id,
    CONCAT(UCASE(SUBSTRING(name, 1, 1)), LCASE(SUBSTRING(name, 2))) as name
from users
ORDER BY user_id;

