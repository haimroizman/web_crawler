import datetime
import time
import pytz
import schedule

import tor_io.web_crawler

import utility.config

if __name__ == '__main__':
    run_interval_hours = utility.config.run_interval_hours
    last_paste_hours_delta = utility.config.last_paste_hours_delta
    last_date = datetime.datetime.now(pytz.utc) - datetime.timedelta(hours=last_paste_hours_delta)

    web_crawler = tor_io.web_crawler.WebCrawler(last_date)

    schedule.every(run_interval_hours).hours.do(web_crawler.crawl_url)

    web_crawler.crawl_url()

    while True:
        schedule.run_pending()
        time.sleep(1)
