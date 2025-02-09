from ..packages.crud.table.base import ModelTable
from ..packages.crud.table.column import ModelCol

from .models import Issue
from .forms import IssueForm

class IssueTable(ModelTable):
    id = ModelCol(display_as='ID', sortable=True, searchable=True)
    title = ModelCol(display_as='Title', sortable=True, searchable=True)
    description = ModelCol(
        display_as='Description', 
        sortable=True, 
        searchable=True
    )
    status = ModelCol(
        display_as='Status', 
        sortable=True,
        searchable=True,
        filterable=True 
    )
    assignee = ModelCol(
        display_as='Assignee',
        sortable=True,
        searchable=True,
        filterable=True
    )
    created_at = ModelCol(
        display_as='Created',
        sortable=True,
        date_format='%Y-%m-%d %H:%M'
    )

    table_actions = [
        {
            "name": "Create",
            "key": "create",
            "description": "Create New Issue",
            "type": "form",
            "form": IssueForm,
        }
    ]
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Issue",
            "type": "form",
            "form": IssueForm,
        },
        {
            "name": "Delete",
            "key": "delete",
            "description": "Delete Issue",
            "type": "confirm",
            "confirm_message": "Are you sure you want to delete this issue?"
        }
    ]


    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'status', 'assignee', 'created_at']
        row_selector = {'enabled': True, 'multi': True} 
        per_page = 25 
        order_by = ['-created_at'] 