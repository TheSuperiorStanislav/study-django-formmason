from __future__ import unicode_literals

from django.db import models

from jsonfield import JSONField
# Create your models here.

class FormSchema(models.Model):
    title = models.CharField(max_length = 100)
    schema = JSONField()

    def __str__(self):
        return self.title

class FormResponse(models.Model):
    form = models.ForeignKey(
        FormSchema,
        on_delete = models.CASCADE
    )
    response = JSONField()

