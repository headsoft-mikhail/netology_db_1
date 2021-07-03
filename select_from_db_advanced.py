import create_db
import passwords
import time

db_name = 'music'
db_password = passwords.db_password
db = create_db.open_db(db_name, db_password)

print('_________________')
# количество исполнителей в каждом жанре
print(f'Artists count in each genre:')
artists_count_by_genre = db.execute(f"""SELECT genres.name, COUNT(*) FROM genres
                                        JOIN artistsgenres ON artistsgenres.genreid = genres.id
                                        JOIN artists ON artistsgenres.artistid = artists.id
                                        GROUP BY genres.name;""").fetchall()
for item in artists_count_by_genre:
    print(f'{item[0]}: {item[1]}')

print('_________________')
# количество треков, вошедших в альбомы XXXX-XXXX годов
start_year = 2002
stop_year = 2003
tracks_at_years_count = db.execute(f"""SELECT COUNT(*) FROM tracks
                                       JOIN albums ON albums.id = tracks.albumid
                                       WHERE albums.year BETWEEN {start_year} AND {stop_year};""").fetchall()[0][0]
print(f'{tracks_at_years_count} tracks released between {start_year} and {stop_year} years')

print('_________________')
# средняя продолжительность треков по каждому альбому
track_cont_by_album = db.execute(f"""SELECT albums.name, AVG(tracks.continuity) FROM tracks
                                     JOIN albums ON albums.id = tracks.albumid
                                     GROUP BY albums.id
                                     ORDER BY AVG(tracks.continuity);""").fetchall()
for item in track_cont_by_album:
    print(f"""Average track continuity in album "{item[0]}"
              is {time.strftime("%M:%S", time.gmtime(int(item[1])))} ({"%.2f" % item[1]})""")

print('_________________')
# все исполнители, которые не выпустили альбомы в XXXX году
year = 2000
artists_with_no_albums_at_year = db.execute(f"""SELECT artists.name FROM artists
                                                LEFT JOIN
                                                    (SELECT DISTINCT artists.id, artists.name FROM artists
                                                    JOIN albumsartists ON albumsartists.artistid = artists.id
                                                    JOIN albums ON albums.id = albumsartists.albumid
                                                    WHERE albums.year = {year})
                                                    AS artists2000
                                                ON artists.id = artists2000.id
                                                WHERE artists2000.id IS NULL;""").fetchall()
print(f'Artists that have no releases at {year} year')
for item in artists_with_no_albums_at_year:
    print(item[0])

print('_________________')
# названия сборников, в которых присутствует конкретный исполнитель
artist = 'Disturbed'
collections_with_artist = db.execute(f"""SELECT DISTINCT collections.name FROM collections
                                         JOIN collectionstracks ON collectionstracks.collectionid = collections.id
                                         JOIN tracks ON tracks.id = collectionstracks.trackid
                                         JOIN albums ON tracks.albumid = albums.id
                                         JOIN albumsartists ON albums.id = albumsartists.albumid
                                         JOIN artists ON artists.id = albumsartists.artistid
                                         WHERE artists.id = (SELECT id FROM artists
                                                               WHERE name = '{artist}');""").fetchall()
print(f'Songs of {artist} are included to collections:')
for item in collections_with_artist:
    print(item[0])

print('_________________')
# название альбомов, в которых присутствуют исполнители более 1 жанра
genres_count = 1
albums_with_count_of_genres = \
    db.execute(f"""SELECT DISTINCT albums.name FROM albums
                   JOIN albumsartists ON albums.id = albumsartists.albumid
                   JOIN (SELECT id FROM
                            (SELECT a.id, COUNT(genres.id) AS genrescount FROM artists AS a
                             JOIN artistsgenres ON artistsgenres.artistid = a.id
                             JOIN genres ON artistsgenres.genreid = genres.id
                             GROUP BY a.id
                             ) AS artistsgenrescount
                        WHERE genrescount > {genres_count}
                        ) AS ga ON albumsartists.artistid = ga.id;""").fetchall()
print(f'Albums with participation of artist in more than {genres_count} genre(s):')
for item in albums_with_count_of_genres:
    print(item[0])

print('_________________')
# наименование треков, которые не входят в сборники;
not_at_collections = db.execute(f"""SELECT tracks.id, tracks.name from tracks
                                    LEFT JOIN (SELECT tracks.id, tracks.name FROM tracks
                                               JOIN collectionstracks ON collectionstracks.trackid = tracks.id
                                               JOIN collections ON collections.id = collectionstracks.collectionid
                                               GROUP BY tracks.id
                                               ) AS not_in_collection ON tracks.id = not_in_collection.id
                                    WHERE not_in_collection.id IS NULL;""").fetchall()
print(f'Tracks not included to collections:')
for item in not_at_collections:
    print(f'{item[0]}\t{item[1]}')

print('_________________')
# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
shortest_track_artist = db.execute(f"""SELECT artists.name, st.name, st.continuity FROM
                                           (SELECT id, name, albumid, continuity FROM tracks
                                            WHERE continuity = (SELECT MIN(tracks.continuity) FROM tracks)) AS st
                                       JOIN albums ON albums.id = st.albumid
                                       JOIN albumsartists ON albumsartists.albumid = albums.id
                                       JOIN artists ON artists.id = albumsartists.artistid;""").fetchall()
for item in shortest_track_artist:
    print(f'Shortest track is {item[0]} - {item[1]}, {time.strftime("%M:%S", time.gmtime(item[2]))}')

print('_________________')
# название альбомов, содержащих наименьшее количество треков
albums_tracks_count = \
    db.execute(f"""WITH tc AS 
                        (SELECT albums.name, COUNT(*) as count FROM albums
                        JOIN tracks ON tracks.albumid = albums.id
                        GROUP BY albums.id)
                   SELECT tc.name, tc.count FROM tc
                   WHERE tc.count = (SELECT MIN(count) FROM tc);""").fetchall()
print('Albums with the least number of tracks: ')
for item in albums_tracks_count:
 print(f'{item[0]} ({item[1]})')
