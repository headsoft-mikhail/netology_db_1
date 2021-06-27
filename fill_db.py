import create_db
import passwords
import random

db_name = 'music'
db_password = passwords.db_password
db = create_db.open_db(db_name, db_password)

artists_data = [
    {'artist': 'Limp Bizkit',
     'genres': ['rock', 'hip-hop', 'metal'],
     'albums': [{'album': 'Chocolate Starfish and the Hot Dog Flavored Water',
                 'year': 2000,
                 'tracks': [{'track': 'My Generation', 'continuity': 221},
                            {'track': 'My Way', 'continuity': 273},
                            {'track': 'Rollin’ (Air Raid Vehicle)', 'continuity': 214},
                            {'track': 'Take a Look Around', 'continuity': 318}
                            ]
                 },
                {'album': 'Results May Vary',
                 'year': 2003,
                 'tracks': [{'track': 'Re-Entry', 'continuity': 157},
                            {'track': 'Eat You Alive', 'continuity': 237},
                            {'track': 'Gimme The Mic', 'continuity': 185},
                            {'track': 'Underneath The Gun', 'continuity': 342},
                            {'track': 'Down Another Day', 'continuity': 246},
                            {'track': 'Build A Bridge', 'continuity': 278},
                            {'track': 'Red Light-Green Light', 'continuity': 237},
                            {'track': 'The Only One', 'continuity': 336},
                            {'track': 'Behind Blue Eyes', 'continuity': 365}
                            ]
                 }
                ]
     },
    {'artist': 'Lera Lynn',
     'genres': ['rock', 'country', 'folk'],
     'albums': [{'album': 'The Avenues',
                 'year': 2014,
                 'tracks': [{'track': 'Standing on the Moon', 'continuity': 260},
                            {'track': 'Coming down', 'continuity': 232},
                            {'track': 'Hooked on You', 'continuity': 237},
                            {'track': 'Sailor Song', 'continuity': 240}
                            ]
                 },
                {'album': 'Resistor',
                 'year': 2016,
                 'tracks': [{'track': 'Shape Shifter', 'continuity': 231},
                            {'track': 'What You Done', 'continuity': 236},
                            {'track': 'Scratch + Hiss', 'continuity': 297}
                            ]
                 },
                {'album': 'Plays Well With Others',
                 'year': 2018,
                 'tracks': [{'track': 'Lose Myself', 'continuity': 210},
                            {'track': 'Crimson Underground', 'continuity': 189},
                            {'track': 'In Another Life', 'continuity': 212}
                            ]
                 }
                ]
     },
    {'artist': 'Lady Gaga',
     'genres': ['pop', 'hip-hop'],
     'albums': [{'album': 'Born This Way',
                 'year': 2014,
                 'tracks': [{'track': 'Judas', 'continuity': 262},
                            {'track': 'Americano', 'continuity': 246},
                            {'track': 'Hair', 'continuity': 250},
                            {'track': 'Bad Kids', 'continuity': 231}
                            ]
                 }
                ]
     },
    {'artist': 'Metallica',
     'genres': ['rock', 'metal'],
     'albums': [{'album': 'Black Album',
                 'year': 1991,
                 'tracks': [{'track': 'Enter Sandman', 'continuity': 330},
                            {'track': 'Sad but True', 'continuity': 323},
                            {'track': 'The Unforgiven', 'continuity': 227},
                            {'track': 'Nothing Else Matters', 'continuity': 386}
                            ]
                 }
                ]
     },
    {'artist': '50 Cent',
     'genres': ['hip-hop'],
     'albums': [{'album': 'The Massacre',
                 'year': 2005,
                 'tracks': [{'track': 'In My Hood', 'continuity': 231},
                            {'track': 'This Is 50', 'continuity': 184},
                            {'track': 'Piggy Bank', 'continuity': 255}
                            ]
                 }
                ]
     },
    {'artist': 'Eminem',
     'genres': ['hip-hop'],
     'albums': [{'album': 'The Marshall Mathers LP',
                 'year': 2000,
                 'tracks': [{'track': 'Stan', 'continuity': 344},
                            {'track': 'Marshall Mathers', 'continuity': 321},
                            {'track': 'Under the Influence', 'continuity': 322}
                            ]
                 }
                ]
     },
    {'artist': 'Dido',
     'genres': ['hip-hop'],
     'albums': [{'album': 'The Marshall Mathers LP',
                 'year': 2000,
                 'tracks': [{'track': 'Stan', 'continuity': 344}
                            ]
                 }
                ]
     },
    {'artist': 'Iggy Pop',
     'genres': ['rock'],
     'albums': [{'album': 'The Idiot',
                 'year': 1977,
                 'tracks': [{'track': 'Sister Midnight', 'continuity': 263},
                            {'track': 'Nightclubbing', 'continuity': 258},
                            {'track': 'Funtime', 'continuity': 173},
                            {'track': 'Baby', 'continuity': 200}
                            ]
                 }
                ]
     },
    {'artist': 'Johny Cash',
     'genres': ['rock', 'country', 'folk'],
     'albums': [{'album': 'American III: Solitary Man',
                 'year': 2000,
                 'tracks': [{'track': 'Solitary Man', 'continuity': 205},
                            {'track': 'One', 'continuity': 233},
                            {'track': 'I See a Darkness', 'continuity': 222},
                            {'track': 'Country Trash', 'continuity': 107}
                            ]
                 }
                ]
     },
    {'artist': 'Disturbed',
     'genres': ['metal'],
     'albums': [{'album': 'The Sickness',
                 'year': 2000,
                 'tracks': [{'track': 'Stupify', 'continuity': 274},
                            {'track': 'Down with the Sickness', 'continuity': 278},
                            {'track': 'Violence Fetish', 'continuity': 203}
                            ]
                 },
                {'album': 'Believe',
                 'year': 2002,
                 'tracks': [{'track': 'Prayer', 'continuity': 221},
                            {'track': 'Liberate', 'continuity': 209},
                            {'track': 'Awaken', 'continuity': 269}
                            ]
                 }
                ]
     }
]

