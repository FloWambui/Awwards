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
