import asyncio
import concurrent.futures

import requests

import utility.config

max_workers = utility.config.max_workers
executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

event_loop = asyncio.get_event_loop()

session = requests.session()
session.proxies = {'http': utility.config.tor_proxy_http, 'https': utility.config.tor_proxy_https}

web_crawler_url = utility.config.web_crawler_url


def load_paste_collection_html():
    return session.get(web_crawler_url).text


async def load_paste_content(content_url):
    return await asyncio.wrap_future(event_loop.run_in_executor(executor, session.get, content_url))
