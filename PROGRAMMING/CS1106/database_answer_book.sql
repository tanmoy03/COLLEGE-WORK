--
--                CS1106/CS6503 Examination
--                Friday, 17 December 2021
--

-- Student Number: 121324683
-- Place X in box if registestered with DSS: [ ]

--                  Student Declaration
-- ==================================================================

-- This is to certify that the work I am submitting is my own and has 
-- been done by me solely and not in consultation with anyone else. 
-- Neither I nor anyone else have submitted this work for assessment, 
-- either at University College Cork or elsewhere. I have read and 
-- understood the regulations of University College Cork concerning 
-- plagiarism.  Where breaches of the declaration are detected, these 
-- will be reviewed under UCC student conduct and plagiarism policies. 
-- Any breach of the examination rules is a serious issue and can incur 
-- penalties.

-- ALL ANSWERS SUBMITTED WILL BE CHECKED FOR COMPLIANCE WITH UNIVERSITY
-- PLAGIARISM POLICY.

-- ==================================================================
-- QUESTION ONE
-- ------------------------------------------------------------------
-- Part (i) 
-- ...................................................................


-- Part (ii)
-- ...................................................................

-- ==================================================================
-- QUESTION TWO
-- ------------------------------------------------------------------
-- Part (i)
INSERT INTO children(id, first_name, last_name, dob, gender, niceness)
VALUES('001', 'Ian', 'McCarthy', '2015-01-19', 'Male', '0.94');
INSERT INTO children(id, first_name, last_name, dob, gender, niceness)
VALUES('002', 'Kars', 'Dio', '2011-06-24', 'Female', '0.69');
INSERT INTO children(id, first_name, last_name, dob, gender, niceness)
VALUES('003', 'Cristiano', 'Penaldo', '2013-09-01', 'Male', '0.22'); 
-- ...................................................................


-- Part (ii)
DELETE 
FROM children 
WHERE niceness < 0.25;
-- ...................................................................


-- Part (iii) 
UPDATE children
SET niceness = niceness - (niceness*0.1)
WHERE gender = 'Male';
-- ...................................................................


-- Part (iv)
SELECT first_name, last_name, niceness
FROM children
WHERE dob BETWEEN '2011-12-25' AND '2021-12-25';
-- ...................................................................


-- Part (v) 
-- ...................................................................



-- ==================================================================
-- QUESTION THREE
-- ------------------------------------------------------------------

-- Part (i) 
SELECT c.name, cl.language, cl.percentage
FROM countries AS c JOIN
    country_languages AS cl
    ON c.code = cl.country_code
WHERE cl.language = "French" AND 
    cl.percentage >= 25;
-- ...................................................................



-- Part (ii)
SELECT COUNT(c2.id), continent
FROM countries AS c1 JOIN
    cities AS c2
    ON c1.code = c2.country_code
WHERE c2.population > 5000000
GROUP BY continent;
-- ...................................................................



-- Part (iii) 
SELECT language, percentage
FROM countries AS c JOIN 
    country_languages AS cl 
    ON cl.country_code = c.code 
ORDER BY cl.percentage DESC;
-- ...................................................................


-- Part (iv)
SELECT c1.name, MAX(c1.population)
FROM cities AS c1
    JOIN countries AS c2
    ON c1.country_code = c2.code
WHERE c1.id = c2.capital;
-- ...................................................................


-- Part (v)
SELECT cl.language
FROM country_languages AS cl
    JOIN countries AS c
    ON cl.country_code = c.code
    AND cl.percentage >= 15
GROUP BY cl.language
HAVING COUNT(c.name) >= 3
    AND COUNT(DISTINCT c.continent) >= 3;
-- ...................................................................


-- Part (vi)
SELECT name, continent, MAX(life_expectancy)
FROM countries 
GROUP BY continent 
UNION 
SELECT name, continent, MIN(life_expectancy)
FROM countries
GROUP BY continent;
-- ...................................................................
