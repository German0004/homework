USE carsshop;


INSERT clients 
(name, age, phone)
VALUES ('Max', 27, '050*****');


SELECT * FROM clients;



UPDATE clients
SET age = 28 
WHERE name = 'Max';


SELECT * FROM clients;


UPDATE clients
SET name = 'TestName',
	phone = '000*******'
WHERE name = 'Max';

SELECT * FROM clients;


UPDATE clients
SET phone = '060*******';  


SELECT * FROM clients;



DELETE FROM clients WHERE name = 'TestName';
SELECT * FROM clients;


DELETE FROM clients;
SELECT * FROM clients;


TRUNCATE TABLE clients;
SELECT * FROM clients;