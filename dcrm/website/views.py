from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    #Check to see if logging in
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been Logged In")
            return redirect ('home')
        else:
            messages.success(request, "There was an error logging in....")
            return redirect('home')
        
    return render (request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have been Logged Out....!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        form = SignUpForm()
    
    # Ensure the form is rendered in both GET and invalid POST scenarios
    return render(request, 'register.html', {'form': form})
