from webpage_scraps.country import get_usernames_for_country
from utilities.database.postgres.upsert._upsert import upsert_data
from utilities.files import read_json_file
from typing import Dict
import csv
import logging


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


def insert_users_to_db(credentials, usernames, country_name):
    data = [{'username': username, 'country': country_name} for username in usernames]
    logger.info(f"inserting chunk to database")
    upsert_data(data, 'scraps', 'users', credentials)
    logger.info("insertion successful")


def write_usernames_to_db(country_name: str, credentials: Dict[str, str], starting_page: int = 1) -> None:
    usernames = get_usernames_for_country(country_name, starting_page=starting_page)
    logger.info(f'connecting to database {credentials["database"]}')
    logger.info('connection successful')
    for username_chunk in usernames:
        insert_users_to_db(credentials, username_chunk, country_name)


write_usernames_to_db('Chile', read_json_file('./config.json'))
