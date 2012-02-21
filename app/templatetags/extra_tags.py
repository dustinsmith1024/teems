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

@register.filter(name='add_time')
def add_time(minutes, start_time):
    # add minutes to tim
    #fulldate = datetime.datetime(1,1,1,tm.hour,tm.minute,tm.second)
    print minutes
    print start_time
    print datetime.datetime
    new_time = start_time + datetime.timedelta(0, 0, minutes)
    return new_time.strftime()

#        a = datetime.datetime.now().time()
#        b = addSecs (a,300)
#        print a
#        print b

