from django.urls import URLPattern, path
from . import views
from django.views.generic.base import TemplateView # new

#url configfile
# urlpatterns = [path('', views.HomePageView.as_view(), name = 'home')] #this was causing me namespace error: reverse not found(assigned urlpatterns twice, poor me)
urlpatterns = [
                path('', views.HomePageView.as_view(), name = 'home'),
                # path('', TemplateView.as_view(template_name='home.html'), name = 'home' ), #this and the one above does the same thing

            path('about/', views.AboutView.as_view(), name = 'about')]
