from django.urls import path
from . import team_views


urlpatterns = [
    # teams/...
    path('', team_views.get, name='Get Teams'),
    path('<int:team_id>/', team_views.get_specific, name='Get a Team'),
]
