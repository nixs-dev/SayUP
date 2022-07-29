from django import template
from polls.models import User
from base64 import b64encode
import json


register = template.Library()


@register.filter(name='dict_item')
def dict_item(dict_, key):
    return dict_.get(key)


@register.filter(name='list_item')
def list_item(list_, index):
    return list_[index]


@register.filter(name='get_profile_photo_src')
def get_profile_photo_src(user):
    src = ''
    gender = user.gender if isinstance(user, User) else user['gender']
    photo = user.photo if isinstance(user, User) else user['photo']
    
    print(type(gender))
    
    if photo is None:
        if gender == True:
        	src = '/static/imgs/default_male_icon.png'
        elif gender == False:
        	src = '/static/imgs/default_female_icon.png'
        else:
            src = '/static/imgs/default_neutral_icon.png'
    else:
        src = f'data:image;base64,{ binary_to_b64(photo) }'
    
    return src


@register.filter(name='binary_to_b64')
def binary_to_b64(binary):
    return b64encode(binary).decode('utf-8')


@register.filter(name='range_list')
def range_list(start, end):
    return range(start, end)


@register.filter(name='get_attribute')
def get_attribute(obj, var):
    return getattr(obj, var)


@register.filter(name='to_str')
def to_str(integer):
    return str(integer)