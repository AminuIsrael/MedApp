import django_tables2 as tables
from .models  import MedicalProfile

class UserTable(tables.Table):
    class Meta:
        model = MedicalProfile
        template_name = "django_tables2/bootstrap.html"
        fields = ("username", )
