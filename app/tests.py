from django.test import TestCase
from .models import Profile, Project, Rates
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    """Test for the profile model class"""
    def setUp(self):
        self.user = User(username='')
        self.user.save()

        self.profile = Profile(id=4, profile_pic='profile.jpg', bio='this is a test profile',contact='0700000000',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class RatesTestCase(TestCase):
    def setUp(self):
        self.user = User(username='Suni')
        self.user.save()
        self.new_profile = Profile(id = 1,profile_pic='profile.png',bio='this is a test profile',user=self.user)
        self.new_profile.save()
        self.new_project = Project(image='profile.png',title="image",url='http', description='test profile description', date='13/06/2022',
        profile=self.new_profile)
        self.rate = Rates(design='10',usability='8',content='6',project = self.new_project, date="13/06/2022")

    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Rates))