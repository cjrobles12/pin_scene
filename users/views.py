from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """logs the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('pinscene:index'))

def register(request):
    """registers a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        #process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #logs user in and directs to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('pinscene:index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)
