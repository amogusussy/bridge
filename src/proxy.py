from bs4 import BeautifulSoup
import requests
import re
import config
import readabilipy


def proxy_url(url: str):
    html = requests.get(
        url=url,
        headers=config.HEADERS,
    )

    if html.status_code != 200:
        return

    proxy_html = readabilipy.simple_json_from_html_string(
        html.text,
        use_readability=True
    )["content"]

    parsed = BeautifulSoup(proxy_html, "lxml")

    for image in parsed.select("img"):
        image["alt"] = f"URL: {image['src']}"
        image["src"] = f"/proxy_image?url={image['src']}"

    proxy_html = str(parsed)

    return proxy_html


def proxy_image(url):
    local_HEADERS = config.HEADERS
    local_HEADERS["accept"] = "image/*"
    image = requests.get(
        url=url,
        headers=local_HEADERS
    ).content

    return image
