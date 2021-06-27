import create_db
import passwords
import time

db_name = 'music'
db_password = passwords.db_password
db = create_db.open_db(db_name, db_password)

print('_________________')
selected_year = 2018
print(f'Albums released in {selected_year}:')
albums_released_2018 = db.execute(f"""SELECT name, year FROM Albums WHERE year = '{selected_year}'""").fetchall()
for album in albums_released_2018:
    print(f'Album: {album[0]}, year: {album[1]}')

print('_________________')
print('Longest track:')
longest_track = db.execute("""SELECT name, continuity FROM Tracks ORDER BY continuity DESC""").fetchone()
print(f'Track: {longest_track[0]}, continuity: {time.strftime("%M:%S", time.gmtime(longest_track[1]))}')

print('_________________')
min_time = 210
print(f'Tracks longer than  {time.strftime("%M:%S", time.gmtime(min_time))}:')
tracks_longer_than_min_time = db.execute(f"""SELECT name FROM Tracks WHERE continuity > {min_time} ORDER BY continuity DESC """).fetchall()
for track in tracks_longer_than_min_time:
    print(track[0])

print('_________________')
min_year = 2018
max_year = 2020
print(f'Collections released between {min_year} and {max_year}:')
collections_between_years = db.execute(f"""SELECT name FROM Collections WHERE year BETWEEN '{min_year}' and '{max_year}'""").fetchall()
for collection in collections_between_years:
    print(collection[0])

print('_________________')
print(f'Single word named artists:')
single_word_artists = db.execute(f"""SELECT name FROM Artists WHERE name NOT LIKE '%% %%'""").fetchall()
for artist in single_word_artists:
    print(artist[0])

print('_________________')
string_to_find = 'My'
print(f'Tracks containing {string_to_find}:')
tracks_with_string = db.execute(f"""SELECT name FROM Tracks WHERE name LIKE '%%{string_to_find}%%'""").fetchall()
for track in tracks_with_string:
    print(track[0])
