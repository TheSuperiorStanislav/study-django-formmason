from django.contrib import admin

from main.models import FormSchema, FormResponse

# Register your models here.
admin.site.register(FormSchema)
admin.site.register(FormResponse)