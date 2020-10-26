from typing import Dict
from bs4 import BeautifulSoup
import requests


def get_country_html(url: str, headers: Dict) -> BeautifulSoup:
    response = requests.get(url, headers)
    return get_country_soup(response)


def get_country_soup(response: requests.Response) -> BeautifulSoup:
    return BeautifulSoup(response.content, 'html.parser')
