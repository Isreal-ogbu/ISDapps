from django.shortcuts import render, redirect
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def Logout_views(request):
    """log out function"""
    logout(request)
    return HttpResponseRedirect(reverse('login'))

#def accounts_logout(request):
#    logout(request)
#    url = reverse("accounts:login")
#    return redirect(url, args=(),kwargs={})

def register(request):
    """register new user"""
    if request.method != 'POST':
        """return a blank creation form"""
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid:
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('Home'))
    context={
        'form': form
    }
    return render(request, 'registration/register.html', context=context)
