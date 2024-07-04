CREATE DATABASE ShopDB;

USE ShopDB;


DROP TABLE MyEmployee;


CREATE TABLE MyEmployee
(
  EmployeeID int NOT NULL,
  ManagerID int NULL REFERENCES MyEmployee(EmployeeID), -- Ïîêàçâàåò êîìó ïîä÷åíÿåòñÿ äàííûé ñîòðóäíèê.
  JobTitle nvarchar(50) NOT NULL,
  LastName nvarchar(50) NOT NULL,
  FirstName nvarchar(50) NOT NULL,
    CONSTRAINT PK_Employee2_EmployeeID PRIMARY KEY CLUSTERED (EmployeeID ASC)
);



INSERT INTO MyEmployee(EmployeeID,ManagerID,JobTitle,LastName,FirstName)
VALUES
  (1, NULL, 'Gen','Andrew', 'Bond'),
  (2, 1, 'Fin', 'Petro', 'Becko'),	
  (3, 1, 'Prog','AA','BB'),		
  (4, 1, 'DEv', 'CC', 'DD'),
  (5, 4, 'Security', 'EE', 'FF'),			
  (8, 5, 'Gruzchik', 'GG', 'HH'),			
  (9, 5, 'Pogruzchik', 'II', 'JJ'),				
  (10 ,5, 'Data Architect', 'KK', 'LL'),			
  (11 ,5, 'Data', 'MM', 'NN'),				
  (6, 4, 'Kto', 'OO', 'PP'),	
  (7, 4, 'Nikto','QQ','RR');				

SELECT * FROM MyEmployee;

SELECT  sub.EmployeeID,
		sub.FirstName,
		sub.LastName
FROM
	MyEmployee as boss
	JOIN
	MyEmployee as sub
	ON boss.EmployeeID = sub.ManagerID;
    



DELIMITER |
CREATE procedure employees () -- Ñîçäàåì ôóíêöèþ ñ îäíèì àðãóìåíòîì.

BEGIN

 DECLARE employeeCursor CURSOR		   -- îáúÿâëåíèå êóðñîðà
FOR
		SELECT * FROM MyEmployee;   -- îòáîð ñòðîê äëÿ êóðñîðà
		
OPEN contact_cursor;	                   -- îòêðûòèå êóðñîðà
CLOSE contact_cursor;                   -- çàêðûòèå êóðñîðà



END;|




CALL employees(); |

DELIMITER |
DROP procedure employees; |
CREATE procedure employees (id INT) -- Ñîçäàåì ôóíêöèþ ñ îäíèì àðãóìåíòîì.

BEGIN
DECLARE manager nvarchar(45);
DECLARE employee nvarchar(45);
DECLARE job_title nvarchar(45);
DECLARE getId INT;


DECLARE employeeCursor CURSOR 
	FOR
	SELECT 
	e.EmployeeID,
    e.FirstName,
 (SELECT m.FirstName FROM myemployee m
 WHERE m.ManagerID = e.ManagerID and  m.EmployeeID = e.EmployeeID),
 e.JobTitle
 FROM myemployee e;
	
OPEN employeeCursor;

get_emp : LOOP
  FETCH employeeCursor INTO getId, manager, employee, job_title;	
  IF getId = id
     THEN
     SELECT manager, employee, job_title;
   ELSE 
     SELECT 'Different employee';
  END IF;
  END LOOP get_emp;

CLOSE employeeCursor;                 -- çàêðûòèå êóðñîðà



END;|

CALL employees(5); |

DROP TABLE BestEmployee; |
CREATE TABLE BestEmployee
(
  EmployeeID int NOT NULL,
  ManagerID int NULL REFERENCES MyEmployee(EmployeeID), 
  JobTitle nvarchar(50) NOT NULL,
  LastName nvarchar(50) NOT NULL,
  FirstName nvarchar(50) NOT NULL,
    CONSTRAINT PK_Employee2_EmployeeID PRIMARY KEY CLUSTERED (EmployeeID ASC)
); |

DELIMITER |
DROP procedure employees; |
CREATE procedure employees () 

BEGIN
DECLARE lastName nvarchar(45);
DECLARE employee nvarchar(45);
DECLARE job_title nvarchar(45);
DECLARE id INT;
DECLARE manager_id INT;

DECLARE employeeCursor CURSOR 
	FOR
	SELECT * FROM MyEmployee;
	
OPEN employeeCursor;

get_emp : LOOP
  FETCH employeeCursor INTO id, manager_id, job_title, lastName, employee;	
  select id, manager_id, job_title, lastName, employee;
    IF id < 5
     THEN 
     INSERT INTO BestEmployee(EmployeeID,ManagerID,JobTitle,LastName,FirstName)
       VALUES (id, manager_id, job_title, lastName, employee);
       END IF;
  END LOOP get_emp;

CLOSE employeeCursor;                 -- çàêðûòèå êóðñîðà



END;|

CALL employees(); |

SELECT * FROM BestEmployee;


