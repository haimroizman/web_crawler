import re

import data_sources.tor_data_source

import utility.string_utils


class Paste(object):
    def __init__(self, title, author, publish_date, content):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.content = content

    def print_paste(self):
        print('title: {}'.format(self.title))
        print('author: {}'.format(self.author))
        print('publish date: {}'.format(self.publish_date))
        print('content: {}'.format(self.content))
        print('=' * 20)

    @staticmethod
    async def from_partial_paste_html_elements(title_element, author_date_element, content_url_element):
        title = utility.string_utils.get_strip(str(title_element.text_content()))
        (author, publish_date) = get_author_and_publish_time(author_date_element.text_content())
        content_url = utility.string_utils.get_strip(content_url_element.get("href"))

        content_response = await data_sources.tor_data_source.load_paste_content(content_url)

        content = get_content(content_response.text)

        return Paste(title,
                     author,
                     utility.string_utils.get_date(publish_date, 'D MMM YYYY, HH:mm:ss'),
                     content)


def get_content(content_html):
    content_html = utility.string_utils.get_clean_html(content_html)

    content_lines = content_html.xpath("//div[@class='well well-sm well-white pre']/div/ol/li/div")

    content_string = ''

    for content_line in content_lines:
        strip_content = str(content_line.text_content()).strip(' \t\n\r')

        strip_content = re.sub(r'[^\x00-\x7F]+', '', strip_content)

        if not strip_content:
            continue

        content_string += strip_content + ' '

    whitespace_pattern = re.compile(r'\s+')

    return re.sub(whitespace_pattern, ' ', content_string.strip(' \t\n\r'))


def get_author_and_publish_time(x):
    return x.strip().replace('Posted by ', '').split('at')
