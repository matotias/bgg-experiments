from typing import Dict
from bs4 import BeautifulSoup
import requests


def get_country_soup(url: str, headers: Dict) -> BeautifulSoup:
    response = requests.get(url, headers)
    return BeautifulSoup(response.content, 'html.parser')
