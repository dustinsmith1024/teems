from django import template
import datetime

register = template.Library()

@register.filter
def prefix(value, arg):
    return "{0} {1}".format(arg, value)

@register.filter
def prefix_or_none(value, arg):
    if value:
        return "{0} {1}".format(arg, value)
    return ""

@register.filter
def add_time(minutes, start_time):
    """ add minutes to time
    Is not really useful because I need to change a bunch but
    leaving in here just in case"""
    fulldate = datetime.datetime(1,1,1,
            start_time.hour,start_time.minute,
            start_time.second)
    new_time = fulldate + datetime.timedelta(minutes=minutes)
    return new_time.time()
