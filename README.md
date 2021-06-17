## Решение домашнего задания к лекции «Введение в БД. Типы БД»
  
    
Схема сайта:  
  
![](https://github.com/headsoft-mikhail/netology_db_1/blob/main/Netology_DB_1.png "Схема сайта")

1. Список исполнителей хранится в таблице Artists
1. Чтобы получить список альбомов исполнителя, нужно пройти по таблице альбомов (Albums) и выбрать нужный ArtistId
1. Чтобы получить список треков, входящих в альбом, нужно пройти по таблице треков (Tracks) и выбрать нужный AlbumId
1. Список жанров хранится в таблице Genres. 
1. Чтобы получить список исполнителей в определеннном жанре, нужно пройти по таблице Artists и выбрать тех, у кого соответствующий GenreId
