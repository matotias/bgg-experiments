from __future__ import annotations
from utilities.database.postgres.upsert._upsert import upsert_data
from utilities.database.postgres import extract
from utilities.files import read_json_file
from apiv2.collections import get_collections
from boardgamegeek import BGGClient
import logging


logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO)
logger = logging.getLogger('bgg-exp')
credentials = read_json_file('./config.json')
bgg = BGGClient()
users = extract.using_query(
    credentials,
    '''
select distinct u.*
from boardgamegeek.users u
left join boardgamegeek.collections c on u.id = c.user_id
where u.country in ('Mexico')
and lower(name) ~ '^[k-p].*'
and c.user_id is null
'''
)
data = get_collections(users)

for row in data:
    logging.info(f'uploading data')
    if len(row) > 0:
        upsert_data(row, 'boardgamegeek', 'collections', credentials, excluded_columns=['inserted_at', 'updated_at'])
        logging.info(f'data uploaded')
    else:
        logging.info('user without a collection, skipping load')
