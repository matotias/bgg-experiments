from string import Template


def construct_country_url(country: str, url: str) -> str:
    return Template(url).safe_substitute({'country': country})
