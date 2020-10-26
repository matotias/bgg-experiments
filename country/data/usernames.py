from bs4 import BeautifulSoup
from typing import List
import re


def get_username_list(country_soup: BeautifulSoup) -> List[BeautifulSoup]:
    return country_soup.find_all(class_='username')


def clean_username_text(user_text: str) -> str:
    return re.findall(r'\((.*)\)', user_text)[0].strip()
