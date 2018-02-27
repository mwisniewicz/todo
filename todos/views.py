from django.shortcuts import render
from todos.forms import UserForm, UserProfileInfo 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
	return render(request, 'todos/index.html')

def register(request):

	registered = False

	if request.method == "POST":

		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfo(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_picture = request.FILES['profile_picture']

			profile.save()

			registered = True

		else:

			print(user_form.errors, profile_form.errors)

	else:

		user_form = UserForm()
		profile_form = UserProfileInfo()

	return render(request, 'todos/registration.html',
							{'user_form':user_form,
							 'profile_form':profile_form,
							 'registered': registered
							 })
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('todos:index'))

def user_login(request):
    
    if request.method == 'POST':
    	username = request.POST.get('username')
    	password = request.POST.get('password')

    	user = authenticate(username=username,password=password)

    	if user:
    		if user.is_active:
    			login(request,user)
    			return HttpResponseRedirect(reverse('todos:index'))

    		else:
    			return HttpResponse("Account not active!")

    	else:
    		return HttpResponse("Invalid login details!")

    else:
    	return render(request, 'todos/login.html',{})
