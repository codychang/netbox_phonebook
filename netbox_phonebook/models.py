from django.db import models
from netbox.models import ChangeLoggedModel
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
import phonenumbers

class Function(ChangeLoggedModel):
    name = models.CharField(max_length=100, unique=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_phonebook:function', args=[self.pk])

class Status(ChangeLoggedModel):
    name = models.CharField(max_length=100, unique=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_phonebook:status', args=[self.pk])

class Number(ChangeLoggedModel):
    number = PhoneNumberField(blank=True, unique=True)
    site = models.ForeignKey(
        to='dcim.site',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    assignto = models.CharField(max_length=100,blank=True)
    function = models.ForeignKey(Function, on_delete=models.RESTRICT)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)
    comments = models.TextField(blank=True)

    def __str__(self):
        return phonenumbers.format_number(self.number, phonenumbers.PhoneNumberFormat.E164)

    def get_absolute_url(self):
        return reverse('plugins:netbox_phonebook:number', args=[self.pk])
