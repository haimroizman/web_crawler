import re
import arrow
import lxml.html
import lxml.html.clean


def get_strip(x):
    return re.sub('[\t\n\r]', '', x)


def get_date(date_string, pattern):
    return arrow.get(date_string, pattern).datetime


def get_clean_html(html):
    return lxml.html.fromstring(
        lxml.html.clean.Cleaner(style=True, links=True, comments=True, page_structure=False).clean_html(html))
