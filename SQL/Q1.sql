-- Practice Qs 1

-- Qs: Create a database for your company named XYZ.

-- Step 1: create a table inside this DB to store employee info (id, name and salary).

-- Step 2: Add following information in the DB:
--     1, "adam", 25000
--     2, "bob", 30000
--     3, "casey", 40000 

-- Step 3: Select & view all your table data. 

create table employee (
    id int primary key,
    name VARCHAR(50),
    salary int NOT NULL
    );

insert into employee (id,name,salary) values(1,'Akarsh',25000);

SELECT * FROM employee;




create table demo (
    id int,
    rool_no int unique,
    name varchar(50),
    age int not null,
    primary key (id)
    )

insert into demo values(101,004,'Harsh',19);

SELECT * FROM demo;


create table employee2 (
    id int primary key,
    name VARCHAR(50),
    salary int DEFAULT 67000 
    );

    SELECT * from demo where age>40; 