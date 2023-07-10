def valid_url(url: str) -> bool:
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url
    return url
