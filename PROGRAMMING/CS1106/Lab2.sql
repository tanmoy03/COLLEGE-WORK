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

SELECT name
FROM countries
WHERE region ;