from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Location, subsection, Job, testimony, company
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages





def home(request):
    jobs = Job.objects.all()
    companyview = company.objects.all()
    cat = Category.objects.all()
    testimonies =testimony.objects.all()
 
    


    params = {
        'companyview':companyview,
        'cat':cat,
        'testimonies':testimonies,
        'jobs':jobs
    }
    return render (request, 'webpages/index1.html', params)
