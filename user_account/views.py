from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from . forms import UserRegistrationForm
from .models import OrganizationProfile
from django.contrib import messages

@login_required
def dashboard(request):
  return render(request, 'user_account/dashboard.html', {'section': 'dashboard'})

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      try:
        # Create User
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Create Organization Profile
        OrganizationProfile.objects.create(
          user=user,
          registration_number=form.cleaned_data['registration_number'],
          phone_number=form.cleaned_data['phone_number'],
        )

        # Auto-login & redirect
        login(request, user)
        messages.success(request, 'Registration successful! Complete your profile details After you have logged in.')
        return redirect('user_account:login')
      
      except Exception as e:
        messages.error(request, f'Registration failed: {str(e)}')
    else:
      messages.error(request, 'Please correct the errors below.')
  else:
    form = UserRegistrationForm()

  return render(request, 'user_account/register.html', {
    'form': form,
    'section': 'register',
  })


