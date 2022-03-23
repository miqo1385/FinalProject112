from django.test import TestCase
from django.contrib.auth.models import User
from .models import MovieType, Movie, Review
import datetime
from .forms import ReviewForms
from django.urls import reverse_lazy, reverse
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

class NewReviewForm(TestCase):
    def test_reviewforms(self):
        data={
                'moviename': 'Titanic',
                'user': 'miguel',
                'dateentered': '2022-3-22',
                'datemoviereleased': '1997-12-25',
                'moviebudget': '200.00',
                'producturl': 'https://en.wikipedia.org/wiki/Titanic_(1997_film)'
        }

        form=ReviewForms (data)
        self.assertTrue(form.is_valid)

class New_Review_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='Alcachofa123#')
        self.type=MovieType.objects.create(moviegender='romantic')
        self.movie=Movie.objects.create(moviename='Titanic',moviegender=self.type, user=self.test_user, dateentered=datetime.date(2022,3,22), datemoviereleased=datetime.date(1997,12,25), moviebudget=200.00, producturl='https://en.wikipedia.org/wiki/Titanic_(1997_film)')


    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newreview'))
        self.assertRedirects(response, '/accounts/login/?next=/movie/newreview/')

