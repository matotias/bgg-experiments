import json
import logging
import time
from typing import Dict, Any, List
from boardgamegeek.objects.user import User
from boardgamegeek import BGGClient


def get_user(username: str) -> User:
    logging.info(f'fetching data from user {username} from bgg')
    bgg = BGGClient()
    for n in range(0, 8):
        try:
            user_data = bgg.user(username)
            logging.info('user data received')
            return user_data
        except Exception as error:
            logging.warning(str(error) + ' error received, trying again in ' + str(3**n) + ' seconds')
            time.sleep(3**n)
    logging.error('too many errors, gg')


def get_users(usernames: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    return [map_user(get_user(username['username'])) for username in usernames]


def map_user(user: User) -> Dict[str, Any]:
    return {
        'id': user.id,
        'name': user.name,
        'firstname': user.firstname,
        'lastname': user.lastname,
        'country': user.country,
        'avatar': user.avatar,
        'buddies': [json.dumps({'id': buddy.id, 'name': buddy.name}) for buddy in user.buddies],
        'guilds': [json.dumps({'id': guild.id, 'name': guild.name}) for guild in user.guilds],
        'homepage': user.homepage,
        'hot10': [json.dumps({'id': hot.id, 'name': hot.name}) for hot in user.hot10],
        'last_login': user.last_login
    }
