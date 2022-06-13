from django.db import models 

class Person(models.Model):
    personId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    birthDate = models.DateField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Study(models.Model):
    studyId = models.AutoField(primary_key=True)
    institutionName = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Projects(models.Model):
    projectId = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=50)
    projectDescription = models.CharField(max_length=1000)
    projectTechnologies = models.CharField(max_length=300)
    projectImage = models.ImageField(upload_to ='images/')
    projectLink = models.CharField(max_length=400)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Language(models.Model):
    languageId = models.AutoField(primary_key=True)
    languageName = models.CharField(max_length=40)
    languageLevel = models.CharField(max_length=40, default=None)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Experience(models.Model):
    experienceId = models.AutoField(primary_key=True)
    experienceName = models.CharField(max_length=100)
    experienceDescription = models.CharField(max_length=300)
    startDate = models.DateField()
    endDate = models.DateField()
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)


class Award(models.Model):
    awardId = models.AutoField(primary_key=True)
    awardName = models.CharField(max_length=80)
    awardDescription = models.CharField(max_length=300)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Contact(models.Model):
    contactId = models.AutoField(primary_key=True)
    contactType = models.CharField(max_length=90)
    contactDescription = models.CharField(max_length=100, default=None)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)

class OtherInformation(models.Model):
    infoId = models.AutoField(primary_key=True)
    infoName = models.CharField(max_length=80)
    infoDescription = models.CharField(max_length=300)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)





