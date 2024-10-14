import requests
import json
import psycopg2
import logging
import configparser
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

API_URL = config['API']['url']
DATABASE_URL = config['DATABASE']['url']

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        return None

def write_to_db(data):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS quotes
                          (id SERIAL PRIMARY KEY, content TEXT, author TEXT)''')

        cursor.execute("INSERT INTO quotes (content, author) VALUES (%s, %s)", 
                       (data['content'], data['author']))

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        logging.error(f"Database error: {e}")

def main():
    data = fetch_data()
    if data:
        write_to_db(data)

if __name__ == "__main__":
    main()
