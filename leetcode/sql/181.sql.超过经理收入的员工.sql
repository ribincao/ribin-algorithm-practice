# Write your MySQL query statement below
# select
#     A.Name as 'Employee'
# from
#     Employee as A,
#     Employee as B
# where
#     A.ManagerId = B.Id
#     and A.Salary > B.Salary
# ;

select 
    A.Name as Employee
from 
    Employee as A join Employee as B
    on A.ManagerId = B.Id
    and A.Salary > B.Salary
;

