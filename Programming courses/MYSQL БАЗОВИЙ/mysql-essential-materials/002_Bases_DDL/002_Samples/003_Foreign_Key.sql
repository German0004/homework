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



DROP TABLE cars;



CREATE TABLE cars
( 
	id int auto_increment NOT NULL,
	client_id int NOT NULL, 
	mark varchar(30) NOT NULL,
	model varchar(30) NOT NULL,
    FOREIGN KEY(client_id) references clients(id),
    primary key(id)
);

INSERT INTO clients																			   
(name, age, phone)
VALUES
('Petrenko Petr Petrovich', 25,  '(093)1231212'),
('Ivanenko Ivan Ivanovich', 5,  '(095)2313244');	

INSERT INTO cars
(client_id, mark, model)
VALUES
(1, 'Audi', 'A5'),
(2, 'Porsche', 'Panamera'),
(2, 'Fiat', '500'),
(1, 'VAZ', 'Kalina');

SELECT id, name, age FROM clients;
SELECT * FROM cars;


INSERT INTO cars
(client_id, mark,	model)
VALUES
(3, 'Renault', 'Twizy'); -- Îøèáêà! 

DROP TABLE cars;



CREATE TABLE cars
(
	id int auto_increment NOT NULL,
	client_id int NOT NULL, 
	mark varchar(30) NOT NULL,
	model varchar(30) NOT NULL,
    primary key(id)
);

ALTER TABLE cars
ADD CONSTRAINT fk_clients_id
FOREIGN KEY (client_id) REFERENCES clients(id);

DROP TABLE clients;

-- Ïåðâûìè óäàëÿþòñÿ äî÷åðíèå òàáëèöû ïîñëå ÷åãî óäàëÿþòñÿ ðîäèòåëüñêèå òàáëèöû.

DROP TABLE cars;
DROP TABLE clients;


USE carsshop; 


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


-- Óäàëåíèå îãðàíè÷åíèÿ âíåøíåãî êëþ÷à. FK_CustomersCustomerNo - èìÿ ïî óìîë÷àíèþ
ALTER TABLE cars
DROP FOREIGN KEY fk_client_id;


DROP TABLE clients; -- Òàáëèöà Customers óäàëåíà.
