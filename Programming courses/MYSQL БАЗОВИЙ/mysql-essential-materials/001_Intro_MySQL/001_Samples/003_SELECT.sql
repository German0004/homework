USE CarsShop;


SELECT * FROM cars; 

-- Ïðîèçâîäèì âûáîðêó äàííûõ èç ñòîëáöà FstName, òàáëèöû MyFriends
SELECT mark FROM cars; 

-- Ïðîèçâîäèì âûáîðêó äàííûõ èç ñòîëáöà LstName, òàáëèöû MyFriends
SELECT model FROM cars; 

SELECT speed FROM cars; 

-- Ïðîèçâîäèì âûáîðêó äàííûõ èç ñòîëáöîâ FstName è LstName, òàáëèöû MyFriends
SELECT mark, speed FROM cars; 

-- Ïðîèçâîäèì âûáîðêó äàííûõ èç ñòîëáöîâ FstName, LstName è BthDate, òàáëèöû MyFriends
SELECT mark, model, price FROM cars; 





SELECT name, age, phone FROM carsshop.clients; -- Sales - ñõåìà


SELECT * FROM carsshop.clients
WHERE id = 1; 


SELECT * FROM carsshop.clients
WHERE id > 2; 


SELECT * FROM carsshop.clients 
WHERE id BETWEEN 1 AND 3; -- Â êîíñòðóêöèè WHERE ïðèìåíåíà îïåðàöèÿ ïðîâåðêè äèàïàçîíà.


SELECT * FROM carsshop.clients 
WHERE name = 'Andrew' OR  name ='Sergey'; -- Ëîãè÷åñêàÿ îïåðàöèÿ "ÈËÈ"


SELECT * FROM carsshop.clients 
WHERE name = 'Andrew' AND age > 18; -- Â êîíñòðóêöèè WHERE ïðèìåíåíà îïåðàöèÿ ïðîâåðêè äèàïàçîíà.



SELECT name, age FROM carsshop.clients  
WHERE NOT name = 'Andrew';



SELECT name, age FROM carsshop.clients 
WHERE phone LIKE '05%';

SELECT name, age FROM carsshop.clients 
WHERE phone LIKE '%03';  -- Âûáîðêà ïóñòàÿ ïîòîìó ÷òî òàêîãî çíà÷åíèÿ êàê 'Dis%' íåò â òàáëèöå
						  
-- Ïðîèçâîäèì âûáîðêó äàííûõ èç ñòîëáöîâ CardType è ExpYear, òàáëèöû CreditCard,
-- ãäå çíà÷åíèÿ ÿ÷ååê ñòîëáöà CardType ñîîòâåòñòâóþò øàáëîíó	'Vis__'
SELECT name, age FROM carsshop.clients 
WHERE phone LIKE '%507%';  




-- Ïðîèçâîäèì âûáîðêó âñåõ äàííûõ èç òàáëèöû CreditCard, 
-- ãäå çíà÷åíèÿ ÿ÷ååê ñòîëáöà ExpMonth ðàâíÿþòñÿ îäíîìó èç çíà÷åíèé ðÿäà (1, 5, 11)
SELECT * FROM carsshop.clients  WHERE age IN (20, 22, 23); -- IN (1, 5, 11) îïðåäåëÿåò çíà÷åíèÿ ExpMonth ðàâíûå 1 èëè 5 èëè 11 

SeLeCt * from carsshop.clients  where age = 20 or age= 22 or age = 23;
