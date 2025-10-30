from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Record

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})
def success(request):
    return render(request, 'blog/success.html')
from .models import Registration

def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'blog/registration_list.html', {'registrations': registrations})
Record.objects.filter(status='published')