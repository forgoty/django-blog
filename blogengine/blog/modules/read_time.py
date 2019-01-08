import datetime
import re
import math

from django.utils.html import strip_tags


AVERAGE_WPM_READ_SPEED = 200.0


def _count_words(html_string) -> int:
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    return len(matching_words)


def get_read_time(html_string) -> str:
    count = _count_words(html_string)
    read_time_min = math.ceil(count/AVERAGE_WPM_READ_SPEED)
    read_time = str(datetime.timedelta(minutes=read_time_min))
    return read_time