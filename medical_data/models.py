from django.db import models
from accounts.models import User



class MedicalProfile(models.Model):

    BLOOD_GROUPS = (
        ('O-', 'O Negative'),
        ('O+', 'O Positive'),
        ('A-', 'A Negative'),
        ('A+', 'A Positive'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
    )
    GENOTYPES = (
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('AC', 'AC'),
        ('SS', 'SS'),
        ('SC', 'SC'),
        ('CC', 'CC'),
    )
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    MARITAL_STATUSES = (
        ('MA', 'Married'),
        ('SG', 'Single'),
        ('DV', 'Divorced')
    )
    YesOrNo = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='medical_profile')
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    genotype = models.CharField(max_length=2, choices=GENOTYPES)
    gender = models.CharField(max_length=1, choices=GENDERS)
    marital_status = models.CharField(max_length=2, choices=MARITAL_STATUSES)
    height = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    physically_challenged = models.CharField(max_length=1, choices=YesOrNo)
    has_hiv = models.CharField(max_length=1, choices=YesOrNo)
    has_malaria = models.CharField(max_length=1, choices=YesOrNo)
    hypertensive = models.CharField(max_length=1, choices=YesOrNo)
    diabetic = models.CharField(max_length=1, choices=YesOrNo)

    def __str__(self):
        return f"{self.user.username}'s medical record"
