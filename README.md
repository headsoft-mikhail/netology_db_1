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
	Name VARCHAR(80) NOT NULL,
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
	Continuity INTEGER NOT NULL CHECK (Continuity > 0)
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

[Ссылка на файл с кодом](https://github.com/headsoft-mikhail/netology_db_1/blob/main/create_db_code.txt "create_db_code_updated.txt")
____ 
