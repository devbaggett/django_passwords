from django.shortcuts import render, HttpResponse, redirect
from .forms import UserProfileInfoForm, UserForm

from django.urls import reverse
# view to require user be logged in
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'users_app/index.html')

@login_required
def special(request):
	return HttpResponse("You are logged in, nice!")

# login decorator (has to be directly on top)
@login_required
def user_logout(request):
	logout(request)
	return redirect(reverse('index'))


def register(request):

    # assume user not registered
    registered = False

    if request.method == "POST":
        # grab information off of forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # grab from base user form
            user = user_form.save()
            # hash password
            user.set_password(user.password)
            # save hashed password to db
            user.save()

            # grab profile form
            profile = profile_form.save(commit=False)
            profile.user = user

            # check if picture before we save
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            # save model
            profile.save()

            # registration successful
            registered = True

        # print out errors
        else:
            print(user_form.errors, profile_form.errors)

    # request wasn't an HTTP request; didn't post a nything
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request, 'users_app/registration.html', context)


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		# built in auth function, authenticate user
		user = authenticate(username=username,password=password)

		# if user is active, log them in
		if user:
			if user.is_active:
				login(request, user)
				return redirect(reverse('index'))
			else:
				return HttpResponse("Account not active")
		else:
			print("Someone tried to login and failed!!!")
			print("Username: {} and password {}".format(username, password))
			return HttpResponse("Invalid login details supplied!")
	else:
		return render(request, "users_app/login.html", {})

