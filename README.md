# L18
1) SQL. Написати програму, яка створює нову базу даних 'my_first_db'.
2) Написати програму, яка створить у базі 'my_first_db', таблицю 'student', з полями 'id'(INT) і 'name'(VARCHAR(255)).
3) Написати програму, яка створить у базі даних 'my_first_db', таблицю 'employee', з полями 'id'(INT AUTO_INCREMENT PRIMARY KEY), 'name'(VARCHAR(255)) і 'salary'(INT(6))
4) Написати програму, яка змінює у таблиці 'student' поле 'id' на PRIMARY KEY
5) Написати програму, яка додає до таблиці 'student' дані (01, 'John'), а до таблиці 'employee' - (01, 'John', 10000)


Рішення:

У цьому коді спочатку підключаємось до бази даних 'my_first_db' за допомогою команди USE. 
Далі створюємо таблиці 'student' і 'employee' за допомогою команди CREATE TABLE, яка приймає назву таблиці і опис її структури - поля з їхніми типами даних. 
У таблиці 'employee' для поля 'id' використовується параметр AUTO_INCREMENT, щоб значення цього поля автоматично збільшувались з кожним новим записом.

Потім використовуємо команду ALTER TABLE для зміни типу поля 'id' у таблиці 'student' на PRIMARY KEY.

Далі додаємо дані до таблиць 'student' і 'employee' за допомогою команди INSERT INTO, яка приймає назву таблиці, назви полів, до яких додається інформація, та їхні значення. 
Використовується параметр VALUES, щоб передати значення полів.

Видаляємо таблиці 'student' і 'employee' за допомогою команди DROP TABLE.
