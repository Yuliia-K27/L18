-- Підключення до бази даних
USE my_first_db;

-- Створення таблиці 'student' з полями 'id' та 'name'
CREATE TABLE student (
  id INT,
  name VARCHAR(255)
);

-- Створення таблиці 'employee' з полями 'id', 'name' та 'salary'
CREATE TABLE employee (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  salary INT(6)
);

-- Зміна типу поля 'id' у таблиці 'student' на PRIMARY KEY
ALTER TABLE student
MODIFY COLUMN id INT PRIMARY KEY;

-- Додавання даних до таблиці 'student'
INSERT INTO student (id, name) VALUES (01, 'John');

-- Додавання даних до таблиці 'employee'
INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000);

-- Видалення таблиці 'student'
DROP TABLE student;

-- Видалення таблиці 'employee'
DROP TABLE employee;
