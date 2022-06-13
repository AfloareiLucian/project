from django.contrib import admin
from .models import Person, Study, Language, Contact, Experience, Award, OtherInformation, Projects

newApp = [Person, Study, Language, Contact, Experience, Award, OtherInformation,Projects]
admin.site.register(newApp)