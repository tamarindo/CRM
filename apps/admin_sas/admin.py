from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Service)
admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(DniType)
admin.site.register(type_service)
admin.site.register(implementation)
admin.site.register(imagen_portfolio)
admin.site.register(publicidad)
