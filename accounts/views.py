from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # the user wants to signup
        if request.POST['password1'] == request.POST['password2']: ## hanshof el password zae b3d wla la
            try:
                user = User.objects.get(username=request.POST['username']) ## lw tmam , hnshof eza kan el username taken abl kda wla la
                return render(request , 'accounts/signup.html' , {'error' : 'Username has already taken /n try another username'}) ## lw taken mn abl kda yrg3 el error da
            except User.DoesNotExist: ## lw msh taken mn abl kda ??!!!
                user = User.objects.create_user(username=request.POST['username'] , password=request.POST['password1']) ## nbtdy ndefo fe object gded bl esm wel pass
                auth.login(request , user) ## w adelo auth eno y3dy
                return redirect('home') ## w d5lo 3al home 3latol
        else:
            return render(request , 'accounts/signup.html' , {'error' : 'Paswoords MUST Match'})## lw el password b2a msh zae b3d nrg3 bl error da (else bta3t tany if fo2 )

    else:
        # user wants to enter info
        return render(request, 'accounts/signup.html') ## else bta3t awl if fo2

def login(request):
        if request.method == 'POST':
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render( request , 'accounts/login.html' ,  {'error' : 'Username OR Password is INCORRECT , Please try again with the correct username and password'})

        else:
            return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    ## Remember to route to homepage
    ## and dont forget to logout
    return render(request, 'accounts/logout.html')
