from django.http import HttpResponse, HttpResponseBadRequest as Http400, Http404, as Json
from .models import Team, Task


def no_method_for_resouce(request):
    return Http404('Cannot perform method {} on resource {}'.format(request.method, request.path))


def missing_required_field(request, field_name):
    return Http400('body for {r.method} Request on resource {r.path}, must contain field {}'.format(r=request, field_name))


def handle_base_request(request):
    if request.method == 'POST':
        return create(request, request.POST.get('name'))
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
    return JsonResponse([team.get_json() for team in Team.objects.all()])


def create(request, team_name):
    team = Team(name=team_name)
    team.save()
    return JsonResponse(team.get_json)


def delete(request, team):
    team.delete()
