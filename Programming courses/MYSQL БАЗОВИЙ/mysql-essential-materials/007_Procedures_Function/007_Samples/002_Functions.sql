
USE ShopDB;

DELIMITER |
CREATE FUNCTION Hello() 
RETURNS varchar(30)     
BEGIN 
DECLARE MyVar varchar(20);
SET MyVar = 'Hello World!';
RETURN MyVar; 
END; 
|

DELIMITER |
 SELECT Hello();
|


drop database carsshop; |

create database carsshop; |

use carsshop; |


create table marks(
   id int not null auto_increment primary key,
   mark varchar(20) unique
); |

create table cars(
  id INT NOT NULL auto_increment primary key,
  mark_id INT NOT NULL,
  model varchar(20) NOT NULL,
  price INT NOT NULL,
  foreign key(mark_id) references marks(id)
); |

CREATE TABLE clients
(
	
	 id INT AUTO_INCREMENT NOT NULL,
     name VARCHAR(30),
     age TINYINT,
     phone VARCHAR(15),
     PRIMARY KEY (id)
); |

create table orders(
     id int not null primary key auto_increment,
     car_id int not null,
     client_id int not null,
     foreign key(car_id) references cars(id),
     foreign key(client_id) references clients(id)
); |

INSERT into marks(mark) values('Audi');|
INSERT into marks(mark) values('Porsche'); |

insert into cars(mark_id, model, price) values (1, 'A5', 50000); |
insert into cars(mark_id, model, price) values (2, 'panamera', 100000); |
insert into cars(mark_id, model, price) values (2, 'caymen S', 88000); |

insert into clients(name, age) values ('petro', 20), ('vasya', 25), ('vitaly', 75); |

insert into orders(car_id, client_id) values(1, 1), (2, 2), (1, 3); |

SELECT m.mark, avg(age) FROM marks m 
    INNER JOIN cars c ON m.id = c.mark_id
    INNER JOIN orders o ON o.car_id = c.id
    INNER JOIN clients cl ON o.client_id = cl.id
    GROUP BY m.mark;
    
|
DELIMITER |
CREATE FUNCTION AverageAge(mark varchar(45)) 
RETURNS INT
BEGIN
    RETURN (SELECT AVG(cl.age) FROM clients cl 
            INNER JOIN orders o ON cl.id = o.client_id
			INNER JOIN cars c ON c.id = o.car_id
            INNER JOIN marks m ON c.mark_id = m.id WHERE m.mark = mark);
END
| 

SELECT mark, AverageAge(mark) FROM marks; |

DELIMITER |
DROP FUNCTION AveragePrice; |
CREATE FUNCTION AveragePrice(mark varchar(45))
RETURNS INT
BEGIN
   RETURN (SELECT avg(c.price) FROM cars c 
   INNER JOIN marks m ON m.id = c.mark_id WHERE m.mark = mark);
END
|

SELECT mark, AveragePrice(mark) FROM marks; |

   