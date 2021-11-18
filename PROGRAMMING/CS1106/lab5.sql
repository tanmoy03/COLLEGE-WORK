SELECT *
FROM movies;

SELECT *
FROM actors;

SELECT *
FROM castings;

-- 1
SELECT actorid
FROM castings
WHERE movieid ==
(   SELECT id
    FROM movies 
    WHERE title = "Big Sleep, The"
);

-- 2
SELECT title
FROM movies 
WHERE director =
(   SELECT director
    FROM movies 
    WHERE title = "Citizen Kane"
)
ORDER BY yr;

-- 3
SELECT name 
FROM actors 
WHERE id =
(   SELECT actorid
    FROM castings
    WHERE movieid = 
    (   SELECT id
        FROM movies 
        WHERE title = "Big Sleep, The"
    )
);

-- 4
SELECT id
FROM movies 
WHERE yr = "1950"
UNION
SELECT movieid 
FROM castings
WHERE actorid = 
(   SELECT id
    FROM actors
    WHERE name = "Elizabeth Taylor"
);

-- 5
SELECT title, score
FROM movies
WHERE score =
(   SELECT MAX(score)
    FROM movies
);

-- 6
SELECT actorid
FROM castings 
