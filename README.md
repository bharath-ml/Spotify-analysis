# 🎧 Spotify Data Analysis Dashboard

An interactive Streamlit dashboard that analyzes and visualizes Spotify tracks stored in a MySQL database.

## 🔧 Tech Stack

- Python + Pandas + Seaborn
- MySQL (via MySQL Workbench)
- Streamlit
- Git + GitHub for version control
- dotenv for secure credentials

## 📊 Features

- Load Spotify data and clean it efficiently
- Store clean data in MySQL with proper schema
- Analyze trends: Top 10 Artists, Genre Comparisons
- Visualize insights (e.g., Danceability of Rock vs Pop)
- Streamlit dashboard with real-time plots from SQL queries

## 🚀 Run Locally

```bash
git clone https://github.com/bharath-ml/Spotify-analysis.git
cd Spotify-analysis
pip install -r requirements.txt
streamlit run dashboard.py
