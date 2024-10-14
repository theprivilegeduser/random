import requests
import sqlite3
import configparser
import logging
import sys
from datetime import datetime

# First we import the needed libraries and then we configure the logging. We specify the name HR_daily_motivational_quotes_events.log and how it will be formated and at what level logging it will be. 
logging.basicConfig(filename='HR_daily_motivational_quotes_events.log', 
                    filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def read_config(config_file='config.ini'):
#Reads the configuration file and returns the results - api keys, db path, base url
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        logging.info("Configuration file loaded successfully.")
        api_base_url = config['API']['base_url']
        db_path = config['DB']['database_path']
        return api_base_url, api_key, db_path
    except Exception as e:
        logging.error(f"Failed to read configuration file: {e}")
        sys.exit(1)
#Here we implement error handling - if the config file is not read it will give an error - and if it is then we define what api_key , db_path and api_base_url is because config file was read successfuly.
def fetch_data_from_api(api_base_url):
#Fetches data from the API.
    try:
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        response = requests.get(api_base_url, headers=headers)

        if response.status_code == 200:
            logging.info("Data fetched successfully from API.")
            return response.json()  # Assuming the API returns JSON data
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch data from API: {e}")
        sys.exit(1)
        #If successful - great - if not - we get an error.

def save_to_db(db_path, data):
#Saves the data we just fetched to sql database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS HR_daily_motivational_quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote TEXT NOT NULL,
                author TEXT NOT NULL,
                date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Insert data (assuming the data is a daily quotes)
        for key, value in data.items():
            cursor.execute('''
               INSERT INTO HR_daily_motivational_quotes (quote, author) 
                VALUES (?, ?)
            ''', (item.get('quote'), item.get('author')))

        conn.commit()
        logging.info("Data saved successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        sys.exit(1)
    finally:
        if conn:
            conn.close()
# Again we write the data on a new table if one already doesn't exist - we have defined the database already and we have access from the API - we have error handling - if there is an issue we will see a prompt 
def main():
#Main function to orchestrate the process
    # Read configuration
    api_base_url, api_key, db_path = read_config()

    # Fetch data from API
    data = fetch_data_from_api(api_base_url, api_key)

    # Save data to the database
    save_to_db(db_path, data)

if __name__ == '__main__':
    main()
