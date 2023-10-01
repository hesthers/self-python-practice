# Write your MySQL query statement below

select v.customer_id, count(v.visit_id) as count_no_trans
from Visits as v
left join Transactions as t
on v.visit_id = t.visit_id 
where t.visit_id is null
group by v.customer_id
-- having count(t.visit_id) = 0