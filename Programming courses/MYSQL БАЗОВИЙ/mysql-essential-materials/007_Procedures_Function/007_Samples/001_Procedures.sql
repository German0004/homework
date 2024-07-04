USE carsshop;

DELIMITER |

DROP procedure getAllClients; |
CREATE PROCEDURE getAllClients()
BEGIN
    SELECT * FROM clients;
END
|

DELIMITER |
CALL getAllClients();
|



----------------------------------------------------------------------



DELIMITER |
DROP PROCEDURE clientsByName; |

CREATE PROCEDURE clientsByName ( IN cname nvarchar(25) )  
BEGIN
	SELECT * FROM clients WHERE name = cname;
END
|

DELIMITER |
CALL clientsByName('Petro');
|

DELIMITER |
CREATE PROCEDURE clientsByName (IN cname nvarchar(25) )

BEGIN
   IF (cname IS NOT NULL)  
   THEN
	
	SELECT * FROM clients WHERE name like cname; 
    ELSE				
	
	SELECT 'Bad error';
    END IF;
 END
|


DELIMITER |
CALL clientsByName('%t%');  |  

CALL clientsByName('vi%');  
|


------------------------------------------------------------------------------

DELIMITER |
DROP PROCEDURE countClients; |


CREATE PROCEDURE countClients (OUT info int) 

BEGIN
	SELECT Count(*) into info From clients;
END
|

DELIMITER |
CALL countClients(@result);
|

SELECT @result;

|



DELIMITER |
DROP PROCEDURE factorial; |

CREATE PROCEDURE factorial (IN valueIn INT)

BEGIN
	DECLARE inWorking int DEFAULT 1;
    DECLARE result int DEFAULT 1;
    
	WHILE (inWorking <= valueIn)
	 DO
		SET result = result * inWorking;
		SET inWorking = inWorking + 1;
    END WHILE;
    
    SELECT result;
END;
|

DELIMITER |
CALL factorial(5);
|




