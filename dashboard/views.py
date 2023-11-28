from django.shortcuts import render, redirect
from main.models import Slider, Testimonial, Team

from django.contrib import messages


# Create your views here.
def dashboard(request):
    return render(request, 'admindash.html', {'navbar': 'admindash'})


def webcontent(request):
    slider = Slider.objects.all()
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()
    slider_count = Slider.objects.count()
    team_count = Team.objects.count()
    testimonial_count = Testimonial.objects.count()
    return render(request, 'webcontent.html',
                  {'navbar': 'webcontent', 'slider': slider, 'team': team, 'testimonial': testimonial,
                   'slider_count': slider_count, 'team_count': team_count, 'testimonial_count': testimonial_count})


def allSliders(request):
    slider = Slider.objects.all()
    slider_count = Slider.objects.count()
    return render(request, 'all_sliders.html', {'navbar': 'webcontent', 'slider': slider, 'slider_count': slider_count})


def theTeam(request):
    team = Team.objects.all()
    team_count = Team.objects.count()
    return render(request, 'the_team.html', {'navbar': 'webcontent', 'team': team, 'team_count': team_count})


def allTestimonials(request):
    testimonial = Testimonial.objects.all()
    testimonial_count = Testimonial.objects.count()
    return render(request, 'all_testimonials.html',
                  {'navbar': 'webcontent', 'testimonial': testimonial, 'testimonial_count': testimonial_count})


def addSlider(request):
    return render(request, 'add_slider.html', {'navbar': 'webcontent'})


def addTeam(request):
    return render(request, 'add_team.html', {'navbar': 'webcontent'})


def addTestimony(request):
    return render(request, 'add_testimonial.html', {'navbar': 'webcontent'})


def editSlider(request, id):
    if request.method == "POST":
        headline = request.POST.get('headline')
        description = request.POST.get('description')
        status = request.POST.get('status')
        image = request.FILES['image']

        slider = Slider.objects.get(id=id)

        slider.headline = headline
        slider.description = description
        slider.status = status
        slider.image = image

        slider.save()
        messages.success(request, 'Data updated successfully!')
        return redirect("/dashboard/all-sliders")

    slider = Slider.objects.get(id=id)
    return render(request, 'edit_slider.html', {'navbar': 'webcontent', 'slider': slider})


def editTeam(request):
    return render(request, 'edit_team.html', {'navbar': 'webcontent'})


def editTestimonial(request):
    return render(request, 'edit_testimonial.html', {'navbar': 'webcontent'})


def insert_slider(request):
    if request.method == "POST":
        headline = request.POST.get('headline')
        description = request.POST.get('description')

        if len(request.FILES) != 0:
            image = request.FILES['image']
        query = Slider(headline=headline, description=description, image=image)
        query.save()
        messages.success(request, 'Slider added successfully!')
        return redirect("/dashboard/all-sliders")
    return redirect("/dashboard/all-sliders")


def insert_team(request):
    if request.method == "POST":
        name = request.POST.get('name')
        position = request.POST.get('position')
        fb_link = request.POST.get('fb_link')
        twitter_link = request.POST.get('twitter_link')
        instagram_field = request.POST.get('instagram_field')

        if len(request.FILES) != 0:
            image = request.FILES['image']

        query = Team(name=name, position=position, image=image, fb_link=fb_link, twitter_link=twitter_link,
                     instagram_field=instagram_field)
        query.save()
        messages.success(request, 'Team Member added successfully!')
        return redirect("/dashboard/the-team")
    return redirect("/dashboard/the-team")


def insert_testimonial(request):
    if request.method == "POST":
        headline = request.POST.get('headline')
        description = request.POST.get('description')

        if len(request.FILES) != 0:
            image = request.FILES['image']
        query = Testimonial(headline=headline, description=description, image=image)
        query.save()
        messages.success(request, 'Slider added successfully!')
        return redirect("/dashboard/all-testimonials")
    return redirect("/dashboard/all-testimonials")


def editTeam(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        position = request.POST.get('position')
        fb_link = request.POST.get('fb_link')
        twitter_link = request.POST.get('twitter_link')
        instagram_field = request.POST.get('instagram_field')
        image = request.FILES['image']

        team = Team.objects.get(id=id)

        team.name = name
        team.position = position
        team.fb_link = fb_link
        team.twitter_link = twitter_link
        team.instagram_field = instagram_field
        team.image = image

        team.save()
        messages.success(request, 'Data updated successfully!')
        return redirect("/dashboard/the-team")

    team = Team.objects.get(id=id)
    return render(request, 'edit_team.html', {'navbar': 'webcontent', 'team': team})


def editTestimonial(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        course = request.POST.get('course')
        testimony = request.POST.get('testimony')
        image = request.FILES['image']

        testimonial = Testimonial.objects.get(id=id)

        testimonial.name = name
        testimonial.course = course
        testimonial.testimony = testimony
        testimonial.image = image

        testimonial.save()
        messages.success(request, 'Data updated successfully!')
        return redirect("/dashboard/all-testimonials")

    testimonial = Testimonial.objects.get(id=id)
    return render(request, 'edit_testimonial.html', {'navbar': 'webcontent', 'testimonial': testimonial})
