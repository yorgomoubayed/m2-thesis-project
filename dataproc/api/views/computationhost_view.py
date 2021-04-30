"""
api application controllers to perform CRUD operations on the ComputationHost model
"""

# Python imports
import json

# Django imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Models imports
from api.models.computationhost_model import ComputationHost

@csrf_exempt
def indexComputationhost(request):

    """
    Get all computation host
    """

    if request.method=='GET':
        try:
            computinghosts=ComputingHost.nodes.all()
            response=[]
            for computationhost in computationhosts :
                node=computationhost.serialize
                response.append(node)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"error": "Error occurred"}, safe=False)

@csrf_exempt
def showComputationhost(request):

    """
    Get one computation host by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            computationhost=ComputationHost.nodes.get(name=name)
            return JsonResponse(computationhost.serialize, safe=False)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def storeComputationhost(request):

    """
    Create one computation host
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            computationhost=ComputationHost(name=name)
            computationhost.save()
            return JsonResponse(computationhost.serialize)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def updateComputationhost(request):

    """
    Update one computation host
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uuid=json_data['uuid']
        try:
            computationhost=ComputationHost.nodes.get(uuid=uuid)
            computationhost.name=name
            computation.save()
            return JsonResponse(computationhost.serialize, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroyComputationhost(request):

    """
    Delete one computation host by name
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            computationhost=ComputationHost.nodes.get(name=name)
            computationhost.delete()
            return JsonResponse({"success": "computation host deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
