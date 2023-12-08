from django.contrib import admin
from .models import Category, Location, subsection, Job, testimony, company



admin.site.site_header = 'OQQI Recruiter'
# Register your models here.

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(subsection)
admin.site.register(Job)
admin.site.register(testimony)
admin.site.register(company)