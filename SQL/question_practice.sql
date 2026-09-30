use users;

--  Select all employees.
select * from employees;

--  Select employee name, department and salary.
select name , departement , salary from employees;

-- List unique cities
select distinct(city) from customer;

--  Find employees earning at least 50000
select name, salary as Earning from employees 
where salary >=50000; 

-- Find employee in IT or HR
select * from employees where departement = 'IT' or 'HR';  

-- Find customers from Patna, Delhi or Mumbai
select * from customer where city = 'Patna' or 'Delhi' or 'Mumbai'; 

--  Find salaries between 40000 and 70000
select * from employees where salary between 40000 and 70000;

-- Find names starting with A
select * from customer where name like 'A%';

-- Find emails ending in gmail.com.
select * from customer where email like '%gmail.com';

--  Find customers with missing city
select * from customer where city is null;

-- • Find customers whose email is not NULL.
select * from customer where email is not null;

-- • Sort employees by salary descending.
select * from employees order by salary desc;  

-- Return the top 5 highest salaries.
select * from employees order by salary desc limit 5;

-- Return the 5 lowest salaries. 
select * from employees order by salary asc limit 5;

-- Calculate annual salary.
select name ,(salary*12) as anual_salary from employees;

-- Exclude customers from Patna
 select * from customer where city != 'Patna';
 
 -- Return the 10 most recent orders.
select * from orders order by order_date ;

-- Count all employees
select count(*) as total_employee from employees;

-- • Count employees with non-NULL salary.
select count(*) as total_employee from employees where salary is not null; 

--  Count unique cities.
select count(distinct(city)) as total_city from customer;  

-- Calculate total salary
select sum(salary) as total_salary from employees ;

-- count min , max , and avg salary
select min(salary) as minimum_salary from employees;    
select max(salary) as maximum_salary from employees;
select avg(salary) as average_salary from employees;

--  Calculate average salary by department.
select departement , avg(salary) average_salary from employees group by departement;

-- • Find departments with average salary above 50000
select departement, avg(salary) as avg_salary from employees group by departement having avg_salary > 50000;

-- • Find cities with more than 10 customers.
select city , count(city) as total_customer from customer group by city having total_customer > 1;

-- Convert name to uppercase
select upper(name) from customer;

-- Convert emial to lowercase
select lower(email) from customer;

-- Trim customer name
select trim(name) from customer;

-- Extract year from order_date
select year(order_date) as year from orders;

--  Extract month and day.
select day(order_date), (order_date) as order_month from orders; 

--  Calculate days since order_date
select datediff(current_date , order_date) as day_Ago from orders;  

-- Replace null with unknow

select city , coalesce('city','unknow') as city from customer; 

--  Clean an email using LOWER(TRIM()).

select lower(trim(email)) as clean_email from customer; 

-- • Inner join customers and orders.
select c.name , c.email, c.city , o.Amount , o.status from customer c 
inner join orders o 
on c.customer_id = o.customer_id;

-- left join customer and orders
select c.name , c.city , o.Amount , o.status from customer c 
left join orders o
on c.customer_id = o.customer_id where o.Amount;

--  Find customers with no orders
select c.name,c.email , coalesce(o.Amount,0) as Order_Amount, coalesce(o.status,'No orders') as Status from customer c
left join orders o
on c.customer_id = o.customer_id where Amount is null; 

-- • Find products never ordered.
select p.product_name , p.category , p.price , coalesce(o.quantity,0) as Quantity from products p 
left join order_items o
on p.product_id = o.product_id where quantity is null;

-- Join three tables: customers, order_items and products.
select c.* , o.* , p.* from customer c
inner join orders o , order_items p 
where c.customer_id = o.customer_id and o.order_id = p.order_id;

-- • Combine two customer lists with UNION.
select * from customer 
union
select * from customer;
 
-- Append two sales tables with UNION ALL.
select * from customer
union all 
select * from customer;

select name , salary , (select avg(salary) from employees) as overall_salary 
from employees;
 
-- Find employees above overall average salary.
 select * from employees where salary > (select avg(salary) from employees);
 
 -- Find emplyees below average salary.
 select * from employees where salary < (select avg(salary) from employees);
 
 -- Find products above average price.
select product_name , price from products where price > (select avg(price) from products); 

-- Create high / low salary levels
select * ,case when  salary >= 25000 then "High" else "Low" end as salary_group from employees;

-- • Create four age groups.
select name,age ,email ,case 
when age <=10 then "Child" 
when age <= 18 then "Aduld"
when age <= 30 then "old"
else "pure old" end as age_group from customer;
 
