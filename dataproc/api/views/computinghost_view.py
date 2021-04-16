"""
api application controllers to perform CRUD operations on the Computinghost model
"""

# Import python and django libraries
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import models
from api.models.computinghost_model import ComputingHost


# Define CRUD functions
@csrf_exempt
def indexComputinghost(request):

    """
    Get all computinghost
    """

    if request.method=='GET':
        try:
            computinghosts=ComputingHost.nodes.all()
            response=[]
            for computinghost in computinghosts :
                node=computinghost.serialize
                response.append(node)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"error": "Error occurred"}, safe=False)

@csrf_exempt
def showComputinghost(request):

    """
    Get one computinghost by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            computinghost=ComputingHost.nodes.get(name=name)
            return JsonResponse(computinghost.serialize, safe=False)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def storeComputinghost(request):

    """
    Create one computinghost
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            computinghost=ComputingHost(name=name)
            computinghost.save()
            return JsonResponse(computinghost.serialize)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def updateComputinghost(request):

    """
    Update one computinghost
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uuid=json_data['uuid']
        try:
            computinghost=ComputingHost.nodes.get(uuid=uuid)
            computinghost.name=name
            computinghost.save()
            return JsonResponse(computinghost.serialize, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroyComputinghost(request):

    """
    Delete one computinghost by name
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            computinghost=ComputingHost.nodes.get(name=name)
            computinghost.delete()
            return JsonResponse({"success": "Computinghost deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
