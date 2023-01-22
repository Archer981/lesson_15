# JOIN из трех таблиц
#
#  JOIN также возможно использовать для трех и более таблиц.
#  Давайте посмотрим в каких жанрах работают артисты.
#  Выведите две колонки в одной из которых будет содержаться имя артиста(name), а в другой жанр(genre).
#  Ознакомится со схемой базы данных можно в файле db_schema.png
#  Подсказка: После первого JOIN аналогичным образом можно
#  использовать такую конструкцию и для других таблиц
#
#
#
import sqlite3
import prettytable

con = sqlite3.connect("../music.db")
cur = con.cursor()
query = """select artists.name as name, genres.name as genre from artists
        join albums on artists.id = albums.artist_id
        join tracks on albums.id = tracks.album_id
        join genres on tracks.genre_id = genres.id
        group by artists.name, genres.name
"""
sqlite_query = query  # TODO составьте JOIN запрос здесь


# Не удаляйте код ниже, он используется
# для вывода заголовков созданной таблицы
table = cur.execute(sqlite_query)
mytable = prettytable.from_db_cursor(table)
mytable.max_width = 30

if __name__ == "__main__":
    print(mytable)
