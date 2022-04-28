from numpy import average
import pyodbc as db
import csv
from myEnums import *

USER = 'db_user'
PASS = 'sqlpassword'
SERVER = 'DESKTOP-CQVQN7N'
DB = 'master'
CONNECTION_STRING = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DB};UID={USER};PWD={PASS}'

def init_db():
    conn = db.connect(CONNECTION_STRING)
    return conn.cursor()

def save_csv_to_db(cursor: db.Cursor):
    with open('netflix_titles.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # Skip header row
        for row in reader:
            if row:
                insert_media(cursor, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

def create_media_table(cursor: db.Cursor):
    sql = """CREATE TABLE Media (
                show_id nvarchar(16),
                type nvarchar(32),
                title nvarchar(255),
                director nvarchar(255),
                cast nvarchar(2048),
                country nvarchar(255),
                date_added nvarchar(64),
                release_year nvarchar(4),
                rating nvarchar(8),
                duration nvarchar(32),
                listed_in nvarchar(2048),
                description nvarchar(2048)
            )"""
    with cursor.execute(sql):
        print("Table Media created")

def insert_media(cursor: db.Cursor, show_id: str, type: str, title: str, director: str, cast: str, country: str, date_added: str, release_year: str, rating: str, duration: str, listed_in: str, description: str):
    sql = 'INSERT INTO Media (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);'
    with cursor.execute(sql, show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description):
        print(f"Inserted row | {show_id}")

def percent_movies(cursor: db.Cursor):
    sql = "SELECT CAST((SELECT COUNT(*) FROM Media WHERE type='Movie') AS FLOAT) / CAST((SELECT COUNT(*) FROM Media) AS FLOAT) * 100 AS PercentMovie"
    with cursor.execute(sql):
        return cursor.fetchval()

def average_movie_runtime(cursor: db.Cursor):
    sql = "SELECT AVG(CAST((SUBSTRING(duration,1,(CHARINDEX(' ',duration + ' ')-1))) AS INT)) FROM Media WHERE type='Movie'"
    with cursor.execute(sql):
        return cursor.fetchval()

def get_keywords_with_media(obj):

    result = []
    for media in obj:
        # TODO get keywords and add to this object

        result.append({
            "title": media[0],
            "director": media[1],
            "cast": [actor.strip() for actor in media[2].split(",")],
            "release_year": media[3],
            "rating": media[4],
            "duration": media[5],
            "genres": [genre.strip() for genre in media[6].split(",")],
            "description": media[7]
        })
    return result

def pipeline(country: str, media_type: Type, time_period: Time_Period, rating: str, duration: Duration, genre: str = None):
    cursor = init_db()
    sql = ""
    media_type = "TV Show" if media_type == Type.TV_SHOW.value else "Movie"
    if genre is not None:
        sql += f"SELECT title, director, cast, release_year, rating, duration, listed_in, description FROM Media WHERE type='{media_type}' AND listed_in LIKE '%{genre}%'"
    else:
        sql += f"SELECT DISTINCT TRIM(cs.Value) AS value FROM Media CROSS APPLY STRING_SPLIT(listed_in, ',') cs WHERE type='{media_type}'"
    if country is not None:
        sql += f" AND country='{country}'"
    if time_period is not None:
        if time_period == Time_Period.TWO_THOUSANDS.value: 
            sql += f" AND CAST(release_year AS INT) >= 2000 AND CAST(release_year AS INT) < 2020"
        elif time_period == Time_Period.NEW.value:
            sql += f" AND CAST(release_year AS INT) >= 2020"
        elif time_period == Time_Period.PRE_TWO_THOUSANDS.value:
            sql += f" AND CAST(release_year AS INT) < 2000"
    if rating is not None and rating != Rating.ADULT.value:
        if rating == Rating.KID.value:
            if media_type == "Movie":
                sql += f" AND NOT rating = 'PG-13' AND NOT rating = 'UR' AND NOT rating = 'NR' AND NOT rating = 'R'"
            else:
                sql += f" AND NOT rating = 'TV-MA' AND NOT rating = 'TV-14'"
        if rating == Rating.TEEN.value:
            if media_type == "Movie":
                sql += f" AND NOT rating = 'UR' AND NOT rating = 'NR' AND NOT rating = 'R'"
            else:
                sql += f" AND NOT rating = 'TV-MA'"
    if duration is not None:
        if media_type == Type.TV_SHOW.value:
            if duration == Duration.ONE_OR_TWO_SEASONS.value:
                sql += f" AND CAST(SUBSTRING(duration,1,(CHARINDEX(' ',duration + ' ')-1)) AS INT) < 3"
            elif duration == Duration.THREE_OR_MORE_SEASONS.value:
                sql += f" AND CAST(SUBSTRING(duration,1,(CHARINDEX(' ',duration + ' ')-1)) AS INT) >= 3"
        elif media_type == Type.MOVIE.value:
            if duration == Duration.LESS_THAN_60_MIN.value:
                sql += f" AND CAST(SUBSTRING(duration,1,(CHARINDEX(' ',duration + ' ')-1)) AS INT) < 60"
            elif duration == Duration.HOUR_TO_90_MIN.value:
                sql += f" AND CAST(SUBSTRING(duration,1,(CHARINDEX(' ',duration + ' ')-1)) AS INT) > 60"
            elif duration == Duration.MORE_THAN_90_MIN.value:
                sql += f" AND CAST(SUBSTRING(duration,1,(CHARINDEX(' ',duration + ' ')-1)) AS INT) > 90"
    if not genre:
        sql += f" ORDER BY value ASC"
    try:
        with cursor.execute(sql):
            result = [list(row) for row in cursor.fetchall()]
    except db.Error as err:
        return {"error": err}
    finally:
        cursor.close()
    if genre:
        return get_keywords_with_media(result)
    else:
        return result

if __name__ == '__main__':
    # create_media_table(cursor)
    # save_csv_to_db(cursor)
    result = pipeline("United States", Type.TV_SHOW, Time_Period.NEW, Rating.ADULT, Duration.THREE_OR_MORE_SEASONS, 'Docuseries')
    print(result)
