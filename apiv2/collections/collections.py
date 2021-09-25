from boardgamegeek.objects.games import BoardGame
from typing import List, Dict, Generator
from boardgamegeek import BGGClient
from boardgamegeek.exceptions import BGGItemNotFoundError
import logging
import time


def get_collection(username: str) -> BGGClient.collection:
    bgg = BGGClient()
    for n in range(0, 8):
        try:
            return bgg.collection(username)
        except BGGItemNotFoundError as error:
            raise error
        except Exception as error:
            logging.warning(str(error) + ' error received, trying again in ' + str(3**n) + ' seconds')
            time.sleep(3**n)
    logging.error('too many errors, gg')


def get_collections(users: List[Dict[str, str]]) -> Generator:
    for user in users:
        logging.info(f'getting collection for user {user["name"]}')
        try:
            collection = get_collection(user['name'])
            logging.info(f'received {len(collection.items)} boardgames')
            logging.info(f'transforming data to load it to db')
            yield [map_collection_board_game(user, board_game) for board_game in collection]
        except BGGItemNotFoundError:
            logging.info('user not found, skipping')


def map_collection_board_game(user: Dict[str, str], board_game: BoardGame) -> Dict[str, str]:
    return {
        'user_id': user['id'],
        'board_game_id': board_game.id,
        'comment': board_game.comment,
        'for_trade': board_game.for_trade,
        'last_modified': board_game.last_modified,
        'numplays': board_game.numplays,
        'owned': board_game.owned,
        'preordered': board_game.preordered,
        'prev_owned': board_game.prev_owned,
        'rating': board_game.rating,
        'want': board_game.want,
        'want_to_buy': board_game.want_to_buy,
        'want_to_play': board_game.want_to_play,
        'wishlist': board_game.wishlist
    }
