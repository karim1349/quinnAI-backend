from django.contrib import admin

# Register your models here.
from api.models import Email, Label

admin.site.register(Email)
admin.site.register(Label)