import re
from bs4 import BeautifulSoup


def get_total_pages(soup: BeautifulSoup) -> int:
    return clean_total_pages_value(soup.find_all("a", title="last page")[0].text)


def clean_total_pages_value(value: str) -> int:
    return int(re.findall(r'\d+', value)[0])
