from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='about'),
    path('prediction/', views.prediction, name='about'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
]