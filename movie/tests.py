from django.test import TestCase
from django.contrib.auth.models import User
from .models import MovieType, Movie, Review
import datetime

# Create your tests here.
class MovieTypeTest(TestCase):
    def setUp(self):
        self.type=MovieType(moviegender='Romantic')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Romantic')

    def test_tablename(self):
        self.assertEqual(str(MovieType._meta.db_table), 'movietype')

class MovieTest(TestCase):
    def setUp(self):
        self.type=MovieType(moviegender='Romantic')
        self.user=User(username='userOne')
        self.movie=Movie(moviename='Titanic', user=self.user, dateentered=datetime.date(2022,3,22), datemoviereleased=datetime.date(1997,12,25), moviebudget=200.00, producturl='https://en.wikipedia.org/wiki/Titanic_(1997_film)' )
    
    def test_string(self):
        self.assertEqual(str(self.movie), 'Titanic')