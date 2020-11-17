from typing import List, Dict, Any
from boardgamegeek.objects.games import BoardGame


def get_categories(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.data()['id'],
            'category': category
        }
        for category in board_game.data()['categories']
    ]


def get_player_suggestions(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.id,
            'player_count': player_suggestion.data()['player_count'],
            'best': player_suggestion.data()['best'],
            'recommended': player_suggestion.data()['recommended'],
            'not_recommended': player_suggestion.data()['not_recommended']
        }
        for player_suggestion in board_game.player_suggestions
    ]


def get_publishers(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.id,
            'publisher': publisher
        }
        for publisher in board_game.publishers
    ]


def get_mechanics(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.id,
            'mechanic': mechanic
        }
        for mechanic in board_game.mechanics
    ]


def get_designers(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.id,
            'designer': designer
        }
        for designer in board_game.designers
    ]


def get_artists(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.id,
            'artist': artist
        }
        for artist in board_game.artists
    ]


def get_families(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.id,
            'family': family
        }
        for family in board_game.families
    ]


def get_ranks(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.id,
            'rank_id': rank.data()['id'],
            'rank_name': rank.data()['name'],
            'rank_friendlyname': rank.data()['friendlyname'],
            'rank': rank.data()['value']
        }
        for rank in board_game.ranks
    ]


def map_board_game(board_game: BoardGame) -> Dict[str, Any]:
    return {
        'id': board_game.id,
        'name': board_game.name,
        'year': board_game.year,
        'accessory': board_game.accessory,
        'bgg_rank': board_game.bgg_rank,
        'boardgame_rank': board_game.boardgame_rank,
        'description': board_game.description,
        'expansion': board_game.expansion,
        'image': board_game.image,
        'min_players': board_game.min_players,
        'max_players': board_game.max_players,
        'max_playing_time': board_game.max_playing_time,
        'min_playing_time': board_game.min_playing_time,
        'playing_time': board_game.playing_time,
        'min_age': board_game.min_age,
        'rating_average': board_game.rating_average,
        'rating_average_weight': board_game.rating_average_weight,
        'rating_bayes_average': board_game.rating_bayes_average,
        'rating_median': board_game.rating_median,
        'rating_num_weights': board_game.rating_num_weights,
        'rating_stddev': board_game.rating_stddev,
        'thumbnail': board_game.thumbnail,
        'users_owned': board_game.users_owned,
        'users_rated': board_game.users_rated,
        'users_trading': board_game.users_trading,
        'users_wanting': board_game.users_wanting,
        'users_wishing': board_game.users_wishing,
        'implementations': board_game.implementations,
        'alternative_names': board_game.alternative_names,
        'versions': board_game.versions,
        'videos': board_game.videos
    }


def get_expands(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': expands.data()['id'],
            'board_game_name': expands.data()['name'],
            'expansion_id': board_game.id,
            'expansion_name': board_game.name
        }
        for expands in board_game.expands
    ]


def get_expansions(board_game: BoardGame) -> List[Dict[str, Any]]:
    return [
        {
            'board_game_id': board_game.id,
            'board_game_name': board_game.name,
            'expansion_id': expansion.data()['id'],
            'expansion_name': expansion.data()['name']
        }
        for expansion in board_game.expansions
    ]
