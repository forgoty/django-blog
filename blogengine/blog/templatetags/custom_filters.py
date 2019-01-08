import datetime
import math

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='to_minutes')
@stringfilter
def to_minutes(time_str):
    t = datetime.datetime.strptime(time_str,"%H:%M:%S")
    time = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    seconds = time.total_seconds()

    return math.ceil(seconds / 60)


if __name__ == '__main__':
    print(to_minutes('00:00:15'))