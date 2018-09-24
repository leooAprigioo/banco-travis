from django.test import TestCase
from .models import *

class teste(TestCase):

    def testeSimple(self):
        banco = Banco()
        menu = Menu()
        banco.setMenu(menu)
        self.assertRaises(Exception, banco.deposita(1000))

# Create your tests here.
