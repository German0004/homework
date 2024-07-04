USE CarsShop; 

CREATE TABLE cars
(
	car_id int auto_increment,
	mark Varchar(20) NOT NULL,
	model Varchar(20) NULL,
	speed int NOT NULL,
	price int NOT NULL,
    primary key(car_id)
);




INSERT INTO cars             -- Êëþ÷åâîå ñëîâî INTO ìîæíî íå èñïîëüçîâàòü.
(mark, model, speed, price) -- Óêàçàíèå ïîðÿäêà çàïèñè äàííûõ.
VALUES
('BMW', '320d', 225, 36000); -- Ââîäèìûå äàííûå.

INSERT INTO cars             -- Êëþ÷åâîå ñëîâî INTO ìîæíî íå èñïîëüçîâàòü.
(mark, model, speed, price) -- Óêàçàíèå ïîðÿäêà çàïèñè äàííûõ.
VALUES
('Audi', 'A5', 250, 50000); -- Ââîäèìûå äàííûå.

-------------------------------------------------------------------------
INSERT INTO cars             -- Êëþ÷åâîå ñëîâî INTO ìîæíî íå èñïîëüçîâàòü.
(mark, model, speed, price) -- Óêàçàíèå ïîðÿäêà çàïèñè äàííûõ.
VALUES
('Porsche', '911', 285, 100000); 
-------------------------------------------------------------------------

 

