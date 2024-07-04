USE shopdb;


CREATE TABLE IF NOT EXISTS users(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(32) NOT NULL UNIQUE,
password VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
created_at DATETIME NOT NULL,
updated_at DATETIME NOT NULL);

CREATE TABLE IF NOT EXISTS profiles(
id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT NOT NULL,
name VARCHAR(100),
last_name VARCHAR(100),
photo_path VARCHAR(100),
about TEXT, 
FOREIGN KEY(user_id) REFERENCES users(id));

DROP TRIGGER IF EXISTS new_profile;

DELIMITER |
CREATE TRIGGER new_profile 
AFTER INSERT ON users 
FOR EACH ROW 
  BEGIN
    INSERT INTO profiles(user_id) VALUES(NEW.id);
 END;
    |
    
DROP TRIGGER IF EXISTS update_user; |

DELIMITER |
CREATE TRIGGER update_user 
AFTER UPDATE ON profiles 
FOR EACH ROW 
  BEGIN
    UPDATE users SET updated_at = NOW() WHERE id = OLD.user_id;
 END;
    |
    
DROP TRIGGER IF EXISTS delete_profile; |

DELIMITER |
CREATE TRIGGER delete_profile
BEFORE DELETE ON users 
FOR EACH ROW 
  BEGIN
    DELETE FROM profiles WHERE id = OLD.id;
 END;
    |
    
INSERT INTO users(username,password ,email ,created_at, updated_at) 
VALUES ('Draw', 'pp', 'sql@mail.ru', NOW(), NOW()); |

SELECT * FROM users; |
SELECT * FROM profiles; |

UPDATE profiles SET about = 'I am pushkin' WHERE user_id = 1; |

SELECT * FROM users; |
SELECT * FROM profiles; |

DELETE FROM users WHERE id = 1; |

SELECT * FROM users; |
SELECT * FROM profiles; |

