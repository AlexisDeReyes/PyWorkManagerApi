from django.http import HttpResponse

# Create your views here.


def get(request):
    return HttpResponse("Get all Teams")


def get_specific(request, team_id):
    return HttpResponse("Get a Team using id: {}".format(team_id))


def create(request):
    return HttpResponse("Create Team")


def delete(request):
    return HttpResponse("Delete Team")
