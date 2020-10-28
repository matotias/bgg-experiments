from utilities.files import read_json_file
from .general.url import construct_country_url
from .general.html import get_country_soup
from .data.total_pages import get_total_pages
from .data.usernames import get_usernames
from typing import List, Callable
from time import sleep
from random import randint
import logging


logger = logging.getLogger('bgg-exp')


def get_total_pages_for_country(country_name: str) -> int:
    request_parameters = read_json_file('request_parameters.json')
    url = construct_country_url(country_name, request_parameters['country_url'])
    country_soup = get_country_soup(url, request_parameters.get('headers', {}))
    return get_total_pages(country_soup)


# FIXME: ALLOW IT TO DO SOMETHING IN BETWEEN CYCLES
# TODO: maybe add an optional callable? print after each cycle and pick it up with singer?
def get_usernames_for_country(country_name: str) -> List:
    request_parameters = read_json_file('request_parameters.json')
    total_pages = get_total_pages_for_country(country_name)
    logger.info(f'found {total_pages} pages')
    return [
        username
        for page in range(1, total_pages + 1)
        for username in slow_get_usernames_in_page(page, country_name, request_parameters)
    ]


def slow_get_usernames_in_page(
        page: int,
        country_name: str,
        request_parameters,
        min_wait: int = 5,
        max_wait: int = 10
) -> List[str]:
    usernames = get_usernames_in_page(country_name, page, request_parameters)
    logger.info(f'received {len(usernames)} usernames')
    wait = randint(min_wait, max_wait)
    logger.info(f'waiting {wait} seconds before continuing')
    sleep(wait)
    return usernames


def get_usernames_in_page(country_name: str, page: int, request_parameters: dict) -> List[str]:
    logger.info(f'getting users of page {page}')
    url = construct_country_url(country_name, request_parameters['country_url_page'], page_number=page)
    logger.info(f'getting users from url {url}')
    country_soup = get_country_soup(url, request_parameters.get('headers', {}))
    return get_usernames(country_soup)


