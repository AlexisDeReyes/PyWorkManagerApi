#!/env/Scripts/python
"""Library containing the handlers associated with the Teams Resouce"""

from django.http import HttpRequest, HttpResponse
from django.db.utils import IntegrityError

from workmanager.request_utils import route_base_request, no_items_found, Json, find_resource_continue_or_404 as find_team
from workmanager.models import Team, Task


def handle_base_request(request: HttpRequest, team_id: int) -> HttpResponse:
    def route_request(resource: Team):
        if request.method == 'GET':
            results = get_all(resource)
            if len(results) > 0:
                return Json(results)
            return no_items_found(request)
        if request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            try:
                return Json(create(body, resource))
            except IntegrityError as error:
                return handle_integrity_error(error, request)
        return no_method_for_resouce(request)

    return find_team(Team, request, team_id, route_request)


def get_all(team: Team):
    return [task.get_json() for task in team.task_set.all()]


def create(body: dict, team: Team):
    if len(body) > 0:
        task_name = body.get('name')
        task_effort = int(body.get('effort'))
        task_description = int(body.get('description'))
        new_task = Task(name=task_name, effort=task_effort,
                        description=task_description)
        team.save()
        return task.get_json()
    else:
        raise IntegrityError("task.name")
