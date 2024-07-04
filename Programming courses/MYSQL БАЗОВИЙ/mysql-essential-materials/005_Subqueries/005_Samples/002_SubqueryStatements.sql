USE ShopDB;



SELECT * FROM SubTest1 AS ST1					  
WHERE name /* 4 */ = /* 3 */(SELECT name					   
							 FROM SubTest2 AS ST2			   
							 WHERE ST1.id1 = ST2.id2); -- (1)  

SELECT * FROM SubTest1 AS ST1					  
WHERE name=(SELECT name				
			FROM SubTest2 AS ST2			 
			WHERE ST1.id1 = ST2.id2);
			  

SELECT * FROM SubTest1  AS ST1
WHERE EXISTS
    (SELECT * FROM SubTest2	ST2
     WHERE ST1.id1 = ST2.id2);
     								



SELECT * ,(SELECT name	FROM SubTest2 AS ST2 WHERE ST1.id1 = ST2.id2) AS Name2 
FROM SubTest1 AS ST1;


SELECT *,
	   (SELECT id2 FROM SubTest2 AS ST2	WHERE ST1.id1 = ST2.id2) AS Id2,
	   (SELECT name	FROM SubTest2 AS ST2 WHERE ST1.id1 = ST2.id2) AS Name2
FROM SubTest1 AS ST1;
 
SELECT *,
	   (SELECT id2 FROM SubTest2 AS ST2	WHERE ST1.id1 = ST2.id2) AS Id2,
	   (SELECT name	FROM SubTest2 AS ST2 WHERE ST1.id1 = ST2.id2) AS Name2
FROM SubTest1 AS ST1
WHERE ST1.id1 = (SELECT id2 FROM SubTest2 AS ST2 
                  WHERE ST1.id1 = ST2.id2);




SELECT Products.ProdID, Description, Qty, TotalPrice 
   	  FROM Products
INNER JOIN OrderDetails
      ON Products.ProdID = OrderDetails.ProdID;
      

      
SELECT (SELECT  ProdID FROM Products 
	    WHERE Products.ProdID = OrderDetails.ProdID) AS ProdID,
	   (SELECT  Description FROM Products 
	    WHERE Products.ProdID = OrderDetails.ProdID) AS Description, Qty, TotalPrice 
FROM OrderDetails;
	  

SELECT FName, LName, MName, SUM(TotalPrice) AS TotalSold 
		FROM Employees
	     JOIN Orders
			ON Employees.EmployeeID	= Orders.EmployeeID
	     JOIN OrderDetails
			ON Orders.OrderID = OrderDetails.OrderID
GROUP BY  Employees.FName,
		  Employees.LName,  
		  Employees.MName;
		  
 
 
CREATE TEMPORARY TABLE TmpTable
SELECT (SELECT FName FROM Employees 
		WHERE EmployeeID = (SELECT EmployeeID FROM Orders
							WHERE Orders.OrderID = OrderDetails.OrderID)
		) AS FName,
	    (SELECT LName FROM Employees 
		 WHERE EmployeeID = (SELECT EmployeeID FROM Orders
							 WHERE Orders.OrderID = OrderDetails.OrderID)
		) AS LName,
		(SELECT MName FROM Employees 
		 WHERE EmployeeID = (SELECT EmployeeID FROM Orders
							 WHERE Orders.OrderID = OrderDetails.OrderID)
		) AS MName,   
		TotalPrice
FROM OrderDetails;
	

SELECT FName, LName, MName, SUM(TotalPrice) AS TotalSold  FROM TmpTable
GROUP BY FName, LName, MName;