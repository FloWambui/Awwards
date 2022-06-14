from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse, HttpResponseRedirect
from .forms import NewUserForm, UpdateProfileForm, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("app:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("app:homepage")



def home(request):
    profile = Profile.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {"profile": profile, "projects": projects})

@login_required
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user=current_user.id).all
    return render(request, 'profile.html', {"projects": projects})

@login_required
def update_profile(request):
    projects = Project.objects.all()
    posts = Profile.objects.all()
    user_form = UpdateUserForm(request.POST or None, request.FILES, instance=request.user)
    profile_form = UpdateProfileForm(request.POST or None, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return HttpResponseRedirect("/profile")

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    'posts':posts,
    'projects':projects,
    }


    return render(request, "profileupdate.html", {"user_form": user_form, "profile_form": profile_form })




#     def updateprofile(request):
#     projects = Project.objects.all()
#     posts = Profile.objects.all()
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, f'Your account has been successfully updated')
#             return redirect('profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     context = {
#     'user_form':user_form,
#     'profile_form':profile_form,
#     'posts':posts,
#     'projects':projects,
#     }

#     return render(request, 'profileupdate.html', context)

# def update_profile(request, id):
#     obj = get_object_or_404(Profile, user_id=id)
#     obj2 = get_object_or_404(User, id=id)
#     form = UpdateProfileForm(request.POST or None, request.FILES, instance=obj)
#     form2 = UpdateUserForm(request.POST or None, instance=obj2)
#     if form.is_valid() and form2.is_valid():
#         form.save()
#         form2.save()
#         return HttpResponseRedirect("/profile")

#     # return render(request, "registration/update_profile.html", {"form": form, "form2": form2})