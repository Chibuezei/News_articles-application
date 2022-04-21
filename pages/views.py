from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'


def say_hello(request):
    return HttpResponse('it is working')
    # return render(request,'heaven.html')
    # return render(request,'heaven.html',{'name': "mosh"})

