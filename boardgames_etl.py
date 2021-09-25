from utilities.database.postgres.upsert._upsert import upsert_data
from utilities.lists.dict_lists import deduplicate_dict_list
from utilities.database.postgres import extract
from utilities.files import read_json_file
from utilities.iterables import to_chunks
from apiv2.boardgames import board_game_mapping
from boardgamegeek import BGGClient
import logging


logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.DEBUG)
logger = logging.getLogger('bgg-exp')
credentials = read_json_file('./config.json')
bgg = BGGClient()
games_list = extract.using_query(credentials, 'select distinct board_game_id from boardgamegeek.collections')
ids = [game['board_game_id'] for game in games_list]
ids_chunks = to_chunks(ids, 100)

for chunk in ids_chunks:
    raw_board_games = bgg.game_list(chunk)
    ranks = []
    player_suggestions = []
    categories = []
    artists = []
    designers = []
    families = []
    mechanics = []
    publishers = []
    board_games = []
    expands = []
    expansions = []
    for board_game in raw_board_games:
        ranks.extend(board_game_mapping.get_ranks(board_game))
        player_suggestions.extend(board_game_mapping.get_player_suggestions(board_game))
        categories.extend(board_game_mapping.get_categories(board_game))
        artists.extend(board_game_mapping.get_artists(board_game))
        designers.extend(board_game_mapping.get_designers(board_game))
        families.extend(board_game_mapping.get_families(board_game))
        mechanics.extend(board_game_mapping.get_mechanics(board_game))
        publishers.extend(board_game_mapping.get_publishers(board_game))
        expands.extend(board_game_mapping.get_expands(board_game))
        expansions.extend(board_game_mapping.get_expansions(board_game))
        board_games.append(board_game_mapping.map_board_game(board_game))

    upsert_data(ranks, 'boardgamegeek', 'ranks', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(player_suggestions, 'boardgamegeek', 'player_suggestions', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(categories, 'boardgamegeek', 'categories', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(deduplicate_dict_list(artists), 'boardgamegeek', 'artists', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(deduplicate_dict_list(designers), 'boardgamegeek', 'designers', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(deduplicate_dict_list(families), 'boardgamegeek', 'families', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(deduplicate_dict_list(mechanics), 'boardgamegeek', 'mechanics', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(deduplicate_dict_list(publishers), 'boardgamegeek', 'publishers', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(board_games, 'boardgamegeek', 'board_games', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(deduplicate_dict_list(expands), 'boardgamegeek', 'expansions', credentials, excluded_columns=['inserted_at', 'updated_at'])
    upsert_data(deduplicate_dict_list(expansions), 'boardgamegeek', 'expansions', credentials, excluded_columns=['inserted_at', 'updated_at'])
