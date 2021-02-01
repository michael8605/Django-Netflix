from django.shortcuts import render , redirect
from django.contrib import messages, auth
from .models import Movies
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
import json

# Create your views here.
class HomeView(View):
    def get(self, request):

        return render(request, "pages/home.html")


class LoginView(View):
    def get(self, request):
        return render(request, "pages/login.html")


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('home'))


class MoviesView(View):
    def get(self, request):
        movies1 = Movies.objects.all().order_by('image_path')
        movies2 = Movies.objects.all().order_by('-image_path')
        context = {
            'movies1' : movies1,
            'movies2' : movies2
        }
        return render(request, "pages/movie_list.html", context)


class MoviesDetail(View):
    def get(self, request, id):
        movies1 = Movies.objects.get(category_id = id)
        print(movies1)
        # movies2 = Movies.objects.all().order_by('-image_path')
        context = {
            'movies1' : movies1,
            'test' : 'Lets test this'
        }
        return render(request, "pages/movie_detail.html", context)


class SignUpView(View):
    def get(self, request):
        return render(request, "pages/sign_up.html")

class ProcessFormView(View):
    def post(self, request):
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']


        # user = User()
        # user.username = username
        if password == password_confirm:
            user = User.objects.create_user(username, username, password)
            # user.set_password('password')
            user.save()

            messages.info(request, 'User Successfully Register')
            return HttpResponseRedirect(reverse('login'))
        else:
            messages.info(request, 'Password not match')
            return HttpResponseRedirect('register')

    def get(self, request):
        return render(request, 'pages/sign_up.html')


class AuthView(View):
    def post(self, request):
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']

        # username = User.objetcs.get(email=email).username
        user = auth.authenticate( username = username, password = password)

        if user is not None:
        # if users.email == email:
        #     if users.password == password:
                auth.login(request,user)
                return HttpResponseRedirect('movies')
        else:
            Status = [{"validation": "Authentication failure","status": False}]
            return HttpResponse(json.dumps(Status), content_type= "application/json")

    # def get(self, request):
    #     return HttpResponse(json.dumps([{"validation": "There is nothing in there", "status": False}]), content_type= "application/json")


