SELECT *
FROM persons;

SELECT first_name, last_name
FROM persons
WHERE first_name LIKE "A%";

SELECT first_name, last_name
FROM persons
WHERE first_name LIKE "%A";

SELECT first_name, last_name
FROM persons
WHERE first_name LIKE "%A%";

SELECT first_name, last_name
FROM persons
WHERE length(first_name) = 5;

SELECT first_name, last_name
FROM persons
WHERE street lIKE "%street%";

SELECT food
FROM likes
WHERE food LIKE "% %";

SELECT food
FROM likes
WHERE food LIKE "%te%";

SELECT *
FROM likes
JOIN persons;

SELECT *
FROM likes
JOIN persons
    ON persons.person_id = likes.person_id;

SELECT food, first_name, last_name
FROM likes AS f
JOIN persons AS p
ON p.first_name = "Aoife" AND p.last_name = "Ahern";

SELECT food, first_name, last_name
FROM likes AS f
JOIN persons AS p
    ON p.person_id = f.person_id
WHERE county = "Cork";

SELECT DISTINCT food
FROM persons
JOIN likes 
WHERE gender = "F";

SELECT DISTINCT first_name, last_name
FROM persons JOIN likes 
WHERE food = "Pizza";

SELECT DISTINCT town
FROM persons JOIN likes
WHERE food = "Beer";

SELECT *
FROM 
    likes AS f1 JOIN
    likes AS f2;

SELECT *
FROM 
    likes AS f1 JOIN
    likes AS f2
    ON f1.person_id = f2.person_id
WHERE f1.food = f2.food;

SELECT f1.person_id
FROM 
    likes AS f1 JOIN
    likes AS f2
    ON f1.person_id = f2.person_id
WHERE 
    f1.food = "Pizza"
 AND   f2.food = "Nutella";

SELECT person_id
FROM likes
WHERE food = "Pizza"
    OR food = "Nutella"

SELECT p.first_name, p.last_name
FROM 
    persons AS p JOIN 
    likes as F
    ON p.person_id == F.person_id
WHERE 
    p.town = "Cork"
 AND F.food = "Beer";
   
SELECT p.first_name, p.last_name
FROM 
    persons AS p 
    JOIN likes AS f1
    JOIN likes AS f2
    ON p.person_id = f1.person_id
WHERE f1.food = "Pizza"
AND f2.food = "Nutella";

SELECT p.first_name, p.last_name
FROM
    persons AS p 
    JOIN likes as f
    ON p.person_id = f.person_id
WHERE food = "Pizza" 
OR food = "Nutella";

SELECT *
FROM
    persons AS p1 JOIN
    persons AS p2;

SELECT p1.first_name, p1.last_name
FROM
    persons AS p1 JOIN
    persons AS p2
    ON p1.birth_date = p2.birth_date
    AND p1.person_id <> p2.person_id;


