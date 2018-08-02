from django.shortcuts import render
from .forms import UserProfileInfoForm, UserForm

def index(request):
	return render(request, 'users_app/index.html')

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
		'user_form' : user_form,
		'profile_form' : profile_form,
		'registered' : registered
	}

	return render(request, 'users_app/registration.html', context)



