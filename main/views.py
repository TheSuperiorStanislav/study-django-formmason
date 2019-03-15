import json

from django.shortcuts import render
from django import forms
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView, ListView, TemplateView
from django.urls import reverse
from main.models import FormSchema, FormResponse

class HomeView(ListView):
    model = FormSchema
    template_name = 'home.html'


class CustomFormView(FormView):
    template_name = 'custom_form.html'

    def get_form(self, form_class=None):
        form_structure = FormSchema.objects.get(
            pk = self.kwargs['form_pk']
        ).schema

        custom_form = forms.Form(**self.get_form_kwargs())

        for key, value in form_structure.items():
            field_class = self.get_field_class_from_type(value)
            if field_class is not None:
                custom_form.fields[key] = field_class()
            else:
                raise TypeError('Invalid field type {}'.format(value))
            
        return custom_form

    def form_valid(self, form):
        custom_form = form_structure = FormSchema.objects.get(
            pk = self.kwargs['form_pk']
        )
        user_response = form.cleaned_data

        form_response = FormResponse(
            form = custom_form,
            response = user_response
        )
        form_response.save()

        return HttpResponseRedirect(reverse('home'))
    def get_field_class_from_type(self, value_type):
        if value_type == 'string':
            return forms.CharField
        elif value_type == 'number':
            return forms.IntegerField

class FormResponseListView(TemplateView):
    template_name = 'form_responses.html'

    def get_context_data(self, **kwargs):
        ctx = super(FormResponseListView, self).get_context_data(**kwargs)

        form = self.get_form()
        schema = form.schema
        form_fields = schema.keys()
        ctx['headers'] = form_fields
        ctx['form'] = form

        responses = self.get_queryset()
        responses_list = []
        for response in responses:
            response_values = []
            response_data = response.response
            for field_name in form_fields:
                if field_name in response_data:
                    response_values.append(response_data[field_name])
                else:
                    response_values.append('')
            responses_list.append(response_values)
        
        ctx['responses_list'] = responses_list

        return ctx

    def get_queryset(self):
        form = self.get_form()
        return FormResponse.objects.filter(form = form)

    def get_form(self):
        return FormSchema.objects.get(pk = self.kwargs['form_pk'])