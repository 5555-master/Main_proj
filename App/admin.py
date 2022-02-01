from django.contrib import admin

# Register your models here.
from App.models import Contact,Profile,Pick

admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Pick)