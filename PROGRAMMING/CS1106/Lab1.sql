SELECT *
FROM students;

SELECT first_name , last_name
FROM students;

SELECT first_name , last_name , points
FROM students
ORDER BY points;

SELECT first_name , last_name
FROM students
ORDER BY date_of_birth;

SELECT DISTINCT hometown
FROM students;

SELECT first_name , last_name
FROM students
WHERE points >= 450;

SELECT first_name , last_name
FROM students
WHERE points = 525;

SELECT first_name , last_name
FROM students
WHERE points <> 525;

SELECT first_name , last_name
FROM students
WHERE points BETWEEN 400 AND 500;

SELECT first_name , last_name
FROM students
WHERE hometown = 'Cork';

SELECT first_name , last_name
FROM students
WHERE date_of_birth >= 1994-01-01;

SELECT first_name , last_name , date_of_birth
FROM students
WHERE date_of_birth >= 1992-10-01;

