PORT = 8000

HTTP_REGEX = r'^https?://'  # http:// or https://
r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
r'(?::\d+)?'  # optional port
r'(?:/?|[/?]\S+)$'

HEADERS = {
    "Accept": "text/html; charset:utf-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
}

REQUEST_TIMEOUT = 20
