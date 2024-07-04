USE ShopDB;
 
DROP TABLE InfoPerson;

SELECT * FROM carsshop.clients;

CREATE TABLE InfoPerson
(
	name nvarchar(50) null,
	age nvarchar(50)null,
	phone nvarchar(50)null
);

Insert into InfoPerson SELECT name, age, phone FROM carsshop.clients;



SELECT * FROM InfoPerson;



CREATE VIEW BthPerson   
AS SELECT name, age
FROM InfoPerson;


SELECT * FROM BthPerson; 

SELECT * FROM InfoPerson;



------------------------------------------------------------

CREATE VIEW BthPrsn2age
AS SELECT name, phone
FROM InfoPerson
WHERE age is not null; 


SELECT * FROM BthPrsn2age; 

SELECT name, phone, age FROM BthPrsn2age;



DROP TABLE InfoPerson; 

Insert into InfoPerson SELECT name, age, phone FROM carsshop.clients;
			
SELECT * FROM InfoPerson;


SELECT * FROM BthPerson;

INSERT INTO BthPerson 
(name, age, phone)
VALUES 
('Andrew', 23 );


SELECT * FROM BthPerson WHERE name = 'Andrew';


SELECT * FROM InfoPerson WHERE name = 'Andrew';

	


UPDATE BthPerson 
	SET age = 24
	WHERE name = 'Andrew';
	
SELECT * FROM BthPerson 
	WHERE name = 'Andrew';
	
SELECT * FROM InfoPerson
	WHERE name = 'Andrew';

UPDATE InfoPerson
SET age = 25
	WHERE name = 'Andrew';
	
SELECT * FROM BthPerson 
	WHERE name = 'Andrew';
	
SELECT * FROM InfoPerson
	WHERE name = 'Andrew';
	


SELECT * FROM BthPerson;

ALTER VIEW BthPerson  
AS  SELECT phone, age, name
FROM InfoPerson;


SELECT * FROM BthPerson;	



DROP VIEW BthPerson;


SELECT * FROM BthPerson 
	WHERE name = 'Andrew';
	
SELECT * FROM InfoPerson
	WHERE name = 'Andrew';
