from netbox.views import generic
from . import forms, models, tables, filtersets

# Number Function
class FunctionView(generic.ObjectView):
    queryset = models.Function.objects.all()

class FunctionListView(generic.ObjectListView):
    queryset = models.Function.objects.all()
    filterset = filtersets.FunctionFilterSet
    table = tables.FunctionTable

class FunctionEditView(generic.ObjectEditView):
    queryset = models.Function.objects.all()
    form = forms.FunctionForm

class FunctionDeleteView(generic.ObjectDeleteView):
    queryset = models.Function.objects.all()

# Number Status
class StatusView(generic.ObjectView):
    queryset = models.Status.objects.all()

class StatusListView(generic.ObjectListView):
    queryset = models.Status.objects.all()
    filterset = filtersets.StatusFilterSet
    table = tables.StatusTable

class StatusEditView(generic.ObjectEditView):
    queryset = models.Status.objects.all()
    form = forms.StatusForm

class StatusDeleteView(generic.ObjectDeleteView):
    queryset = models.Status.objects.all()
    default_return_url = "plugins:netbox_phonebook:status_list"

# Number
class NumberView(generic.ObjectView):
    queryset = models.Number.objects.all()

class NumberListView(generic.ObjectListView):
    queryset = models.Number.objects.all()
    filterset = filtersets.NumberFilterSet
    filterset_form = forms.NumberFilterForm
    table = tables.NumberTable
    actions = ['export']

class NumberEditView(generic.ObjectEditView):
    queryset = models.Number.objects.all()
    form = forms.NumberForm
