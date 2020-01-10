from django.http import HttpResponse, HttpResponseBadRequest as Http400, Http404, JsonResponse
import json
from .models import Team, Task


def Json(data):
    return JsonResponse(data, safe=False)


def no_method_for_resouce(request):
    return Http404('Cannot perform method {} on resource {}'.format(request.method, request.path))


def missing_required_field(request, field_names):
    return Http400('body for {r.method} Request on resource {r.path}, must contain fields {}'.format(', '.join(field_names), r=request))


def handle_base_request(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        fields = ['name']
        if body.get(fields[0]) != None:
            return create(request, body.get(fields[0]))
        else:
            return missing_required_field(request, fields)
    elif request.method == 'GET':
        return get(request)
    else:
        return no_method_for_resouce(request)


def handle_specific_request(request, team_id):
    try:
        team = Team.objects.find(pk=team_id)
        if request.method == 'GET':
            return HttpResponse(team)
        elif request.method == 'DELETE':
            return delete(request, team)
        else:
            return no_method_for_resouce(request)
    except Team.DoesNotExist:
        raise Http404("Team Does not Exist")


def get(request):
    return Json([team.get_json() for team in Team.objects.all()])


def create(request, team_name):
    team = Team(name=team_name)
    team.save()
    return Json(team.get_json())


def delete(request, team):
    team.delete()
