-------------------------------------------------------------------------
--                 Ñâÿçü Îäèí ê Îäíîìó
-------------------------------------------------------------------------

USE carsshop; 


DROP TABLE cars;


DROP TABLE clients;


CREATE TABLE clients					
(                                      
	id int auto_increment NOT NULL,  
	name varchar(25) NOT NULL,   
	age varchar(25) NOT NULL,
	phone char(12),
    primary key (id) 
);

CREATE TABLE cars
( 
	id int auto_increment NOT NULL,
	client_id int NOT NULL, 
	mark varchar(30) NOT NULL,
	model varchar(30) NOT NULL,
    primary key(id),
    foreign key(client_id) references clients(id)
);


INSERT INTO clients																			   
(name, age, phone)
VALUES
('Petro', ' 25',  '(093)1231212'),
('Vasya', '18',  '(095)2313244');	

INSERT INTO cars
(client_id, mark,	model)
VALUES
(1, 'Audi', 'A5'),
(2, 'Lada', 'Priora');


SELECT name, age FROM clients;
SELECT * FROM cars;

INSERT INTO cars
(client_id, mark,	model)
VALUES
(1, 'Audi', 'A5'),
(2, 'Lada', 'Priora');

-------------------------------------------------------------------------
--                 Ñâÿçü Îäèí êî Ìíîãèì
-------------------------------------------------------------------------


DROP TABLE cars;


DROP TABLE clients;

CREATE TABLE clients					
(                                      
	id int auto_increment NOT NULL,  
	name varchar(25) NOT NULL,   
	age varchar(25) NOT NULL,
	phone char(12),
    primary key (id) 
);

CREATE TABLE cars
( 
	id int auto_increment NOT NULL,
	client_id int NOT NULL UNIQUE, 
	mark varchar(30) NOT NULL,
	model varchar(30) NOT NULL,
    primary key(id),
    foreign key(client_id) references clients(id)
);

INSERT INTO clients																			   
(name, age, phone)
VALUES
('Petro', ' 25',  '(093)1231212'),
('Vasya', '18',  '(095)2313244');	

INSERT INTO cars
(client_id, mark,	model)
VALUES
(1, 'Audi', 'A5'),
(2, 'Lada', 'Priora');

SELECT name, age FROM clients;
SELECT * FROM cars;

-------------------------------------------------------------------------
--                 Ñâÿçü Ìíîãèå êî Ìíîãèì
-------------------------------------------------------------------------

DROP TABLE Students;
DROP TABLE StudentsCourses;
DROP TABLE Courses;

CREATE TABLE Students				
(                                      
	StudentId int NOT NULL auto_increment ,				  
	FName varchar(50) NOT NULL,
	LName varchar(50) NOT NULL,
	Email varchar(50) NOT NULL,
	Phone varchar(50) NOT NULL,
    primary key (StudentId)
);

CREATE TABLE Courses
( 
	CourseId int  NOT NULL auto_increment,
	CourseName varchar(50) NOT NULL,
	Price double(10,2) Not Null,
    PRIMARY KEY (CourseId)
);


CREATE TABLE StudentsCourses
(
	 StudentId int NOT NULL,
	 CourseId int NOT NULL,
	 PRIMARY KEY(StudentId, CourseId),
	 FOREIGN KEY (StudentId) references Students(StudentId),
     FOREIGN KEY (CourseId) references Courses(CourseId)
);

INSERT INTO Students																			   
(FName, LName, Email, Phone)
VALUES
('Petro', 'Petrov', 'PetrPetrenko@mail.com', '(093)1231212'),
('Ivan', 'Ivanov', 'IvanenkoIvan@mail.com', '(095)2313244'),
('Fedor', 'F', 'MaximovMax@mail.com', '(095)7658786');	

INSERT INTO Courses
(CourseName, Price)
VALUES
('SQL Essential', 100.00),
('C# Professional', 200.00),
('ASP.NET MVC', 300.00),
('Patterns GoF', 400.00);

INSERT INTO StudentsCourses
(StudentId, CourseId)
VALUES
(1,1),
(2,1),
(3,3),
(3,1),
(2,2);


SELECT * FROM Students;
SELECT * FROM StudentsCourses;
SELECT * FROM Courses;