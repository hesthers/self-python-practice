# Write your MySQL query statement below
select name
from Employee 
where ID in (
    select managerID from Employee
    group by managerID
    having count(ManagerId) >= 5
  )
