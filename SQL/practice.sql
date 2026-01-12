-- Creating Database--
create database collage;
create database if not exists collage;

--
-- Drop Database--
drop database collage;
DROP DATABASE IF EXISTS collage;

-- use database--
use collage;

-- To see our database and table --
show databases;
SHOW tables;

-- Create table -- 
create table if not exists student(
id int primary key,
name varchar(50),
roll_no int unique,
age int not null,
mobile_no varchar(10),
email_id varchar(50),
address varchar (100) 
);

-- Insert query --
insert into student value(1,'Harsh',0004,19,6205808582,'harshkr53453@gmail.com','Patna,bihar 800004');
insert into student value(4,'Akash',0001,18,6205808582,'aakash@gmail.com','Delhi,india');
insert into student value(5,'Akansha',0002,16,6205808582,'akansha@gmail.com','vaishali,bihar 844123');
insert into student value(6,'Shreya',0003,23,6205808582,'shreya@gmail.com','Patna ,bihar 800010');
insert into student value(7,'shrishti',0009,21,6205808582,'shrishti@gmail.com','muzzafarpur,bihar 812346');
insert into student value(8,'Vikash',0005,14,6205808582,'vikash@gmail.com','Patna ,bihar,800011');
insert into student value(9,'Aditya',0007,20,6205808582,'aditya@gmail.com','Patna ,bihar 800004');

insert into student(id,name,roll_no,age,mobile_no,email_id,address) values
(2,'Ravi',008,21,9798817881,'ravikr@gmail.com','Patna,bihar 800001'),
(3,'arya',0006,21,7898655423,'arya@gmail.com','Patna,bihar 800001');


-- View data in table -- select query
select * from student;
select age from student;
select name,address from student;
select age,address from student where age>18 and address = 'Patna,bihar 800001'; 

-- create table course --
create table course (
id int,
course_id int primary key,
course_name varchar(50),
foreign key (id) references student(id)
); 

-- Insert into course --
insert into course value(1,003,'DBMS'); 

select * from course;

-- DEFAULT sets the default value of a column
create table faculty(
faculty_id int primary key,
faculty_name varchar(50),
faculty_mobile_no varchar(10),
f_email_id varchar(50),
f_salary int default 55000
);

--  limit the values allowed in a column

create table if not exists student(
id int primary key,
name varchar(50),
roll_no int unique,
age int not null check (age >=18),
mobile_no varchar(10),
email_id varchar(50),
address varchar (100) 
);
-------------------------------------------------------------------------------------------------------------------------
-- student table for perform such operation on it
create table student (
roll_no int primary key,
name varchar(50),
marks int not null,
grade varchar(2),
city varchar(20)
);

-- insert sample data on student table
INSERT INTO student (roll_no, name, marks, grade, city) VALUES
(1, 'Aarav Sharma', 85, 'A', 'Mumbai'),
(2, 'Ananya Singh', 78, 'B', 'Delhi'),
(3, 'Rohan Patel', 92, 'A', 'Ahmedabad'),
(4, 'Sanya Mehta', 65, 'C', 'Bengaluru'),
(5, 'Vivaan Kapoor', 74, 'B', 'Chennai'),
(6, 'Ishaan Verma', 88, 'A', 'Kolkata'),
(7, 'Diya Reddy', 55, 'D', 'Hyderabad'),
(8, 'Kabir Jain', 90, 'A', 'Pune'),
(9, 'Myra Sharma', 60, 'C', 'Jaipur'),
(10, 'Aditya Rao', 72, 'B', 'Lucknow'),
(11, 'Kavya Nair', 81, 'A', 'Thiruvananthapuram'),
(12, 'Arjun Singh', 69, 'B', 'Kanpur'),
(13, 'Tanya Choudhary', 95, 'A', 'Surat'),
(14, 'Riddhi Desai', 58, 'D', 'Indore'),
(15, 'Aryan Malhotra', 76, 'B', 'Bhopal'),
(16, 'Sneha Kulkarni', 83, 'A', 'Nagpur'),
(17, 'Yash Khanna', 67, 'C', 'Patna'),
(18, 'Pooja Sharma', 89, 'A', 'Vadodara'),
(19, 'Devansh Gupta', 61, 'C', 'Mysore'),
(20, 'Meera Joshi', 73, 'B', 'Coimbatore');
-- Insert richer dataset for practice
INSERT INTO student (roll_no, name, marks, grade, city) VALUES
(41, 'Aarav Sharma', 88, 'A', 'Mumbai'),
(42, 'Aarav Sharma', 75, 'B', 'Delhi'),
(43, 'Neha Verma', 92, 'A', 'Delhi'),
(44, 'Neha Verma', 65, 'C', 'Bengaluru'),
(45, 'Rohan Patel', 70, 'B', 'Ahmedabad'),
(46, 'Rohan Patel', 85, 'A', 'Surat'),
(47, 'Sanya Mehta', 60, 'C', 'Bengaluru'),
(48, 'Sanya Mehta', 78, 'B', 'Chennai'),
(49, 'Vivaan Kapoor', 82, 'A', 'Chennai'),
(50, 'Vivaan Kapoor', 56, 'D', 'Pune'),
(51, 'Ishaan Verma', 90, 'A', 'Kolkata'),
(52, 'Ishaan Verma', 72, 'B', 'Mumbai'),
(53, 'Diya Reddy', 55, 'D', 'Hyderabad'),
(54, 'Diya Reddy', 68, 'C', 'Bengaluru'),
(55, 'Kabir Jain', 88, 'A', 'Pune'),
(56, 'Kabir Jain', 60, 'C', 'Ahmedabad'),
(57, 'Myra Sharma', 70, 'B', 'Jaipur'),
(58, 'Myra Sharma', 85, 'A', 'Delhi'),
(59, 'Aditya Rao', 73, 'B', 'Lucknow'),
(60, 'Aditya Rao', 95, 'A', 'Mumbai'),
(61, 'Kavya Nair', 81, 'A', 'Thiruvananthapuram'),
(62, 'Kavya Nair', 77, 'B', 'Chennai'),
(63, 'Arjun Singh', 69, 'B', 'Kanpur'),
(64, 'Arjun Singh', 88, 'A', 'Delhi'),
(65, 'Tanya Choudhary', 95, 'A', 'Surat'),
(66, 'Tanya Choudhary', 72, 'B', 'Ahmedabad'),
(67, 'Riddhi Desai', 58, 'D', 'Indore'),
(68, 'Riddhi Desai', 64, 'C', 'Bhopal'),
(69, 'Aryan Malhotra', 76, 'B', 'Bhopal'),
(70, 'Aryan Malhotra', 83, 'A', 'Vadodara'),
(71, 'Sneha Kulkarni', 85, 'A', 'Nagpur'),
(72, 'Sneha Kulkarni', 69, 'C', 'Pune'),
(73, 'Yash Khanna', 67, 'C', 'Patna'),
(74, 'Yash Khanna', 80, 'B', 'Jaipur'),
(75, 'Pooja Sharma', 89, 'A', 'Vadodara'),
(76, 'Pooja Sharma', 74, 'B', 'Surat'),
(77, 'Devansh Gupta', 61, 'C', 'Mysore'),
(78, 'Devansh Gupta', 78, 'B', 'Nagpur'),
(79, 'Meera Joshi', 73, 'B', 'Coimbatore'),
(80, 'Meera Joshi', 88, 'A', 'Chennai');

