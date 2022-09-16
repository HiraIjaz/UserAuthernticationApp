from django import template

register = template.Library()


def upper(value):
    value = value[0].upper()+value[1::]
    return value


register.filter('upper', upper)
