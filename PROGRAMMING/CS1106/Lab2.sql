SELECT MAX(area)
FROM countries;

SELECT MAX(area)
FROM countries
WHERE region = "Africa";

SELECT SUM(gdp)
FROM countries
WHERE region="Europe";

SELECT name
FROM countries
WHERE gdp IS NULL;

SELECT name
FROM countries
WHERE gdp IS NOT NULL;

SELECT region, AVG(gdp)
FROM countries
GROUP BY region;

SELECT region, COUNT(*), SUM(population)
FROM countries
WHERE region IN ("Europe", "Middle East", "Africa")
GROUP BY region;

SELECT SUM(population), SUM(area), SUM(gdp)
FROM countries
WHERE name IN ("France", "Germany", "Spain");

SELECT region, COUNT(*)
FROM countries 
WHERE population > 100000000
GROUP BY region;

SELECT region, name 
FROM countries
ORDER BY region, population DESC;

SELECT region, COUNT(*), SUM(area)/SUM(population)
FROM countries
GROUP BY region
HAVING SUM(population) > 1000000000;

SELECT c2.region, c2.name
FROM 
    countries AS c1 JOIN
    countries AS c2
    ON c1.region = c2.region
WHERE c1.name = "Jordan";

SELECT COUNT(*)
FROM 
    countries AS c1 JOIN
    countries AS c2
    ON c1.region = c2.region
WHERE c1.name = "Jordan";

SELECT c2.name 
FROM
    countries AS c1 JOIN
    countries AS c2
    ON c1.region = c2.region 
WHERE c1.name = "Spain"
AND c2.area > c1.area;

SELECT MIN(c2.population)
FROM 
    countries AS c1 JOIN
    countries AS c2
    ON c1.region = c2.region
WHERE c1.name = "China";


