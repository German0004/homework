USE carsshop;



DROP TABLE clients;               


CREATE TABLE clients                 
(	                                     
	id int auto_increment NOT NULL,  
	name varchar(25) NOT NULL,   
	age varchar(25) NOT NULL,
	phone varchar(25) DEFAULT 'Unknown',
    PRIMARY KEY (id)
);


DROP TABLE clients;


CREATE TABLE clients                 
(	                                   
	id int auto_increment NOT NULL,  
	name varchar(25) NOT NULL,   
	age varchar(25) NOT NULL,
	phone varchar(25) DEFAULT 'Unknown',
	data datetime NOT NULL ,
    PRIMARY KEY (id)
); 

INSERT INTO clients
(name, age, phone, data)
VALUES
('Jeremy', 20, '0567878932',  NOW());


SELECT * FROM clients;




ALTER TABLE clients 
ADD                   
newFild int NULL;    



SELECT * FROM clients;

		

ALTER TABLE clients 
DROP COLUMN           
newFild;

SELECT * FROM clients;


ALTER TABLE clients
ADD					 
newFild2 varchar(10) NOT NULL;

SELECT * FROM clients;


ALTER TABLE clients 
DROP COLUMN           
newFild2;



ALTER TABLE clients
ADD						
newFild2 varchar(10) NOT NULL 
DEFAULT 'Unknown';

SELECT * FROM clients;

