import data_sources.paste_repository
import tor_io.paste_stronghold_downloader


class WebCrawler(object):
    def __init__(self, last_date):
        self.last_date = last_date

    def crawl_url(self):
        print('Downloading stronghold pastes...')

        paste_stronghold_downloader = tor_io.paste_stronghold_downloader.PasteStrongholdDownloader()

        paste_collection = paste_stronghold_downloader.download_pastes()

        with data_sources.paste_repository.PasteRepository() as past_repository:
            print('Saving pastes to database...')

            past_repository.ensure_table()

            for paste in paste_collection.pastes:
                if paste.publish_date < self.last_date:
                    break

                past_repository.insert_paste(paste)
