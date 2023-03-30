from django.forms import ModelForm
from django import forms
from .models import Function, Status, Number
from dcim.models import Site

class FunctionForm(ModelForm):
    class Meta:
        model = Function
        fields = ['name','comments']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name','comments']

class NumberForm(ModelForm):
    class Meta:
        model = Number
        fields = ['number','site','assignto','function','status','comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].disabled = True

class NumberFilterForm(ModelForm):
    site = forms.ModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
    )

    function = forms.ModelChoiceField(
        queryset=Function.objects.all(),
        required=False,
    )

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
    )

    class Meta:
        model = Number
        fields = ['site','function','status']
