create table student (
    id int primary key,
    name varchar(50),
    age int not null
);

INSERT into student values(1,'Aman',26);
INSERT into student(id,name,age) values(4,'Ram',45);

SELECT * FROM student;



-- drop table student

create table demo (
    id int,
    rool_no int unique,
    name varchar(50),
    age int not null,
    primary key (id)
    );

insert into demo values(101,004,'Harsh',19);

SELECT * FROM demo;


create table employee2 (
    id int primary key,
    name VARCHAR(50),
    salary int DEFAULT 67000 
    );
    
    SELECT * from demo where age>10;
    select * from demo where name = 'Harsh' and age = 19;