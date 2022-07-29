from django.test import TestCase
from polls.models import User, Punishment

class PunishmentTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(id=1, username="a", password="b", gender="Masculino")
        Punishment.objects.create(id=1, user=user, punishment=1)

    def test_punishment_register(self):
        p = Punishment.objects.get(id=1)
        
        print(p.get_punishment_display())