from .views import HomeView, LoginView, MoviesView, SignUpView, ProcessFormView, AuthView, LogoutView, MoviesDetail
from django.urls import path

urlpatterns = [
    path('home/', HomeView.as_view(), name = 'home'),
    path('login', LoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    path('movies/', MoviesView.as_view(), name = 'movies'),
    path('movies_detail/<int:id>', MoviesDetail.as_view(), name = 'movies_detail'),
    path('signup', SignUpView.as_view(), name = 'signup'),
    path('process_form/', ProcessFormView.as_view(), name = 'process_form'),
    path('auth_form', AuthView.as_view(), name = 'auth_form'),
]