from django.db import models
from PIL import Image
from datetime import timedelta, datetime, date


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000, null=True, verbose_name="Category title")
    icon = models.ImageField(upload_to='category/images', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'




class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000, null=True, verbose_name="Location name")

    def __str__(self):
        return f'{self.name}'


class subsection(models.Model):
    subsection_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=2000, null=True, verbose_name="Job recruitment type")
    color = models.CharField(max_length=50, null=True)


    def __str__(self):
        return f'{self.name}'







class Job (models.Model):

    gender =(
        ("Male", 'Male'),
        ("Female", 'Female'),
        ("Both",'Both'),
        ("None", 'None'),
    )


    job_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=2000, null=True, verbose_name="Job title")
    description = models.TextField(verbose_name= "Job Description")
    requirement = models.TextField(verbose_name= "Job Requirement")
    responsibilities = models.TextField(verbose_name= " Responsibilities")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sub = models.ForeignKey(subsection, on_delete=models.CASCADE, null=True)
    sex = models.CharField(max_length=20, choices=gender, null=True, verbose_name="Gender for the job")
    skill = models.CharField(max_length=2000, null=True, verbose_name="Job expected skills")
    pay = models.IntegerField()
    url = models.CharField(max_length=2000, null=True, verbose_name="Google form iframe link")
    uploaded = models.DateField(auto_now=True, null=True)
    deadline = models.DateField(verbose_name="Application deadline")
    image = models.ImageField(upload_to='job/images', null=True, blank=True)


    @property
    def daysago(self):
        days = (datetime.now().date() - self.uploaded).days
        if days ==0:
            days = "Today"
        else:
            af = "days ago"
            days = f'{days}{af}'
        return days


    def __str__(self):
        return f'{self.title}, {self.category}'




class testimony(models.Model):
    testimony_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=2000, null=True, verbose_name="Testimonial name")
    category = models.ForeignKey(Category, verbose_name="job category", on_delete=models.CASCADE)
    testimonies =  models.TextField(verbose_name="Testimony")
    image = models.ImageField(upload_to='testimony/images', null=True, blank=True, verbose_name="Testimonial Picture")

    def __str__(self):
        return f'{self.name}'


class company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=2000, null=True, verbose_name="Company name")
    picture = models.ImageField(upload_to='company/images', null=True, blank=True, verbose_name="Company Picture")

    def __str__(self):
        return f'{self.name}'






















