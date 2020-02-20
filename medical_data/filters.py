import django_filters
from .models import MedicalProfile


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = MedicalProfile
        exclude = ('user','height', 'weight')