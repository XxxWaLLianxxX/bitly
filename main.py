import argparse
import os
import requests

from urllib.parse import urlparse
from dotenv import load_dotenv


def get_shorten_link(token, url):
    bitly = "https://api-ssl.bitly.com/v4/shorten"
    headers = {"Authorization": token}
    payload = {"long_url": url}
    response = requests.post(bitly, headers=headers, json=payload)
    response.raise_for_status()
    response_info = response.json()
    bitlink = response_info['id']
    return bitlink


def count_clicks(token, bitlink):
    parsed_bitlink = urlparse(bitlink)
    bitlink = parsed_bitlink.netloc + parsed_bitlink.path
    bitly = "https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary".format(
        bitlink=bitlink)
    headers = {"Authorization": token}
    response = requests.get(bitly, headers=headers)
    response.raise_for_status()
    response_dict = response.json()
    clicks_count = response_dict['total_clicks']
    return clicks_count


def get_cmd_args():
    parser = argparse.ArgumentParser(description="Программа сокращает или подсчитывает клики по ссылке")
    parser.add_argument(
        "url",
        help="Ссылка",
    )
    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')

    args = get_cmd_args()
    url = args.url

    try:
        try:
            clicks_count = count_clicks(token, url)
            print(clicks_count)
        except requests.exceptions.HTTPError:
            bitlink = get_shorten_link(token, url)
            print(bitlink)
    except requests.exceptions.HTTPError:
        print("Неверная ссылка")


if __name__ == '__main__':
    main()
