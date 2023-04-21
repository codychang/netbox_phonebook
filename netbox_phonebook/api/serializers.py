from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Number

class NumberSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_phonebook-api:number-detail'
    )
    site_name = serializers.CharField(source='site.name')
    function_name = serializers.CharField(source='function.name')
    status_name = serializers.CharField(source='status.name')
    class Meta:
        model = Number
        fields = (
            'id',
            'url',
            'number',
            'site',
            'site_name',
            'assignto',
            'function',
            'function_name',
            'status',
            'status_name',
            'comments',
        )


