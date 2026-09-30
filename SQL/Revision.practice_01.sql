create database users;
use users;
drop database users;
--------------------------------------------------------------------------------------------------------------- 
create table customer (
    customer_id int primary key auto_increment,
    name varchar(50) not null,
    email varchar(50) not null,
    city varchar(50) not null,
    age int not null,
    signup_date date default (current_date) not null
);

create table orders(
	order_id int primary key auto_increment,
    customer_id int not null,
    order_date date default (current_date) not null,
    Amount decimal (10,2) not null,
    status varchar(50) default 'Pending' not null,
    foreign key (customer_id) references customer(customer_id)
);

create table products (
	product_id int primary key auto_increment,
    product_name varchar(100) not null,
    category varchar(50) not null,
    price decimal(10,2) not null
);

create table order_items (
	order_id int not null,
    product_id int not null,
    quantity int not null,
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id)
);

create table employees (
	employee_id int primary key auto_increment,
    name varchar(50) not null,
    departement varchar(50) not null,
    salary decimal(10,2) not null,
    manager_id int not null,
    hire_date date default(current_date) not null
);
show tables;
 ---------------------------------------------------------------------------------
insert into customer (name,email,city,age) values 
("Harsh kumar","harshkr53453@gmail.com","Patna",20),
("Ramesh kumar","Ramesh@gmail.com","Muzzafarpur",18),
("Ravi kumar","ravi@gmail.com","Aurangabad",22),
("Rahul kumar","rahul@gmail.com","Patna",20),
("Prashant kumar","prashant@gmail.com","Patna",21),
("Sudhanshu kumar","sudhanshu@gmail.com","Muzzafarpur",14),
("Sukla singh","sukla@gmail.com","Muzzafarpur",45),
("Amit Sharma", "amit@gmail.com", "Gaya", 30),
("Priya Verma", "priya@gmail.com", "Patna", 25),
("Vikram Singh", "vikram@gmail.com", "Bhagalpur", 62),
("Neha Raj", "neha@gmail.com", "Muzzafarpur", 16),
("Deepak Kumar", "deepak@gmail.com", "Darbhanga", 28),
("Anjali Kumari", "anjali@gmail.com", "Patna", 19),
("Rajesh Mishra", "rajesh@gmail.com", "Gaya", 50),
("Suman Rao", "suman@gmail.com", "Aurangabad", 13),
("Aman Gupta", "aman@gmail.com", "Bhagalpur", 24),
("Kriti Sinha", "kriti@gmail.com", "Darbhanga", 35);
    
INSERT INTO orders (customer_id, Amount, status) VALUES 
(1, 150.00, 'Complete'),
(2, 200.00, DEFAULT),
(3, 300.00, DEFAULT),
(4, 400.00, DEFAULT),
(5, 500.00, 'Reject'),
(6, 800.00, DEFAULT),
(7, 900.00, DEFAULT),
(8, 1000.00, DEFAULT),
(9, 1100.00, DEFAULT),
(10, 1200.00, DEFAULT);

insert into products(product_name,category,price) values
('Laptop','Electronics',45000),
('Mobile','Electronics',18000),
('Shirt','Faishons',1200),
('Saree', 'Faishons',3500),
('Table' , 'Furniture',800),
('Chair','Furniture',2200),
('Biscuit','Foods',50),
('Choclates','Foods',100);

insert into order_items(order_id,product_id,quantity) value
(1,3,2),
(2,4,1),
(1,1,1),
(9,8,2),
(7,5,5),
(1,4,2),
(6,8,5),
(3,2,1);

insert into employees(name,departement,salary,manager_id) value
('Sanjay kumar',"Sales",45000,2),
("Manoj kumar","Sales",34000,2),
("Harsh kumar", "IT", 89000,1),
("Ravi kumar","IT",67000,1),
("Rahul kumar", "Electric",340000,3);

select * from customer;
select * from orders;
select * from products;
select * from order_items;
select * from employees;
---------------------------------------------------------------------------------------------------
-- Find customers whose age is between 20 and 30 and who live in either Patna or Delhi. 
select * from customer where age between 20 and 30 and city = 'Patna' or 'Delhi';

-- Find customers whose name starts with A and whose email is not NULL.
select * from customer where name like "A%"  and email is not null;

-- Display customers from oldest to youngest and show only the first 5 records.
select * from customer order by age asc limit 5;  

-- Find the number of customers in each city and show only cities having more than 3 customers.

select distinct city , count(city) from customer group by city having count(customer_id) >= 3;

-- Find the average age, minimum age, and maximum age of customers.
select avg(age) from customer; 
select min(age) from customer;
select max(age) from customer;

--  Create a status column in the orders table and set its default value to 'Pending'



alter table orders add column status varchar(20) default "Pending";

-- Update the city of a particular customer and delete a customer using customer_id

update customer set city = "Delhi" where customer_id =  17;
delete from customer where customer_id = 17;


--  Display every order with the customer's name, city, order date, and amount.
select c.name , c.city , o.order_date , o.total_amount as amount from customer c 
inner join orders o
on c.customer_id = o.customer_id ;

-- Find customers who have never placed an order

select c.customer_id , name, email, city , age, signup_date from customer c 
left join orders o
on c.customer_id = o.customer_id
where order_id is null;

-- find customers who have placed at least one order
select c.customer_id , name , email, city ,age, signup_date from customer c 
inner join orders o
on c.customer_id = o.customer_id 
group by c.customer_id;

-- Calculate the total amount spent by every customer.

select c.customer_id , c.name, coalesce(sum(o.total_amount),0) as total_spend from customer c
left join orders o
on c.customer_id = o.customer_id
group by c.customer_id , c.name;

-- Find the top 5 customers by total spending.
select c.customer_id , c.name , coalesce(sum(o.total_amount),0) as total_spend from customer c 
left join orders o
on c.customer_id = o.customer_id
group by  c.customer_id , c.name  order by total_spend desc limit 5;

-- Find customers whose age is greater than the average age of all customers.
select name,age from customer where age > (select avg(age) from customer); 

-- Find orders whose amount is greater than the average order amount.
select c.name , c.email, c.city , o.total_amount as order_amount from customer c 
inner join orders o
on c.customer_id = o.customer_id 
where total_amount > (select avg(total_amount) from orders);


 
