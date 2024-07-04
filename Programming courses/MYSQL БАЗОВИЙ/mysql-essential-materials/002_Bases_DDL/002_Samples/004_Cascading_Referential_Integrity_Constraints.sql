USE carsshop; 


DROP TABLE clients;

DROP TABLE cars;

CREATE TABLE clients					
(                                      
	id int auto_increment NOT NULL,  
	name varchar(25) NOT NULL,   
	age varchar(25) NOT NULL,
	phone varchar(25) DEFAULT 'Unknown',
    PRIMARY KEY (id)
);
									

CREATE TABLE cars
(
	id int auto_increment NOT NULL,
	client_id int NOT NULL, 
	mark varchar(30) NOT NULL,
	model varchar(30) NOT NULL,
    primary key(id)
);

ALTER TABLE cars
ADD CONSTRAINT fk_client_id
FOREIGN KEY (client_id) REFERENCES clients(id);

INSERT INTO clients																			   
(name, age, phone)
VALUES
('Petrenko Petr Petrovich', '25',  '(093)1231212'),
('Ivanenko Ivan Ivanovich', '18',  '(095)2313244');	

INSERT INTO cars
(client_id, mark,	model)
VALUES
(1, 'Audi', 'A5');

SELECT * FROM clients;
SELECT * FROM cars;


DELETE FROM clients
WHERE name = 'Petrenko Petr Petrovich';


ALTER TABLE cars
DROP foreign key fk_client_id;


ALTER TABLE cars
ADD CONSTRAINT fk_client_id
FOREIGN KEY (client_id) REFERENCES clients(id)
	ON DELETE CASCADE ON UPDATE CASCADE;


DELETE FROM clients
WHERE name = 'Petrenko Petr Petrovich';

SELECT * FROM clients;
SELECT * FROM cars;

DELETE FROM clients;
DELETE FROM cars;

SELECT * FROM clients;
SELECT * FROM cars;

INSERT INTO clients																			   
(name, age, phone)
VALUES
('Petrenko Petr Petrovich', '25',  '(093)1231212'),
('Ivanenko Ivan Ivanovich', '18',  '(095)2313244');	

INSERT INTO cars
(client_id, mark,	model)
VALUES
(3, 'Audi', 'A5');

SELECT * FROM clients;
SELECT * FROM cars;

DELETE FROM clients;
DELETE FROM cars;




ALTER TABLE clients auto_increment = 0;
ALTER TABLE cars auto_increment = 0;

ALTER TABLE cars
DROP foreign key fk_client_id;

 
ALTER TABLE cars
ADD CONSTRAINT fk_client_id
FOREIGN KEY (client_id) REFERENCES clients(id)
	ON DELETE SET NULL;
    
    
INSERT INTO clients																			   
(name, age, phone)
VALUES
('Petrenko Petr Petrovich', '25',  '(093)1231212');  

INSERT INTO cars
(client_id, mark,	model)
VALUES
(1, 'Audi', 'A5');


DELETE FROM clients
WHERE name = 'Petrenko Petr Petrovich';


SELECT * FROM clients;
SELECT * FROM cars;

ALTER TABLE clients auto_increment = 0;



INSERT INTO clients																			   
(name, age, phone)
VALUES
('Petrenko Petr Petrovich', '25',  '(093)1231212'); 



DELETE FROM cars;




INSERT INTO cars
(client_id, mark,	model)
VALUES (1, 'Audi', 'A5');


SELECT * FROM clients;
SELECT * FROM cars;




ALTER TABLE clients auto_increment=0; 


INSERT INTO clients																			   
(name, age, phone)
VALUES
('Petrenko Petr Petrovich', '25',  '(093)1231212');



DELETE FROM cars;


ALTER TABLE cars auto_increment=0;  


INSERT INTO cars
(client_id, mark, model)
VALUES (3,'Audi','A5');


SELECT * FROM clients;
SELECT * FROM cars;

