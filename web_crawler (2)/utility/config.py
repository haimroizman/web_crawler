import configparser

config = configparser.ConfigParser()
config.read('config.ini')

web_crawler_url = config.get('ProjectSection', 'web_crawler_url')
run_interval_hours = config.getint('ProjectSection', 'run_interval_hours')
last_paste_hours_delta = config.getint('ProjectSection', 'last_paste_hours_delta')
tor_proxy_http = config.get('ProjectSection', 'tor_proxy_http')
tor_proxy_https = config.get('ProjectSection', 'tor_proxy_https')
max_workers = config.getint('ProjectSection', 'max_workers')
onion_database_path = config.get('ProjectSection', 'onion_database_path')
