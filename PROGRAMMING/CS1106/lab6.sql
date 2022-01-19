-- SELECT *
-- FROM cities;

-- SELECT *
-- FROM countries;

-- SELECT * 
-- FROM country_languages;

-- --Q1
-- SELECT name, population
-- FROM cities
-- ORDER BY population DESC
-- LIMIT 20;

-- --Q2
-- SELECT c.name, c.code, COUNT(*)
-- FROM countries as c
--     JOIN cities as ci
--     ON ci.country_code = c.code
-- WHERE ci.population >= 1000000
-- GROUP BY c.code
-- HAVING COUNT(*) >= 5
-- ORDER BY COUNT(*) DESC;

-- --Q3
-- SELECT name, indep_year
-- FROM countries 
-- WHERE indep_year >= 
-- (   SELECT indep_year
--     FROM countries
--     WHERE name = "India"
-- )
-- ORDER BY indep_year;


-- --Q4 
-- SELECT language, COUNT(*)
-- FROM countries AS c
--     JOIN country_languages AS cl
--     ON c.code = cl.country_code
-- WHERE cl.percentage >= 25
-- GROUP BY cl.language
-- HAVING COUNT(*) >= 6;

--Q5 
-- SELECT *
-- FROM countries
-- WHERE code IN 
-- (SELECT code 
-- FROM
--     SELECT * 
--     FROM (SELECT *
--     FROM countries
--     WHERE gnp IS NOT NULL
--         AND population > 0
--     ORDER BY life_expectancy
--     LIMIT 20
--     )

--     UNION ALL

--     SELECT *
--     FROM 
--     (SELECT *
--     FROM countries
--     ORDER BY gnp/population
--     LIMIT 20
--     )  AS poorcountries
--     GROUP BY code
--     HAVING COUNT(*) > 1)
-- );

-- --6
-- SELECT name, surface_area
-- FROM countries AS c1
-- WHERE surface_area >= 0.1*
-- (   SELECT SUM(surface_area)
--     FROM countries AS c2
--     WHERE c1.continent = c2.continent
-- );

-- --7
-- SELECT 
-- (   SELECT gnp
--     FROM
--     (    SELECT gnp
--         FROM countries
--         ORDER BY gnp DESC
--         LIMIT 20
--     )AS richest20
-- )/
-- (   SELECT SUM(gnp)
--     FROM countries
-- );

SELECT capital, name
FROM countries;

SELECT id, name
FROM cities;