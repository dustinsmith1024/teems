import datetime

def add_time(start_time, add_amount):
    fulldate = datetime.datetime(1,1,1,
            start_time.hour,
            start_time.minute,
            start_time.second)
    return (fulldate + datetime.timedelta(minutes=add_amount)).time()


def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i-=1
                break
            else:
                l[i:i+1]=l[i]
        i+=1
    return ltype(l)

