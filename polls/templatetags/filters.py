from django import template
from base64 import b64encode

register = template.Library()

@register.filter(name='dict_item')
def dict_item(dict_, key):
    return dict_.get(key)

@register.filter(name='list_item')
def list_item(list_, index):
    return list_[index]

@register.filter(name='binary_to_b64')
def binary_to_b64(binary):
    return b64encode(binary).decode('utf-8')