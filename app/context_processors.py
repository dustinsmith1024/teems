from django.conf import settings # import the settings file
import datetime

def mode(context):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'MODE': settings.MODE}


def time_add(minutes, start_time):
    # add minutes to time
    #fulldate = datetime.datetime(1,1,1,tm.hour,tm.minute,tm.second)
    print minutes
    print start_time
    new_time = start_time + datetime.timedelta(0, 0, minutes)
    return new_time.time()

    #        a = datetime.datetime.now().time()
    #        b = addSecs (a,300)
    #        print a
    #        print b
