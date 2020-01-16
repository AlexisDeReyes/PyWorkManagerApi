#!/env/Scripts/python
"""Library containing the handlers associated with the Teams Resouce"""


from django.http import HttpRequest
from django.db.utils import IntegrityError
from .request_utils import route_base_request, route_specific_request, Http404, JsonResponse, no_method_for_resouce, no_items_found
from .models import Team, Task


def handle_base_request(request: HttpRequest):
    """Handles requests to the resource teams/ with no identifier

    Arguments:
        request {HttpRequest}

    Returns:
        HttpResponse -- HttpResponse or Error
    """
    return route_base_request(request, create, get)


def handle_specific_request(request: HttpRequest, team_id: int):
    """Handles requests to the resource teams/ with an identifier

    Arguments:
        request {HttpRequest}
        team_id {int}

    Raises:
        Http404: Team does not exist or no method for resource

    Returns:
        HttpResponse -- Http Response or error
    """
    return route_specific_request(request, Team, team_id, delete)


def get(request: HttpRequest):
    """Retrieves all instances of teams

    Arguments:
        request {HttpRequest}

    Returns:
        List -- List of teams
    """
    return [team.get_json() for team in Team.objects.all()]


def create(body: dict):
    """Creates a Team object

    Arguments:
        body {dict} -- request body

    Returns:
        dict -- dict representing the new team

    Raises:
        IntegrityError -- will hold information about required fields
    """
    if len(body) > 0:
        team_name = body.get('name')
        team = Team(name=team_name)
        team.save()
        return team.get_json()
    else:
        raise IntegrityError("_team.name")


def delete(request: HttpRequest, team: Team):
    """Deletes a team

    Arguments:\n
        request {HttpRequest}
        team {Team} -- Team to delete

    Returns:
        Team -- Deleted team
    """
    team.delete()
    return team.get_json()
