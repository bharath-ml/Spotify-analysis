# streamlit_app.py

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Streamlit layout
st.set_page_config(page_title="Spotify Dashboard", layout="wide")
st.title("🎵 Spotify Data Dashboard")
st.markdown("Explore trends in music 🎶 — powered by MySQL + Seaborn")

# 📡 Function to run SQL and return DataFrame
def run_query(query):
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    df = pd.read_sql(query, con=conn)
    conn.close()
    return df


# 🎯 Top 10 Artists by Popularity
st.subheader("🔥 Top 10 Artists by Average Popularity")

query_top_artists = """
SELECT 
    artists,
    ROUND(AVG(popularity), 2) AS avg_popularity
FROM 
    spotify_tracks
GROUP BY 
    artists
ORDER BY 
    avg_popularity DESC
LIMIT 10;
"""

df_top_artists = run_query(query_top_artists)

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(data=df_top_artists, y="artists", x="avg_popularity", palette="mako", ax=ax1)
ax1.set_title("Top 10 Artists by Average Popularity", fontsize=14)
ax1.set_xlabel("Average Popularity")
ax1.set_ylabel("Artists")
st.pyplot(fig1)


# 💃 Danceability: Rock vs. Pop
st.subheader("💃 Danceability: Rock vs. Pop")

query_danceability = """
SELECT 
    track_genre,
    ROUND(AVG(danceability), 3) AS avg_danceability,
    COUNT(*) AS total_tracks
FROM 
    spotify_tracks
WHERE 
    LOWER(track_genre) IN ('rock', 'pop')
GROUP BY 
    track_genre;
"""

df_dance = run_query(query_danceability)

fig2, ax2 = plt.subplots()
sns.barplot(data=df_dance, x="track_genre", y="avg_danceability", palette="coolwarm", ax=ax2)
ax2.set_title("Average Danceability: Rock vs. Pop", fontsize=14)
ax2.set_ylabel("Danceability")
ax2.set_xlabel("Genre")
st.pyplot(fig2)

# Optional: raw data
with st.expander("📄 Show Raw SQL Data"):
    st.dataframe(df_dance)
