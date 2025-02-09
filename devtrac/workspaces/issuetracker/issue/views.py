from django.contrib.auth.mixins import LoginRequiredMixin
from ..packages.crud.base import BaseCrudView
from .models import Issue
from .tables import IssueTable
from .forms import IssueForm
from .workflow import IssueWorkflow

class TodoCrudView(BaseCrudView):
    page_title = "Issue list"
    add_btn_title = "New Issue item"
    table = IssueTable
    form = IssueForm
    workflow = IssueWorkflow

    def display_add_button_check(self, request):
        return True

