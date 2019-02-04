import asyncio

import objects.paste
import utility.string_utils
import data_sources.tor_data_source


class PasteCollection(object):
    def __init__(self, pastes):
        self.pastes = pastes

    @staticmethod
    def from_pastes_url():
        paste_collection_html = data_sources.tor_data_source.load_paste_collection_html()

        return PasteCollection.from_pastes_html(paste_collection_html)

    @classmethod
    def from_pastes_html(cls, html):
        clean_html = utility.string_utils.get_clean_html(html)

        titles = clean_html.xpath("//div[@class='col-sm-5']/h4")
        authors_and_dates = clean_html.xpath("//div[@class='col-sm-6']")
        urls_for_contents = clean_html.xpath("//div[@class='col-sm-7 text-right']/a")

        paste_futures = map(
            lambda tuple: objects.paste.Paste.from_partial_paste_html_elements(tuple[0], tuple[1], tuple[2]),
            zip(titles, authors_and_dates, urls_for_contents))

        event_loop = asyncio.get_event_loop()

        pastes = event_loop.run_until_complete(asyncio.gather(*paste_futures))

        return cls(pastes)