for artist in artists_data:
    db.execute(f"""INSERT INTO Artists (name) 
                   VALUES ('{artist['artist']}') 
                   ON CONFLICT DO NOTHING;""")
    artistid = db.execute(f"SELECT id FROM Artists WHERE name = '{artist['artist']}'").fetchone()[0]
    for genre in artist['genres']:
        db.execute(f"""INSERT INTO Genres (name) 
                       VALUES ('{genre}') 
                       ON CONFLICT DO NOTHING;""")
        genreid = db.execute(f"SELECT id FROM Genres WHERE name = '{genre}'").fetchone()[0]
        db.execute(f"""INSERT INTO ArtistsGenres (artistid, genreid) 
                       VALUES ('{artistid}', '{genreid}') 
                       ON CONFLICT DO NOTHING;""")
    for album in artist['albums']:
        db.execute(f"""INSERT INTO Albums (name, year) 
                       VALUES ('{album['album']}', '{album['year']}') 
                       ON CONFLICT DO NOTHING;""")
        albumid = db.execute(f"SELECT id FROM Albums WHERE name = '{album['album']}'").fetchone()[0]
        db.execute(f"""INSERT INTO AlbumsArtists (artistid, albumid) 
                       VALUES ('{artistid}', '{albumid}') 
                       ON CONFLICT DO NOTHING;""")
        for track in album['tracks']:
            albumid = db.execute(f"SELECT id FROM Albums WHERE name = '{album['album']}'").fetchone()[0]
            db.execute(f"""INSERT INTO Tracks (name, albumid, continuity) 
                           VALUES ('{track['track']}', {albumid}, '{track['continuity']}') 
                           ON CONFLICT DO NOTHING;""")

tracksids = [tracknum[0] for tracknum in db.execute(f"SELECT id FROM Tracks ORDER BY id DESC;").fetchall()]
for i in range(1, 10):
    tracks = []
    for count in range(5, 15):
        tracks.append(random.choice(tracksids))
    tracks = list(set(tracks))
    collection = {'name': f'Random Collection {i}',
                  'year': 2012 + i,
                  'trackids': tracks
                  }
    db.execute(f"""INSERT INTO Collections (name, year) 
               VALUES ('{collection['name']}', '{collection['year']}') 
               ON CONFLICT DO NOTHING;""")
    collectionid = db.execute(f"SELECT id FROM Collections WHERE name = '{collection['name']}';").fetchone()[0]
    for trackid in collection['trackids']:
        db.execute(f"""INSERT INTO CollectionsTracks (trackid, collectionid) 
                   VALUES ('{trackid}', '{collectionid}') 
                   ON CONFLICT DO NOTHING;""")

db.close()
