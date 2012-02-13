from django.conf import settings # import the settings file

def mode(context):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'MODE': settings.MODE}
