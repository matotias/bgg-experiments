from string import Template


def construct_country_url(country: str, url: str, page_number: int = None) -> str:
    return Template(url).safe_substitute({'country': country, 'page_number': page_number})