Drop table course;
-- Course table 
-- Create the course table
CREATE TABLE course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    student_roll_no INT,
    FOREIGN KEY (student_roll_no) REFERENCES student(roll_no)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- insert sample data in course table
INSERT INTO course (course_id, course_name, student_roll_no) VALUES
(1, 'Mathematics', 1),
(2, 'Physics', 1),
(3, 'Chemistry', 2),
(4, 'Biology', 3),
(5, 'Computer Science', 4),
(6, 'English', 5),
(7, 'History', 6),
(8, 'Geography', 7),
(9, 'Economics', 8),
(10, 'Political Science', 9),
(11, 'Mathematics', 10),
(12, 'Physics', 11),
(13, 'Chemistry', 12),
(14, 'Biology', 13),
(15, 'Computer Science', 14);
--------------------------------------------------------------------------------------------------------------
-- Select query in Detail
-- To Select ALL
SELECT * FROM student;

--  select specif column
select roll_no,name,marks from student;

-- Where clause
select * from student where marks >80;
select * from student where marks >80 and city = 'Mumbai' ;

-- Where clause 'using operator in where'
select * from student where marks+10 >100; -- Arithmatic operator
select * from student where grade = 'A'; -- Comparison operator 
select * from student where marks >80 and city = 'mumbai'; -- And operator
select * from student where marks >90 or city = 'mumbai'; -- Or operator
select * from student where marks between 80 and 90; -- Between operator
select * from student where city in ('delhi','mumbai','patna','kanpur'); -- In oeprator (match any value in list)
select * from student where city not in ('delhi','mumbai','patna','kanpur'); -- not  oeprator

-- limit clause :Sets an upper limit on number of (tuples)rows to be returned
select * from student where marks >80 limit 3; 

-- Order by clause : To sort in ascending (ASC) or descending order (DESC)
select * from student order by city asc; 
select * from student order by marks desc; 

-- Aggeregate functions 
select count(name) from student;
select count(roll_no) from student;
select max(marks)from student; 
select min(marks)from student; 
select sum(marks) from student;
select avg(marks) from student;

--  group by clause
select city , count(name) from student group by city; 
select grade , count(name) from student group by grade; 

-- Write query to find avg marks in each city in asending order
select city,avg(marks) from student group by city order by avg(marks); 


-- Having clause :Used when we want to apply any condition after grouping.
select count(name), city
from student
where city = 'mumbai' 
group by city 
having max(marks) > 90;

-- genral orders of commands
 select city,count(name)
 from student 
 where grade = 'A'
 group by city
 having max(marks) > 90
 order by grade asc;
-- ----------------------------------------------------------------------------------------------------------------
-- TABLE RELATED QUERIES : Update (to update existing rows)
update student set marks = 99 
where roll_no = 17;

update student set grade = 'A'
where roll_no = 17;
update student set marks = marks-1;
select name,marks from student where marks = 99; 

-- Table related Queries : Delete (to delete existing rows)  
delete from student where marks < 30; 
delete from student where roll_no = 67;

-- operation on Cascading forien key
-- See students
SELECT * FROM student LIMIT 5;

-- See courses
SELECT * FROM course LIMIT 5;

-- update cascading
UPDATE student
SET roll_no = 101
WHERE roll_no = 1;

-- check
SELECT * FROM course WHERE student_roll_no = 101;

-- Delete cascading
DELETE FROM student
WHERE roll_no = 2;

-- check 
SELECT * FROM course WHERE student_roll_no = 2;

-- Alter (to change the schema)   

-- Add columns 
alter table student 
add column age int not null default 19;

-- Drop columns
alter table student
drop column age;

-- Rename table --
alter table stu
rename to student;

-- Change column (rename) --
alter table student
change full_name name varchar(50);  

-- Modify column --
alter table student
modify age varchar(2);

-- Truncate (to delete table's data) ---
truncate table course;

----------------------------------------------------------------------------------------------------------------


 


 






 


 