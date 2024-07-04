USE ShopDB;

DROP TABLE BTree;


CREATE TABLE BTree
(
numbers int ,
word varchar(25)
);

INSERT BTree
VALUES
(1,'one'),
(2,'two'),
(3,'three'),
(4,'four'),
(6,'six'),
(7,'seven'),
(8,'eight'),
(9,'nine');

EXPLAIN SELECT * FROM BTree WHERE numbers IN (5,6);

SELECT * FROM BTree;

INSERT BTree
VALUES (5,'five');

SELECT * FROM BTree WHERE numbers IN (5,6);
--------------------------------------------------

DROP TABLE BTree;


CREATE TABLE BTree
(
numbers int primary key, 
word varchar(25)
);

INSERT BTree
VALUES
(1,'one'),
(2,'two'),
(3,'three'),
(4,'four'),
(6,'six'),
(7,'seven'),
(8,'eight'),
(9,'nine');

CREATE INDEX word ON BTree(word);

SELECT * FROM BTree WHERE word = 'one';

EXPLAIN SELECT * FROM BTree WHERE word = 'one';

INSERT BTree
VALUES (5,'five');

SELECT * FROM BTree;

--------------------------------------------------

DROP TABLE BTree;


CREATE TABLE BTree
(
numbers int ,
word varchar(25)primary key 
);

INSERT BTree
VALUES
(1,'one'),
(2,'two'),
(3,'three'),
(4,'four'),
(6,'six'),
(7,'seven'),
(8,'eight'),
(9,'nine');

SELECT * FROM BTree;

INSERT BTree
VALUES (5,'five');

SELECT * FROM BTree;

--------------------------------------------------

DROP TABLE BTree;


CREATE TABLE BTree
(
numbers int unique, 
word varchar(25)
);

INSERT BTree
VALUES
(1,'one'),
(2,'two'),
(3,'three'),
(4,'four'),
(6,'six'),
(7,'seven'),
(8,'eight'),
(9,'nine');

SELECT * FROM BTree;

INSERT BTree
VALUES (5,'five');

SELECT * FROM BTree where word = 'one';

--------------------------------------------------

DROP TABLE BTree;


CREATE TABLE BTree
(
numbers int primary key, 
word varchar(25)unique   
);

INSERT BTree
VALUES
(1,'one'),
(2,'two'),
(3,'three'),
(4,'four'),
(6,'six'),
(7,'seven'),
(8,'eight'),
(9,'nine');

SELECT * FROM BTree;

INSERT BTree
VALUES (5,'five');

SELECT * FROM BTree where word in ('five', 'one'); -- ïîèñê ïî íåêëàñòåðèçîâàííîìó èíäåêñó
SELECT * FROM BTree where numbers in (3,5);   -- ïîèñê ïî êëàñòåðèçîâàííîìó èíäåêñó
--------------------------------------------------
DROP TABLE OrderDetails;

DROP TABLE Orders;

DROP TABLE Customers;


CREATE TABLE Customers                
(                                      
	CustumerNo int NOT NULL, 
	CustumerName varchar(25) NOT NULL,
	Address1 varchar(25) NOT NULL,
	Address2 varchar(25) NOT NULL,
	City      varchar(15) NOT NULL,
	State char(2) NOT NULL,
	Zip varchar(10) NOT NULL,
	Contact varchar(25) NOT NULL,
	Phone char(12),
	FedIDNo  varchar(10) NOT NULL,
	DateInSystem date NOT NULL 
);


INSERT INTO Customers
( CustumerNo, CustumerName, Address1, Address2, City, State, Zip, Contact, Phone, FedIDNo, DateInSystem)
VALUES
(1,'Alex', 'NewSTR', 'NewSTR2', 'City', 'NS', 'NewZip', 'dfgjs@mail.ru', '(093)1231212', 'qweq', NOW()),
(2,'Alex2', 'NewSTR2', 'NewSTR22', 'City2', 'SN', 'NewZip2', 'dfg2@mail.ru', '(093)2221212', 'qwq2', NOW());


SELECT * FROM Customers;

-----------------------------------------------------------------------------------------------------------------

DROP TABLE Customers;


CREATE TABLE Customers                
(                                      
	CustumerNo int NOT NULL PRIMARY KEY,    
	CustumerName varchar(25) NOT NULL,
	Address1 varchar(25) NOT NULL,
	Address2 varchar(25) NOT NULL,
	City      varchar(15) NOT NULL,
	State char(2) NOT NULL,
	Zip varchar(10) NOT NULL,
	Contact varchar(25) NOT NULL,
	Phone char(12),
	FedIDNo  varchar(10) NOT NULL,
	DateInSystem date NOT NULL 
);

INSERT INTO Customers
( CustumerNo, CustumerName, Address1, Address2, City, State, Zip, Contact, Phone, FedIDNo, DateInSystem)
VALUES
(1,'Alex', 'NewSTR', 'NewSTR2', 'City', 'NS', 'NewZip', 'dfgjs@mail.ru', '(093)1231212', 'qweq', NOW()),
(2,'Alex2', 'NewSTR2', 'NewSTR22', 'City2', 'SN', 'NewZip2', 'dfg2@mail.ru', '(093)2221212', 'qwq2', NOW());

SELECT * FROM Customers; 

-----------------------------------------------------------------------------------------------------------------

DROP TABLE Customers;


