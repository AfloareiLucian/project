from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Study, Language, Contact, Experience, Award, OtherInformation,Projects

def main_view(request):
    contact = Contact.objects.all()
    experience = Experience.objects.all()
    languages = Language.objects.all()
    information = OtherInformation.objects.all()
    person = Person.objects.get(personId=1)
    studies = list(Study.objects.all())
    awards = Award.objects.all()
    return render(request, 'my_cv.html', {'person': person,'studies':studies,'languages':languages, 'contacts':contact,'experience':experience,'awards':awards,'information':information})

def view(request):
    view = list(Projects.objects.all())
    return render(request, 'my_projects.html', {'projects': view})