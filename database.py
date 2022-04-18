from numpy import average
import pyodbc as db
import csv

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

def pipeline(cursor: db.Cursor, country: str, type: str, time_period: str, rating: str, duration: str):
    sql = f"SELECT title, listed_in FROM Media WHERE type='{type}'"
    if country:
        sql += f" AND country='{country}'"
    if time_period:
        if time_period == '2000s': 
            sql += f" AND CAST(release_year AS INT) >= 2000 AND CAST(release_year AS INT) < 2020"
        elif time_period == 'new':
            sql += f" AND CAST(release_year AS INT) >= 2020"
        else:
            sql += f" AND CAST(release_year AS INT) < 2000"
    if rating and rating != "adult":
        if rating == "kid":
            if type == "Movie":
                sql += f" AND NOT rating = 'PG-13' AND NOT rating = 'UR' AND NOT rating = 'NR' AND NOT rating = 'R'"
            else:
                sql += f" AND NOT rating = 'TV-MA' AND NOT rating = 'TV-14'"
        if rating == "teenager":
            if type == "Movie":
                sql += f" AND NOT rating = 'UR' AND NOT rating = 'NR' AND NOT rating = 'R'"
            else:
                sql += f" AND NOT rating = 'TV-MA'"
    print(sql)
        

if __name__ == '__main__':
    cursor = init_db()
    # create_media_table(cursor)
    # save_csv_to_db(cursor)
    print(pipeline(cursor, "United States", "TV Show", "2000+", "Teenage", None))
