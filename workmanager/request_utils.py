#!/env/Scripts/python

"""Library for common procedures necessary for handling and responding to requests"""

from django.http import HttpResponse, HttpResponseBadRequest as Http400, Http404, JsonResponse, HttpRequest, HttpResponseNotFound
from django.db.utils import IntegrityError
import json


def Json(data: object) -> HttpResponse:
    """responds to the request with a Json data response. Will not throw errors for "improper" json

    Arguments:
        data {dict|list} -- dict or list to send as json

    Returns:
        HttpResponse -- Http response with json body
    """
    return JsonResponse(data)


def no_method_for_resouce(request: HttpRequest) -> Http404:
    """responds to the request with a 404 resource does not support method

    Arguments:
        request {HttpRequest} -- django HttpRequest

    Returns:
        Http404 -- Http Response 404 resource does not support method
    """
    return HttpResponseNotFound('Cannot perform method {r.method} on resource {r.path}'.format(r=request))


def no_items_found(request: HttpRequest) -> Http404:
    """responds to the request with a 404 not found

    Arguments:
        request {HttpRequest} -- django HttpRequest

    Returns:
        Http404 -- Http Response 404 not found
    """
    return HttpResponseNotFound('request for resource {} returned no results'.format(request.path))


def missing_required_field(request: HttpRequest, field_names: list) -> Http400:
    """responds to the request with a 400 bad request

    Arguments:\n
        request {HttpRequest} -- django HttpRequest
        field_names {list of str} -- list of field names missing or invalid

    Returns:
        Http400 -- Http Response 404 not found
    """
    return Http400('body for {r.method} request on resource {r.path}, must contain fields {}'.format(', '.join(field_names), r=request))


def route_base_request(request: HttpRequest, create_item, get_all):
    """handles and routes requests for a base resource 'get all, create, etc...

    Arguments:
        request {HttpRequest} -- django HttpRequest
        create_item {function} -- function takes json object and returns newly created resource
        get_all {function} -- function returns list of all items of resource

    Returns:
        HttpResponse -- Http Response with the result(s) or an error
    """
    if request.method == 'GET':
        results = get_all(request)
        if len(results) > 0:
            return Json(results)
        return Http404(request)
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        try:
            return Json(create_item(body))
        except IntegrityError as error:
            return missing_required_field(request, [field.split('_')[1] for field in error.args])


def route_specific_request(request: HttpRequest, model, id: int, delete) -> HttpResponse:
    """handles and routes requests for an identified resource 'get specific, delete, put, etc...

    Arguments:
        request {HttpRequest} -- [description]
        model {django model class} -- Class matching resource
        id {int} -- identifier for resource
        delete {function} -- Takes resource, deletes, returns resource in dict form

    Returns:
        HttpResponse
    """
    try:
        resource = model.objects.get(pk=id)
        if request.method == 'GET':
            return Json(resource.get_json())
        if request.method == 'DELETE':
            return delete(request, resource)
        return no_method_for_resouce(request)
    except model.DoesNotExist:
        return no_items_found(request)
