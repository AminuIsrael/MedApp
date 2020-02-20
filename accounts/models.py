from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    CATEGORIES = (
        ('US', 'User'),
        ('MP', 'Medical Practitioner'),
    )
    
    category = models.CharField(max_length=2, default='US')

    @property
    def is_customer(self):
        return self.category == 'US'

    @property
    def is_practitioner(self):
        return self.category == 'MP'

