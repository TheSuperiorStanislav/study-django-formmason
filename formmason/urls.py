from django.contrib import admin
from django.urls import path

from main.views import HomeView, CustomFormView, FormResponseListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home'),
    path('form/<int:form_pk>', CustomFormView.as_view(), name = 'custom-form'),
    path('form/<int:form_pk>/responses', FormResponseListView.as_view(), name = 'form-responses'),
]
