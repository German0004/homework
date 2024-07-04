USE ShopDB;	 


DROP TABLE MyUserName;

DROP TABLE MyUserTell;

DROP TABLE MyUserInfo;

CREATE TABLE MyUserName
(
	IdTest int auto_increment PRIMARY KEY,
	FName varchar(25),
	LName varchar(25)
);

CREATE TABLE MyUserTell
(
	IdTest int auto_increment PRIMARY KEY,
	IdUser int  UNIQUE,
	TellN char(12),
    FOREIGN KEY (IdUser) REFERENCES MyUserName(IdTest)
);

CREATE TABLE MyUserInfo
(
	IdTest int auto_increment PRIMARY KEY,
	IdUser int,
	Bdate date,
    FOREIGN KEY (IdUser) REFERENCES MyUserName(IdTest)
);



START TRANSACTION; 
 INSERT MyUserName (FName, LName)
 VALUES('TestName0','TestLName0');
COMMIT;
 
 SELECT * FROM MyUserName;

 
START TRANSACTION;  

 INSERT MyUserName (FName, LName)
 VALUES
	('RollTest1','RollTestL1');
	
 ROLLBACK; 

SELECT * FROM MyUserName;



START TRANSACTION; 
 

INSERT MyUserName (FName, LName)
VALUES
	('TestName0','TestLName0');
	
		
INSERT MyUserTell (IdUser, TellN)
VALUES 
( @id = @@IDENTITY,'(097)2224455');
		
INSERT MyUserInfo (IdUser, Bdate)
VALUES (@id,'1990-01-02');

COMMIT;  
 
SELECT * FROM MyUserName;
SELECT * FROM MyUserInfo;
SELECT * FROM MyUserTell;




START TRANSACTION;
 

INSERT MyUserName (FName, LName)
VALUES
	('RollBackTest','TestLName0');
	
		
INSERT MyUserTell (IdUser, TellN)
VALUES 
( @id = @@IDENTITY,'(097)2224455');
		
INSERT MyUserInfo (IdUser, Bdate)
VALUES (@id,'1990-01-02');

ROLLBACK; 

SELECT * FROM MyUserName;
SELECT * FROM MyUserInfo;
SELECT * FROM MyUserTell;
---------------------------------------------------------
-- Òî÷êà ñîõðàíåíèÿ òðàíçàêöèè (ïðîìåæóòî÷íîå ñîõðàíåíèå òðàíçàêöèè)

START TRANSACTION; 

INSERT MyUserName (FName, LName)
VALUES
	('SavePoinTest1','TestLName0');
SAVEPOINT SavePointTran; 

INSERT MyUserName (FName, LName)
VALUES
	('SavePointTest2','TestLName0');

ROLLBACK TO SAVEPOINT SavePointTran; 

COMMIT; 

SELECT * FROM MyUserName;


DELIMITER |
DROP PROCEDURE MyTransactProc; |
CREATE PROCEDURE MyTransactProc (IN name varchar(25), IN last varchar(25), IN tell char(12),IN Date date)

BEGIN
DECLARE Id int;
START TRANSACTION;
			
		INSERT MyUserName (FName, LName)
		VALUES (name, last);
		SET Id = @@IDENTITY;
		
		INSERT MyUserTell (IdUser, TellN)
		VALUES (Id,tell);
		
		INSERT MyUserInfo (IdUser, Bdate)
		VALUES (Id, Date);
		
IF EXISTS (SELECT * FROM MyUserName WHERE FName = name AND LName = last AND IdTest != Id)
			THEN
				ROLLBACK; 
				
			END IF;	
			
		COMMIT; 
END; |	

 
CALL MyTransactProc( 'Name1','LName1', '(097)7775566','2010-01-02'); |

CALL MyTransactProc ( 'Name1', 'LName1',  '(097)7775566' ,'2010-01-02'); |


CALL MyTransactProc	( 'TestName2','TestLName2', '(097)7775566' , '2010-01-02'); |

SELECT * FROM MyUserName;  |
SELECT * FROM MyUserInfo;  |
SELECT * FROM MyUserTell;  |