from django import template

register = template.Library()

@register.filter
def prefix(value, arg):
    return "{0} {1}".format(arg, value)

@register.filter
def prefix_or_none(value, arg):
    if value:
        return "{0} {1}".format(arg, value)
    return ""
