USE carsshop;


SELECT mark, model 
FROM carsshop.cars
WHERE speed IN (225, 240, 250);



SELECT mark, SUM(speed) 
FROM carsshop.cars
WHERE speed IN (225, 240, 250)
GROUP BY mark; 


SELECT car_id AS ID, SUM(speed) AS Total 
FROM carsshop.cars
WHERE speed IN (225, 240, 250)
GROUP BY model; 


SELECT COUNT(*) AS Emp
FROM carsshop.cars; 

SELECT mark, avg(speed) AS AVERAGE_SPEED
FROM carsshop.cars group by mark
HAVING avg(speed) > 230; 


SELECT mark, COUNT(*) AS TOTAL
FROM carsshop.cars
WHERE speed IN (225, 240, 250)
GROUP BY mark
HAVING COUNT(*) > 3;