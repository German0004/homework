USE carsshop; 


DROP TABLE clients;




CREATE TABLE clients                 
(	                                     
	id int NOT NULL,  
	name varchar(25) NOT NULL,   
	age int NOT NULL,
	phone varchar(25) DEFAULT 'Unknown',
    PRIMARY KEY (id)
);


INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(1,'Петро', 25,  '(093)1231212'),
(2,'Василий', 18,  '(095)2313244'); 



INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(1,'Семен', 19, '(063)4533272'); 

SELECT * FROM clients;

DROP TABLE clients;


CREATE TABLE clients                 
(	                                     
	id int NOT NULL,  
	name varchar(25) NOT NULL,   
	age int NOT NULL,
	phone varchar(25) DEFAULT 'Unknown',
    PRIMARY KEY (id, name)
);

INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(1,'Петро', 25,  '(093)1231212'),
(2,'Василий', 18,  '(095)2313244');  


INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(1,'Семен', 19, '(063)4533272'); 

INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(2,'Василий', 18,  '(095)2313244');

SELECT * FROM clients;


DROP TABLE clients;


CREATE TABLE clients                 
(	                                     
	id int NOT NULL,  
	name varchar(25) NOT NULL,   
	age int NOT NULL,
	phone varchar(25) DEFAULT 'Unknown'
);

-- Èçìåíÿåì òàáëèöó	Customers çàäàâ îãðàíè÷åíèå ïåðâè÷íîãî êëþ÷à íà ñòîëáöå	CustomerNo
ALTER TABLE clients
ADD CONSTRAINT pk_clients
PRIMARY KEY (id);

INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(1, 'Петро', 25,  '(093)1231212'),
(2, 'Василий', 18,  '(095)2313244'); 


SELECT * FROM clients;

DROP TABLE clients;


CREATE TABLE clients                 
(	                                     
	id int NOT NULL,  
	name varchar(25) NOT NULL,   
	age int NOT NULL,
	phone varchar(25) DEFAULT 'Unknown'
);


ALTER TABLE clients
ADD  
PRIMARY KEY (id, age);

INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(1,'Петро', 25, '(093)1231212'),
(2,'Василий', 18, '(095)2313244'); 


INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(1,'Cемен', 22, '(093)1231212'); 

INSERT INTO clients																			   
(id, name, age, phone)
VALUES
(2,'Рейдо', 21, '(093)1231212'); 

SELECT * FROM clients;

