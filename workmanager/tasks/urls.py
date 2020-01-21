from django.urls import path
from . import views as task_views


urlpatterns = [
    # teams/...
    path('<int:team_id>/tasks', task_views.handle_base_request, name='Tasks'),
]
