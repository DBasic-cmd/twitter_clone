from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def landing(request):
    return render(request, 'users/landing.html')

def register(request):
    form = UserRegistrationForm(request.POST)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'you have successfully created an account')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            if user.is_active:
                auth.login(request, user)
                return redirect('twitter-home')
            else:
                messages.error(request, 'invalid account')
                return render(request, 'users/landing.html')
        elif user is not None and not user.is_staff:
            if user.is_active:
                auth.login(request, user)
                return redirect('twitter-home')
            else:
                messages.warning(request, 'account is not active')
                return render(request, 'users/landing.html')
        else:
            messages.error(request, 'please enter valid details')
            return render(request, 'users/landing.html')
    context = {}
    return render(request, 'users/login.html', context)



