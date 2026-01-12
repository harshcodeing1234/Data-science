
CREATE DATABASE college_db;
USE college_db;

-- 2. Create Course Table
CREATE TABLE course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

-- 3. Create Student Table
CREATE TABLE student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

-- Insert into student 
INSERT INTO student (student_id, student_name, course_id) VALUES
(101, 'Alice Johnson', 1),
(102, 'Bob Smith', 2),
(103, 'Charlie Patel', 3),
(104, 'Diana Gomez', 4),
(105, 'Edward Lee', 5),
(106, 'Fiona Davis', 6),
(107, 'George Brown', 7),
(108, 'Hannah Wilson', 8),
(109, 'Ian Turner', 9),
(110, 'Julia Adams', 10);

-- insert into course
INSERT INTO course (course_id, course_name, credits) VALUES
(1, 'Mathematics', 4),
(2, 'Physics', 3),
(3, 'Chemistry', 4),
(4, 'Biology', 3),
(5, 'Computer Science', 4),
(6, 'English Literature', 2),
(7, 'History', 3),
(8, 'Economics', 3),
(9, 'Statistics', 4),
(10, 'Philosophy', 2);
 
 
 -- INNER JOIN
 select * from student as s
 inner join course as c
 on s.course_id = c.course_id;
 
 -- LEFT JOIN
 select * from student as s
 left join course as c
 on s.course_id = c.course_id;
 
 -- RIGHT JOIN
select * from student as s
right join course as c
 on s.course_id = c.course_id;
 
 -- FULL JOIN
 select * from student as s
 left join course as c
 on s.course_id = c.course_id
 union
 select * from student as s
right join course as c
 on s.course_id = c.course_id;
 
 -- Self join 
 create table employee (
 id int primary key,
 name varchar(50),
 manager_id int
 );
 
INSERT INTO employee (id, name, manager_id) VALUES
(101, 'Alice Johnson', 103),
(102, 'jon deo', 104),
(103, 'Dewald', null),
(104, 'casey', 103),
(105, 'donald', 102);

-- SELF JOIN 
select a.name as manager_name, b.name 
from employee as a
join employee as b
on a.id = b.manager_id


 
 
 
 