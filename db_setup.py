import mysql.connector 
from mysql.connector import Error #To catch and handle mysql exceptions
from dotenv import load_dotenv #For loading the environment variables
import os # We use this whenever we are working with env and file paths


load_dotenv()


host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

create_table_query = """
    CREATE TABLE IF NOT EXISTS spotify_tracks (
        track_id VARCHAR(100) PRIMARY KEY,
        artists TEXT,
        album_name TEXT,
        track_name TEXT,
        popularity INT,
        duration_ms INT,
        explicit BOOLEAN,
        danceability FLOAT,
        energy FLOAT,
        `key` INT,
        loudness FLOAT,
        mode INT,
        speechiness FLOAT,
        acousticness FLOAT,
        instrumentalness FLOAT,
        liveness FLOAT,
        valence FLOAT,
        tempo FLOAT,
        time_signature INT,
        track_genre VARCHAR(100)
    );
    """


try:
    #connection to mysql
    connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password
    )

    cursor = connection.cursor() #Conneced to mysql

    #Creating a database 
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    print(f"database {database} is successfully created")

    connection.database = database # Connection to specified database
    cursor.execute(create_table_query)
    print(f"table spotify_tracks created successfully")

except Error as e:
    print(f" error {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print(f"mysql connection is closed")


