import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import Function, Status, Number
from netbox.tables import columns

class FunctionTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    comments = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Function
        fields = ['name','comments']
        default_columns = ['name','comments']

class StatusTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    comments = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Status
        fields = ['name','comments']
        default_columns = ['name','comments']

class NumberTable(NetBoxTable):
    number = tables.Column(
        linkify=True
    )

    comments = tables.Column()
    actions = columns.ActionsColumn(actions=('edit', 'changelog'))

    class Meta(NetBoxTable.Meta):
        model = Number
        fields = ['number','site','assignto','function','status','comments']
        default_columns = ['number','site','assignto','function','status']
