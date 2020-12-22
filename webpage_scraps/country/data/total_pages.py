import re
from bs4 import BeautifulSoup


def get_total_pages(soup: BeautifulSoup) -> int:
    total_pages_soup = soup.find_all("a", title="last page")
    if len(total_pages_soup) == 0:
        return 5
    return clean_total_pages_value(soup.find_all("a", title="last page")[0].text)


def clean_total_pages_value(value: str) -> int:
    return int(re.findall(r'\d+', value)[0])
