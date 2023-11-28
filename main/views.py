from django.shortcuts import render
from .models import Slider, Team, Testimonial


# Create your views here.

def index(request):
    slider = Slider.objects.all()
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()

    return render(request, 'index.html', {'navbar': 'index', 'slider': slider, 'team': team, 'testimonial': testimonial})


def about(request):
    team = Team.objects.all()
    return render(request, 'about.html', {'navbar': 'about', 'team': team})


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})
