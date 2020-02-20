from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import MedicalProfile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def update_profile(request):

    if not request.user.is_customer:
        return redirect('/')

    profile = request.user.medical_profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})


@login_required
def health_statistics(request):
    if request.is_ajax():
        profiles = MedicalProfile.objects.all()
        labels = ['diabetic', 'hypertensive', 'has_malaria',
                  'has_hiv', 'physically_challenged']
        counts = [
            profiles.filter(diabetic='Y').count(),
            profiles.filter(hypertensive='Y').count(),
            profiles.filter(has_malaria='Y').count(),
            profiles.filter(has_hiv='Y').count(),
            profiles.filter(physically_challenged='Y').count()
        ]

        return JsonResponse({'labels': labels, 'counts': counts})
