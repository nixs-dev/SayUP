from abc import ABC
from django.core.management.base import BaseCommand
from polls.models import User

class Command(BaseCommand, ABC):
    help = 'Seed database'
    users = [
        {
            'gender': 'Masculino',
            'username': 'Lucas',
            'password': '123'
        },
        {
            'gender': 'Feminino',
            'username': 'Felipa',
            'password': '123'
        },
        {
            'gender': 'Outro',
            'username': 'Felipe',
            'password': '123'
        }

    ]

    def handle(self, *args, **kwargs):
        for user in self.users:
            user = User.objects.create(gender=user['gender'], username=user['username'], password=user['password'])
            user.save()

        self.stdout.write('Done!')
