import re
import config

url_regex = re.compile(config.HTTP_REGEX, re.IGNORECASE)


def valid_url(url: str) -> bool:
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url
    return url
