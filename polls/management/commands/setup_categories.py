from abc import ABC
from django.core.management.base import BaseCommand
from polls.models import Category

class Command(BaseCommand, ABC):
    help = 'Setup categories'
    categories = [
        {
            'name': 'Tecnologia',
            'classname': 'fas fa-desktop'
        },
        {
            'name': 'Meio ambiente',
            'classname': 'fas fa-tree'
        },
        {
            'name': 'Economia',
            'classname': 'fas fa-money-bill-wave'
        },
        {
            'name': 'Cinema',
            'classname': 'fas fa-film'
        },
        {
            'name': 'Ciência',
            'classname': 'fas fa-bug'
        },
        {
            'name': 'Artes',
            'classname': 'fas fa-paint-brush'
        },
        {
            'name': 'Idiomas',
            'classname': 'fas fa-language'
        },
        {
            'name': 'História',
            'classname': 'fas fa-monument'
        },
        {
            'name': 'Política',
            'classname': 'fas fa-landmark'
        },
        {
            'name': 'Musica',
            'classname': 'fas fa-music'
        },
        {
            'name': 'Religião',
            'classname': 'fas fa-star-of-david'
        },
        {
            'name': 'Saúde',
            'classname': 'fas fa-heartbeat'
        },
        {
            'name': 'Filosofia/Sociologia',
            'classname': 'fas fa-book-reader'
        }
    ]
    
    def handle(self, *args, **kwargs):
        for category in self.categories:
            category = Category.objects.create(name=category['name'], classname_fontawesome=category['classname'])
            category.save()
            
        self.stdout.write('Done!')