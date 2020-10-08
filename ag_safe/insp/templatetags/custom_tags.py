import ast
from django import template
register = template.Library()


@register.filter
def get_string_as_list(value): # Only one argument.
    """Evaluate a string if it contains []"""
    if '[' and ']' in value:
        return eval(value)


@register.filter
def match_value(obj, d):
    show = True
    for abc in obj:
        if abc == d:
            show = True
            return show
        else:
            show = False
    return show


@register.filter
def get_item(dictionary, key):
    print(dictionary)
    return dictionary.get(key)


@register.filter()
def radio_three(dic, name):
    if dic == name:
        return_data = "checked"
    else:
        return_data = ""
    return return_data
