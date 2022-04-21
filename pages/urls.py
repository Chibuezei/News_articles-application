from django.urls import URLPattern, path
from . import views

#url configfile
# urlpatterns = [path('', views.HomePageView.as_view(), name = 'home')] #this was causing me namespace error: reverse not found
urlpatterns = [path('', views.HomePageView.as_view(), name = 'home'),

path('about/', views.AboutView.as_view(), name = 'about')]
