import pandas as pd
import mysql.connector 
from mysql.connector import Error
from dotenv import load_dotenv
import os 
import time

load_dotenv()# for loading the env variables


host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

df = pd.read_csv(r"D:\spotify\dataset.csv") #loading data into dataframe

df.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')

    # Strip column names
df.columns = df.columns.str.strip()
    
    # Drop duplicates based on unique ID
df.drop_duplicates(subset="track_id", inplace=True)
    
    # Drop rows missing essential fields
df.dropna(subset=["track_id", "track_name"], inplace=True)
    
    # Ensure explicit is boolean
if df["explicit"].dtype != bool:
        df["explicit"] = df["explicit"].astype(bool)
    
    # Replace NaNs with None (MySQL NULL)
df = df.where(pd.notnull(df), None)



try:
    
    start = time.time()
    #establishing mysql connection
    connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )


    cursor = connection.cursor()

    

    insert_query = """
            INSERT INTO spotify_tracks (
                track_id, artists, album_name, track_name,
                popularity, duration_ms, explicit, danceability, energy,
                `key`, loudness, mode, speechiness, acousticness,
                instrumentalness, liveness, valence, tempo,
                time_signature, track_genre
            ) VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s
            );
        """

    # ✅ Step 4: Drop "Unnamed: 0" if it exists
    

    # ✅ Step 5: Convert DataFrame to list of tuples
    data = list(df.itertuples(index=False, name=None))

    print(f"📦 Preparing to insert {len(data)} rows...")



    data = list(df.itertuples(index=False, name=None))

    cursor.executemany(insert_query, data)

    connection.commit()

    end = time.time()

    print(f"inserted: {cursor.rowcount} rows in {round(end-start, 2)} secs")

except Error as e:
    print(f"error {e} occured")
    cursor.close()
    connection.close()
    print("mysql connection is closed")
        
