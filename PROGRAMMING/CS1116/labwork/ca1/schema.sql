DROP TABLE IF EXISTS users;

CREATE TABLE users 
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
);


DROP TABLE IF EXISTS vinyls;

CREATE TABLE vinyls 
(
    vinyl_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist TEXT NOT NULL,
    price REAL NOT NULL,
    genre TEXT,
    description TEXT
);

INSERT INTO vinyls (name, artist, price, genre, description)
VALUES
    ('My Beautiful Dark Twisted Fantasy', 'Kanye West', 55.25, 'Rap', 'Kanye Wests magnum opus. A certified three times platinum album that helped change Hip-Hop forever.'),
    ('Thriller', 'Michael Jackson', 35.15, 'Pop', 'Thriller remains as the best selling album of all time with a 34x Platinum certification. The "King of Pop" at his best.'),
    ('Currents', 'Tame Impala', 30.95, 'Indie', 'A psychedelic pop album for the senses. Bittersweet yet warm this albums replayability is matched by few.'),
    ('Rodeo', 'Travis Scott', 27.95, 'Rap', 'A foundation for Hip-Hop as we know it today. Created a whole new genre of rap with its psychedelic trap instrumentals and haunting vocals.'),
    ('Beauty Behind The Madness', 'The Weeknd', 34.75, 'R&B', 'Including massive hits like "The Hills" and "Cant Feel My Face", this album is one for the ages.'),
    ('Blonde', 'Frank Ocean', 45.85, 'R&B', 'Heart-wrenching album that will leave you in a mess. Have a tissue box ready at all times for this one.'),
    ('Salad Days', 'Mac DeMarco', 32.75, 'Indie', 'Something so peaceful about Macs voice. This is the album for a rainy day.'),
    ('In the Court of the Crimson King', 'King Crimson', 45.85, 'Rock', 'Complex, poetic and melancholic. Progressive Rock at its finest.'),
    ('Kid A', 'Radiohead', 52.35, 'Rock', 'Its a Radiohead album.'),
    ('Madvillainy', 'Madvillain', 61.25, 'Rap', 'Abstract Hip-Hop was made from this incredible collaboration from rapper MF DOOM and MC Madlib. Mind-bending instrumentals with tongue-twisting flows from the late great.'),
    ('Purple Rain', 'Prince', 55.75, 'Pop', 'Believed to be as if not more talented than MJ himself, Purple Rain was Prince at his best.');