DROP TABLE IF EXISTS winners;

CREATE TABLE winners 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    country TEXT NOT NULL,
    song TEXT NOT NULL,
    performer TEXT NOT NULL,
    points INTEGER
);

INSERT INTO winners (year, country, song, performer, points)
VALUES
    (1956, "Switzerland", "Refrain", "Lys Assia", NULL),
    (1957, "Netherlands", "Net Als Toen", "Corry Brokken", 31),
    (1958, "France", "Dors, Mon Amour", "Andre Claveau", 27),
    (1959, "Netherlands", "Een Beetje", "Teddy Scholten", 21),
    (1960, "France", "Tom Pillibi", "Jacqueline Boyer", 32),
    (1961, "Luxembourg", "Nous les amoureux", "Jean-Claude Pascal", 31),
    (1962, "France", "Un premier amour", "Isabelle Aubret", 26),
    (1963, "Denmark", "Dansevise", "Grethe & Jorgen Ingmann", 42),
    (1964, "Italy", "Non ho l'eta (per amarti)", "Gigliola Cinquetti", 49),
    (1965, "Luxembourg", "Poupee de cire, poupee de son", "France Gall", 32),
    (1966, "Austria", "Merci Cherie", "Udo Jurgens", 31),
    (1967, "United Kingdom", "Puppet on a String", "Sandie Shaw", 42),
    (1968, "Spain", "La, la, la", "Massiel", 29),
    (1969, "Spain", "Vivo Cantando", "Salome", 18),
    (1969, "United Kingdom", "Boom Bang-a-Bang", "Lulu", 18),
    (1969, "Netherlands", "De Troubadour", "Lennie Kuhr", 18),
    (1969, "France", "Un jour, un enfant", "Frida Boccara", 18),
    (1970, "Ireland", "All Kinds of Everything", "Dana (nasty lady)", 32),
    (1971, "Monaco", "Un banc, un arbre, une rue", "Severine", 128),
    (1972, "Luxembourg", "Apres Toi", "Vicky Leandros", 128),
    (1973, "Luxembourg", "Tu Te Reconnaitras", "Anne-Marie David", 129),
    (1974, "Sweden", "Waterloo", "ABBA", 24),
    (1975, "Netherlands", "Ding-A-Dong", "Teach-In", 152),
    (1976, "United Kingdom", "Save Your Kisses for Me", "Brotherhood of Man", 164),
    (1977, "France", "L'Oiseau Et L'Enfant", "Marie Myriam", 136),
    (1978, "Israel", "A-Ba-Ni-Bi", "Izhar Cohen & Alphabeta", 157),
    (1979, "Israel", "Hallelujah", "Gali Atari & Milk and Honey", 125),
    (1980, "Ireland", "What's Another Year?", "Johnny Logan", 143),
    (1981, "United Kingdom", "Making Your Mind Up", "Bucks Fizz", 136),
    (1982, "Germany", "Ein Bisschen Frieden", "Nicole", 161),
    (1983, "Luxembourg", "Si la vie est cadeau", "Corinne Hermes", 142),
    (1984, "Sweden", "Diggi-Loo Diggi-Ley", "Herreys", 145),
    (1985, "Norway", "La det swinge", "Bobbysocks", 123),
    (1986, "Belgium", "J'aime la vie", "Sandra Kim", 176),
    (1987, "Ireland", "Hold Me Now", "Johnny Logan", 172),
    (1988, "Switzerland", "Ne partez pas sans moi", "Celine Dion", 137),
    (1989, "Yugoslavia", "Rock Me", "Riva", 137),
    (1990, "Italy", "Insieme: (1992)", "Toto Cutugno", 149),
    (1991, "Sweden", "Fangad av en stormvind", "Carola", 146),
    (1992, "Ireland", "Why Me", "Linda Martin", 155),
    (1993, "Ireland", "In Your Eyes", "Niamh Kavanagh", 187),
    (1994, "Ireland", "Rock 'n' Roll Kids", "Paul Harrington & Charlie McGettigan", 226),
    (1995, "Norway", "Nocturne", "Secret Garden", 148),
    (1996, "Ireland", "The Voice", "Eimear Quinn", 162),
    (1997, "United Kingdom", "Love Shine a Light", "Katrina and the Waves", 227),
    (1998, "Israel", "Diva", "Dana International", 172),
    (1999, "Sweden", "Take Me to Your Heaven", "Charlotte Nilsson", 163),
    (2000, "Denmark", "Fly on the Wings of Love", "Olsen Brothers", 195),
    (2001, "Estonia", "Everybody", "Tanel Padar, Dave Benton & 2XL", 198),
    (2002, "Latvia", "I Wanna", "Marie N", 176),
    (2003, "Turkey", "Everyway That I Can", "Sertab Erener", 167),
    (2004, "Ukraine", "Wild Dances", "Ruslana", 280),
    (2005, "Greece", "My Number One", "Helena Paparizou", 230),
    (2006, "Finland", "Hard Rock Hallelujah", "Lordi", 292),
    (2007, "Serbia", "Molitva", "Marija Serifovic", 268),
    (2008, "Russia", "Believe", "Dima Bilan", 272),
    (2009, "Norway", "Fairytale", "Alexander Rybak", 387),
    (2010, "Germany", "Satellite", "Lena", 246),
    (2011, "Azerbaijan", "Running Scared", "Ell/Nikki", 221),
    (2012, "Sweden", "Euphoria", "Loreen", 372),
    (2013, "Denmark", "Only Teardrops", "Emmelie de Forest", 281),
    (2014, "Austria", "Rise Like a Phoenix", "Conchita Wurst", 290),
    (2015, "Sweden", "Heroes", "Mans Zelmerlow", 365),
    (2016, "Ukraine", "1944", "Jamala", 534),
    (2017, "Portugal", "Amar pelos dois", "Salvador Sobral", 758),
    (2018, "Israel", "Toy", "Netta", 529),
    (2019, "Netherlands", "Arcade", "Duncan Laurence", 498),
    (2021, "Italy", "Zitti e buoni", "Maneskin", 524)
;

DROP TABLE IF EXISTS countries;

CREATE TABLE countries
(
    code TEXT PRIMARY KEY,
    country TEXT NOT NULL
);

INSERT INTO countries (code, country)
VALUES
    ("AUT", "Austria"),
    ("AZE", "Azerbaijan"),
    ("BEL", "Belgium"),
    ("CHE", "Switzerland"),
    ("DEU", "Germany"), 
    ("DNK", "Denmark"),
    ("ESP", "Spain"),
    ("EST", "Estonia"),
    ("FIN", "Finland"),
    ("FRA", "France"),
    ("GBR", "United Kingdom"),
    ("GRC", "Greece"),
    ("IRL", "Ireland"),
    ("ISR", "Israel"),
    ("ITA", "Italy"),
    ("LUX", "Luxembourg"),
    ("LVA", "Latvia"),
    ("MCO", "Monaco"),
    ("NLD", "Netherlands"),
    ("NOR", "Norway"), 
    ("PRT", "Portugal"),
    ("RUS", "Russia"),
    ("SRB", "Serbia"), 
    ("SWE", "Sweden"),
    ("TUR", "Turkey"),
    ("UKR", "Ukraine"),
    ("YUG", "Yugoslavia")
;

