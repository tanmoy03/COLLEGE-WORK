--1
SELECT COUNT(DISTINCT m.title), COUNT(DISTINCT a.name)
FROM movies AS m JOIN actors AS a;

--2
SELECT COUNT(title)
FROM movies
WHERE yr == 1975;

--3
SELECT m.id
FROM 
    actors AS a 
    JOIN castings AS c
    JOIN movies AS m 
    ON a.id = c.actorid
    AND m.id = c.movieid
WHERE a.name = "Clint Eastwood";

--4
SELECT m.title, m.yr 
FROM 
    actors AS a 
    JOIN castings AS c
    JOIN movies AS m 
    ON a.id = c.actorid
    AND m.id = c.movieid
WHERE a.name = "Clint Eastwood"
ORDER BY yr;

--5
SELECT a.name
FROM actors AS a 
    JOIN castings AS c
    JOIN movies AS m 
    ON a.id = c.actorid
    AND m.id = c.movieid
WHERE m.title = "Citizen Kane";

--6
SELECT DISTINCT a.name
FROM actors AS a 
    JOIN castings AS c
    JOIN movies AS m 
    ON a.id = c.actorid
    AND m.id = c.movieid
WHERE m.title = "Vertigo" 
    OR m.title = "Rear Window";

--7
SELECT DISTINCT m.title
FROM actors AS a 
    JOIN castings AS c
    JOIN movies AS m 
    ON a.id = c.actorid
    AND m.id = c.movieid
WHERE m.director = "28";

--8
SELECT DISTINCT m.title
FROM actors AS a 
    JOIN castings AS c
    JOIN movies AS m 
    ON a.id = c.actorid
    AND m.id = c.movieid
WHERE m.director = (
SELECT director
FROM movies 
WHERE title = "Godfather, The");

--9
SELECT DISTINCT m1.title, m1.yr, m2.title, m2.yr
FROM actors AS a 
    JOIN castings AS c
    JOIN movies AS m1
    JOIN movies AS m2 
    ON a.id = c.actorid
    AND m1.id = c.movieid
WHERE m1.title = m2.title
    AND m1.id <> m2.id;

--10
SELECT DISTINCT m.title
FROM movies AS m 
WHERE m.title LIKE "%II%"
    OR m.title LIKE "%III%"
    OR m.title LIKE "%IV%"
    OR m.title LIKE "%V%";


