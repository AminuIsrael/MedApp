from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login

from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from .forms import UserRegisterationForm
from .models import User

from medical_data.models import MedicalProfile
from medical_data.tables import UserTable
from medical_data.filters import UserFilter


class Dashboard(TemplateView):
    template_name = 'general_dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserListView(SingleTableMixin, FilterView):
    model = MedicalProfile
    template_name = 'doctor_dashboard.html'
    table = UserTable
    filterset_class = UserFilter

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):

        if not self.request.user.is_practitioner:
            return redirect('/')
        return super().dispatch(*args, **kwargs)


def user_signup(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.category = 'US'
            user = form.save()

            # The user's medical profile is better created here
            # Incase the user looses session during registration
            user.medical_profile.create()
            login(request, user)

            # send the user to the profile update screen
            return redirect('update')
    else:
        form = UserRegisterationForm()
    return render(request, 'user_registration.html', {'form': form})


def practitioner_signup(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.category = 'MP'
            user = form.save()

            login(request, user)

            # send the user to the dashboard
            return redirect('/')
    else:
        form = UserRegisterationForm()
    return render(request, 'user_registration.html', {'form': form})
