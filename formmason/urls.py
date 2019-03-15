from django.contrib import admin
from django.urls import path

from main.views import HomeView, CustomFormView, FormResponseListView, CreateEditFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home'),
    path('form/<int:form_pk>/', CustomFormView.as_view(), name = 'custom-form'),
    path('form/new/', CreateEditFormView.as_view(), name = 'create-form'),
    path('form/<int:form_pk>/edit', CreateEditFormView.as_view(), name = 'edit-form'),
    path('form/<int:form_pk>/responses/', FormResponseListView.as_view(), name = 'form-responses'),
]
