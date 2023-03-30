import django_filters
from netbox.filtersets import ChangeLoggedModelFilterSet
from .models import Function, Status, Number
from dcim.models import Site
from django.db.models import Q

class FunctionFilterSet(ChangeLoggedModelFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = Function
        fields = ['name','comments']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value)
            | Q(comments__icontains=value)
        )

class StatusFilterSet(ChangeLoggedModelFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = Status
        fields = ['name','comments']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value)
            | Q(comments__icontains=value)
        )

class NumberFilterSet(ChangeLoggedModelFilterSet):
    site = django_filters.ModelChoiceFilter(
        queryset=Site.objects.all(),
    )

    function = django_filters.ModelChoiceFilter(
        queryset=Function.objects.all(),
    )

    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
    )

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = Number
        fields = ['site','function','status']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(assignto__icontains=value)
            | Q(site__name__icontains=value)
            | Q(function__name__icontains=value)
            | Q(status__name__icontains=value)
            | Q(number__icontains=value)
            | Q(comments__icontains=value)
        )