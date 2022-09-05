from webpage_scraps.country import get_usernames_for_country
from utilities.database.postgres.upsert._upsert import upsert_data
from utilities.files import read_json_file
from utilities.database.bigquery.load.insert import load_data
from datetime import datetime, timezone
from typing import Dict
import csv
import logging
import uuid


logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO)
logger = logging.getLogger('bgg-exp')


def write_usernames_to_file(country_name) -> None:
    usernames = get_usernames_for_country(country_name)
    with open('usernames.csv', 'a', newline='') as csvfile:
        fieldnames = ['username', 'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for username_chunk in usernames:
            for username in username_chunk:
                writer.writerow({'username': username, 'country': country_name})


def insert_users_to_db(credentials_path, usernames, country_name):
    data = [{'username': username, 'country': country_name} for username in usernames]
    logger.info(f"inserting chunk to database")
    upsert_data(data, 'scraps', 'users', credentials_path)
    logger.info("insertion successful")


def write_usernames_to_db(country_name: str, credentials_path: str, starting_page: int = 1, min_wait=1, max_wait=2) -> None:
    run_id = str(uuid.uuid4())
    usernames = get_usernames_for_country(country_name, starting_page=starting_page, min_wait=min_wait, max_wait=max_wait)
    for username_chunk in usernames:
        formatted_data = format_data_for_bigquery(username_chunk, run_id, country_name)
        load_data(credentials_path, 'raw', 'scrapped_users', formatted_data)
        # insert_users_to_db(credentials, username_chunk, country_name)


def format_data_for_bigquery(data: list, run_id: str, country: str):
    return [
        {
            'run_id': run_id,
            'username': value,
            'country': country,
            'inserted_at': datetime.now(timezone.utc),
            'updated_at': datetime.now(timezone.utc)
        }
        for value in data
    ]


write_usernames_to_db('Chile', './bgg-experiments-419cf3c9e4cf.json', starting_page=1, min_wait=0.1, max_wait=0.5)