CREATE TABLE Customers                
(                                      
	CustumerNo int NOT NULL, 
	CustumerName varchar(25) NOT NULL,
	Address1 varchar(25) NOT NULL,
	Address2 varchar(25) NOT NULL,
	City      varchar(15) NOT NULL,
	State char(2) NOT NULL,
	Zip varchar(10) NOT NULL,
	Contact varchar(25) NOT NULL,
	Phone char(12) UNIQUE, 
	FedIDNo  varchar(10) NOT NULL,
	DateInSystem date NOT NULL 
);

INSERT INTO Customers
( CustumerNo, CustumerName, Address1, Address2, City, State, Zip, Contact, Phone, FedIDNo, DateInSystem)
VALUES
(1,'Alex', 'NewSTR', 'NewSTR2', 'City', 'NS', 'NewZip', 'dfgjs@mail.ru', '(093)1231212', 'qweq', NOW()),
(2,'Alex2', 'NewSTR2', 'NewSTR22', 'City2', 'SN', 'NewZip2', 'dfg2@mail.ru', '(093)2221212', 'qwq2', NOW());


SELECT * FROM Customers;

SELECT Phone FROM Customers			  
	WHERE Phone = '(093)2221212'; 
	
-----------------------------------------------------------------------------------------------------------------

DROP TABLE Customers;


CREATE TABLE Customers                
(                                      
	CustumerNo int auto_increment NOT NULL
		PRIMARY KEY,    
	CustumerName varchar(25) NOT NULL,
	Address1 varchar(25) NOT NULL,
	Address2 varchar(25) NOT NULL,
	City      varchar(15) NOT NULL,
	State char(2) NOT NULL,
	Zip varchar(10) NOT NULL,
	Contact varchar(25) NOT NULL,
	Phone char(12) UNIQUE, 
	FedIDNo  varchar(10) NOT NULL,
	DateInSystem date NOT NULL 
);

INSERT INTO Customers
( CustumerName, Address1, Address2, City, State, Zip, Contact, Phone, FedIDNo, DateInSystem)
VALUES
('Alex', 'NewSTR', 'NewSTR2', 'City', 'NS', 'NewZip', 'dfgjs@mail.ru', '(093)1231212', 'qweq', NOW()),
('Alex2', 'NewSTR2', 'NewSTR22', 'City2', 'SN', 'NewZip2', 'dfg2@mail.ru', '(093)2221212', 'qwq2', NOW());

SELECT * FROM Customers; 

SELECT * FROM Customers			  
	WHERE Phone = '(093)2221212'; 
	
------------------------- Êëàñòåðèçîâàííûé èíäåêñ -------------------------------------------------------

DROP TABLE Customers;


CREATE TABLE Customers                
(                                      
	CustumerNo int NOT NULL, 
	CustumerName varchar(25) NOT NULL,
	Address1 varchar(25) NOT NULL,
	Address2 varchar(25) NOT NULL,
	City      varchar(15) NOT NULL,
	State char(2) NOT NULL,
	Zip varchar(10) NOT NULL,
	Contact varchar(25) NOT NULL,
	Phone char(12),
	FedIDNo  varchar(10) NOT NULL,
	DateInSystem date NOT NULL 
);

CREATE INDEX Customers -- ñîçäàíèå ñîáñòâåííîãî êëàñòåðèçîâàííîãî èíäåêñà
ON Customers(CustumerNo);


INSERT INTO Customers
( CustumerNo, CustumerName, Address1, Address2, City, State, Zip, Contact, Phone, FedIDNo, DateInSystem)
VALUES
(1,'Alex', 'NewSTR', 'NewSTR2', 'City', 'NS', 'NewZip', 'dfgjs@mail.ru', '(093)1231212', 'qweq', NOW()),
(1,'Alex2', 'NewSTR2', 'NewSTR22', 'City2', 'SN', 'NewZip2', 'dfg2@mail.ru', '(093)2221212', 'qwq2', NOW()); 


SELECT * FROM Customers;



DROP TABLE Customers;


CREATE TABLE Customers               
(                                      
	CustumerNo int NOT NULL, 
	CustumerName varchar(25) NOT NULL,
	Address1 varchar(25) NOT NULL,
	Address2 varchar(25) NOT NULL,
	City      varchar(15) NOT NULL,
	State char(2) NOT NULL,
	Zip varchar(10) NOT NULL,
	Contact varchar(25) NOT NULL,
	Phone char(12) Primary key,
	FedIDNo  varchar(10) NOT NULL,
	DateInSystem date NOT NULL 
);

CREATE UNIQUE INDEX CustomersNo 
ON Customers(CustumerNo);


INSERT INTO Customers
( CustumerNo, CustumerName, Address1, Address2, City, State, Zip, Contact, Phone, FedIDNo, DateInSystem)
VALUES
(1,'Alex', 'NewSTR', 'NewSTR2', 'City', 'NS', 'NewZip', 'dfgjs@mail.ru', '(093)1231212', 'qweq', NOW()),
(1,'Alex2', 'NewSTR2', 'NewSTR22', 'City2', 'SN', 'NewZip2', 'dfg2@mail.ru', '(093)2221212', 'qwq2', NOW()); -- CustumerNo = 1 áóäåò îøèáêà


INSERT INTO Customers
( CustumerNo, CustumerName, Address1, Address2, City, State, Zip, Contact, Phone, FedIDNo, DateInSystem)
VALUES
(1,'Alex', 'NewSTR', 'NewSTR2', 'City', 'NS', 'NewZip', 'dfgjs@mail.ru', '(093)1231212', 'qweq', NOW()),
(2,'Alex2', 'NewSTR2', 'NewSTR22', 'City2', 'SN', 'NewZip2', 'dfg2@mail.ru', '(093)2221212', 'qwq2', NOW()); 


SELECT * FROM Customers; 