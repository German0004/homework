USE ShopDB;



SELECT * FROM JoinTest1 
UNION 
SELECT * FROM JoinTest2 ;


SELECT * FROM JoinTest1 
UNION ALL
SELECT * FROM JoinTest2;




SELECT * FROM JoinTest1
LEFT JOIN JoinTest2 ON id_jt1=id_jt2
UNION
SELECT * FROM JoinTest1
RIGHT JOIN JoinTest2 ON id_jt1=id_jt2;



