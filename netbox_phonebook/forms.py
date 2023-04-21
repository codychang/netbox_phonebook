from netbox.forms import NetBoxModelForm
from django import forms
from .models import Function, Status, Number
from dcim.models import Site

class FunctionForm(NetBoxModelForm):
    comments = forms.CharField(
                    widget=forms.Textarea(),
                    required=False)
    fieldsets = (
        ('Function', ('name',)),
    )

    class Meta:
        model = Function
        fields = ['name', 'comments']

class StatusForm(NetBoxModelForm):
    comments = forms.CharField(
                    widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}),
                    required=False)
    fieldsets = (
        ('Function', ('name',)),
    )
    class Meta:
        model = Status
        fields = ['name','comments']

class NumberForm(NetBoxModelForm):
    comments = forms.CharField(
                    widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}),
                    required=False)
    fieldsets = (
        ('Default Value', ('number','site')),
        ('Number Info', ('assignto','function','status')),
    )
    class Meta:
        model = Number
        fields = ['number','site','assignto','function','status','comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].disabled = True
        self.fields['site'].disabled = True

class NumberFilterForm(NetBoxModelForm):
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

    fieldsets = (
        ('Filter', ('site','function','status')),
    )

    class Meta:
        model = Number
        fields = ['site','function','status']
