import json

from django import forms

class NewDynamicForm(forms.Form):
    form_pk = forms.CharField(
        widget = forms.HiddenInput,
        required = False
    )
    title = forms.CharField()
    schema = forms.CharField(widget = forms.Textarea)

    def clean_schema(self):
        schema = self.cleaned_data['schema']
        try:
            schema = json.loads(schema)
        except:
            raise forms.ValidationError('Invalid JSON') 
        
        return schema 
