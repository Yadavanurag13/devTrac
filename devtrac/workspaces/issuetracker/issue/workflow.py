from ..packages.workflow.base.engine import WorkflowBase
from .models import Issue

class IssueWorkflow(WorkflowBase):
    status_transitions = [
        {
            "name": "open_to_progress",
            "display_name": "Start Progress",
            "description": "Move issue to in progress state",
            "from": "Open",
            "to": "In Progress",
            "confirmation_message": "Are you sure you want to start working on this issue?",
        },
        {
            "name": "progress_to_resolved",
            "display_name": "Mark Resolved",
            "description": "Mark this issue as resolved",
            "from": "In Progress",
            "to": "Resolved",
            "confirmation_message": "Are you sure you want to mark this issue as resolved?",
        },
        {
            "name": "resolved_to_progress",
            "display_name": "Reopen Issue",
            "description": "Reopen this issue and move back to in progress",
            "from": "Resolved",
            "to": "In Progress",
            "confirmation_message": "Are you sure you want to reopen this issue?",
        },
        {
            "name": "open_to_resolved",
            "display_name": "Direct Resolution",
            "description": "Mark issue as resolved directly",
            "from": "Open",
            "to": "Resolved",
            "confirmation_message": "Are you sure you want to mark this issue as resolved?",
        }
    ]

    def open_to_progress_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.IssueType.IN_PROGRESS
        object_instance.save()

    def progress_to_resolved_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.IssueType.RESOLVED
        object_instance.save()

    def resolved_to_progress_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.IssueType.IN_PROGRESS
        object_instance.save()

    def open_to_resolved_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.IssueType.RESOLVED
        object_instance.save()

    class Meta:
        statuses = {
            "Open": {
                "color": "#3498db",  # Blue
                "label": "Open",
            },
            "In Progress": {
                "color": "#f1c40f",  # Yellow
                "label": "In Progress",
            },
            "Resolved": {
                "color": "#2ecc71",  # Green
                "label": "Resolved",
            }
        }
        model = Issue
        on_create_status = "Open"