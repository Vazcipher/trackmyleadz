from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Company)
admin.site.register(UserLogin)
admin.site.register(Permission)
admin.site.register(UserRole)
admin.site.register(LeadSource)
