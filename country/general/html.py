from typing import Dict
import requests


def get_country_html(url: str, headers: Dict) -> requests.Response:
    return requests.get(url, headers)
