## Решение домашнего задания к лекции «Введение в БД. Типы БД»
  
    
Схема сайта:  
  
![](https://github.com/headsoft-mikhail/netology_db_1/blob/main/Netology_DB_1.png "Схема сайта")

1. Список исполнителей хранится в таблице Artists
1. Чтобы получить список альбомов исполнителя, нужно пройти по таблице альбомов (Albums) и выбрать нужный ArtistId
1. Чтобы получить список треков, входящих в альбом, нужно пройти по таблице треков (Tracks) и выбрать нужный AlbumId
1. Список жанров хранится в таблице Genres. 
1. Чтобы получить список исполнителей в определеннном жанре, нужно пройти по таблице Artists и выбрать тех, у кого соответствующий GenreId
  
____   
## Решение домашнего задания к лекции «Работа с PostgreSQL. Создание БД»
### Код для создания описанной выше структуры:
```SQL
CREATE DATABASE music WITH OWNER = postgres;

\c music;

CREATE TABLE IF NOT EXISTS Tracks (
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(80) NOT NULL,
	Continuity TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS Artists (
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Albums (	
	Id SERIAL PRIMARY KEY,
	ArtistId INTEGER REFERENCES Artists,
	Name VARCHAR(80) NOT NULL,
	Year INTEGER CHECK (Year > 1950 and Year < 2050)
);

ALTER TABLE Tracks ADD COLUMN AlbumId INTEGER REFERENCES Albums;

CREATE TABLE IF NOT EXISTS Genres (
	Id SERIAL PRIMARY KEY,	
	Name VARCHAR(80) NOT NULL UNIQUE
);

ALTER TABLE Artists ADD COLUMN GenreId INTEGER NOT NULL REFERENCES Genres 
```
[Ссылка на файл с кодом](https://github.com/headsoft-mikhail/netology_db_1/blob/main/create_db_code.txt "create_db_code.txt")
____ 
## Решение домашнего задания к лекции «Проектирование БД. Связи. 3НФ»
  
### Схема сайта обновленная:
![](https://github.com/headsoft-mikhail/netology_db_1/blob/main/Netology_DB_2.png)
  
### Код для создания описанной выше структуры:

```SQL
CREATE DATABASE music WITH OWNER = postgres;

\c music;

CREATE TABLE IF NOT EXISTS Artists (
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Genres (
	Id SERIAL PRIMARY KEY,	
	Name VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS ArtistsGenres (
	ArtistId INTEGER REFERENCES Artists,
	GenreId INTEGER REFERENCES Genres,
	constraint pk_ArtistsGenres PRIMARY KEY (ArtistId, GenreId)
);

CREATE TABLE IF NOT EXISTS Albums (	
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(80) NOT NULL UNIQUE,
	Year INTEGER CHECK (Year > 1950 and Year < 2050)
);

CREATE TABLE IF NOT EXISTS AlbumsArtists (
	ArtistId INTEGER REFERENCES Artists,
	AlbumId INTEGER REFERENCES Albums,
	constraint pk_AlbumsArtists PRIMARY KEY (ArtistId, AlbumId)
);

CREATE TABLE IF NOT EXISTS Tracks (
	Id SERIAL PRIMARY KEY,
	AlbumId INTEGER REFERENCES Albums,
	Name VARCHAR(80) NOT NULL,
	Continuity INTEGER NOT NULL CHECK (Continuity > 0),
	constraint pk_Tracks UNIQUE (Name, AlbumId)
);

CREATE TABLE IF NOT EXISTS Collections (	
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(80) NOT NULL,
	Year INTEGER CHECK (Year > 1950 and Year < 2050)
);

CREATE TABLE IF NOT EXISTS CollectionsTracks (
	CollectionId INTEGER REFERENCES Collections,
	TrackId INTEGER REFERENCES Tracks,
	constraint pk_CollectionsTracks PRIMARY KEY (CollectionId, TrackId)
);
```

[Ссылка на файл с кодом](https://github.com/headsoft-mikhail/netology_db_1/blob/main/create_db_code_updated.txt "create_db_code_updated.txt")
____ 
## Решение домашнего задания к лекции «SELECT-запросы, выборки из одной таблицы»
  
### Создание БД и таблиц:
Ссылка на файл: [create_db.py](https://github.com/headsoft-mikhail/netology_db_1/blob/main/create_db.py "create_db.py")
1. При запуске программа пытается подключиться к БД "music", если такой не существует, тогда подключается к БД "postgres", которая должна существовать по умолчанию, и из этого состояния создаёт БД "music"
1. Команды для создания таблиц и столбцов программа берет прямо из этого репозитория на github из решения ДЗ ([текстового файла](https://github.com/headsoft-mikhail/netology_db_1/blob/main/create_db_code_updated.txt "create_db_code_updated.txt")) для предыдущей лекции (не выполняются первые 2 команды, т.к. они нужны при работе из командной строки)
### Заполнение БД данными:
Ссылка на файл: [fill_db.py](https://github.com/headsoft-mikhail/netology_db_1/blob/main/fill_db.py "fill_db.py")
1. Данные для заполнения загружаются из структуры вида:
```python
data = [
    {'artist': artist_name,
     'genres': [genre],
     'albums': [{'album': album_name,
                 'year': year,
                 'tracks': [{'track': track_name, 'continuity': continuity_sec},
		 	     ...
                            ]
                 }
		 ...
		]
     },
     ...] 
```
1. Для заполнения коллекций, с помощью запроса получаю все id треков и случайным образом выбираю от 5 до 15 треков для новой коллекции.
1. Годы выпуска и названия коллекций заполняются с помощью инкремента. Можно Создавать колекции с помощью SELECT-запросов с фильтрацией по исполнителю или жанру, но этого в задании не было, поэтому коллекции заполняются случайными треками.
### SELECT-запросы согласно инструкциям:
Ссылка на файл: [select_from_db.py](https://github.com/headsoft-mikhail/netology_db_1/blob/main/select_from_db.py "select_from_db.py")
____ 
