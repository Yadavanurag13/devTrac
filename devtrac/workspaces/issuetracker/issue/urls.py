from django.urls import path
from .views import TodoCrudView

urlpatterns = [
    path('all/', TodoCrudView.as_view(), name='todo_crud'),
]