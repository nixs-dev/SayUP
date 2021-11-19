from django import template

register = template.Library()


@register.filter(name='dict_item')
def dict_item(dict_, key):
    return dict_.get(key)


@register.filter(name='list_item')
def list_item(list_, index):
    return list_[index]
