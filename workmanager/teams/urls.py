from django.urls import path
from . import views as team_views
#from .. import task_views


urlpatterns = [
    # teams/...
    path('', team_views.handle_base_request, name='Teams'),
    path('<int:team_id>/', team_views.handle_specific_request, name='Specific Team'),
    path('<int:team_id>', team_views.handle_specific_request, name='Specific Team'),
]
