from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import NewUserForm, ProjectForm, RatingsForm, UpdateProfileForm, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Rates
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer



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


@login_required
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post_project = form.save(commit=False)
            post_project.user = current_user
            post_project.save()
            return redirect('app:homepage')
    else:
        form = ProjectForm()
    return render(request, 'projects.html', {"form": form})

@login_required
def view_project(request, id):
    project = Project.objects.get(id=id)
    rate = Rates.objects.filter(user=request.user, project=project).first()
    ratings = Rates.objects.all()
    rating_status = None
    if rate is None:
        rating_status = False
    else:
        rating_status = True
    current_user = request.user
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Rates()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (
                review.design + review.usability + review.content)/3
            review.save()
            return HttpResponseRedirect(reverse('app:viewProject', args=(project.id,)))
    else:
        form = RatingsForm()
    params = {
        'project': project,
        'form': form,
        'rating_status': rating_status,
        'reviews': ratings,
        'ratings': rate

    }
    return render(request, 'projectview.html', params)


def search(request):
    if 'project' in request.GET and request.GET['project']:
        project = request.GET.get("project")
        results = Project.search_project(project)
        message = f'project'
        return render(request, 'search.html', {'projects': results, 'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'search.html', {'message': message})


class ProfileList(APIView):
    def get(self, request, format=None):
        allprofiles = Profile.objects.all()
        serializer = ProfileSerializer(allprofiles, many=True)
        return Response(serializer.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        allprojects = Project.objects.all()
        serializer = ProjectSerializer(allprojects, many=True)
        return Response(serializer.data)