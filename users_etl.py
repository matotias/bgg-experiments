from __future__ import annotations
from utilities.database.postgres.upsert._upsert import upsert_data
from utilities.database.postgres import extract
from utilities.files import read_json_file
from utilities.iterables import to_chunks
from apiv2.users.users import get_users
from boardgamegeek import BGGClient
import logging


logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.DEBUG)
logger = logging.getLogger('bgg-exp')
credentials = read_json_file('./config.json')
usernames_query = "select username from scraps.users where country='Peru'"
usernames = extract.using_query(credentials, usernames_query)
username_chunks = to_chunks(usernames, 100)
bgg = BGGClient()
for username_chunk in username_chunks:
    users = get_users(username_chunk)
    upsert_data(users, 'boardgamegeek', 'users', credentials)
