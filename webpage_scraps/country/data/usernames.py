from bs4 import BeautifulSoup
from typing import List
import re


def get_username_list(country_soup: BeautifulSoup) -> List[BeautifulSoup]:
    return country_soup.find_all(class_='username')


def clean_username_text(user_text: str) -> str:
    return re.findall(r'\((.*)\)', user_text)[0].strip()


def get_usernames(country_soup: BeautifulSoup) -> List[str]:
    raw_usernames = get_username_list(country_soup)
    return [
        clean_username_text(raw_username.text)
        for raw_username in raw_usernames
    ]
