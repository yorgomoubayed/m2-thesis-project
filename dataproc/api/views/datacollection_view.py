"""
api application controllers to perform CRUD operations on the Datacollection model
"""

# Import python and django libraries
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import models
from api.models.datacollection_model import DataCollection

# Define CRUD functions
@csrf_exempt
def indexDatacollection(request):

    """
    Get all datacollections
    """

    if request.method=='GET':
        try:
            datacollections=datacollection.nodes.all()
            response=[]
            for datacollection in datacollections:
                node=Datacollection.serialize
                response.append(node)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"error": "Error occurred"}, safe=False)

@csrf_exempt
def showDatacollection(request):

    """
    Get one datacollection by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            datacollection=Datacollection.nodes.get(name=name)
            return JsonResponse(datacollection.serialize, safe=False)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def storedatacollection(request):

    """
    Create one datacollection
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            datacollection=datacollection(name=name)
            datacollection.save()
            return JsonResponse(datacollection.serialize)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def updatedatacollection(request):

    """
    Update one datacollection
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uuid=json_data['uuid']
        try:
            datacollection=Datacollection.nodes.get(uuid=uuid)
            datacollection.name=name
            datacollection.save()
            return JsonResponse(datacollection.serialize, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroydatacollection(request):

    """
    Delete one datacollection by uuid
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        uuid=json_data['uuid']
        try:
            datacollection=Datacollection.nodes.get(uuid=uuid)
            datacollection.delete()
            return JsonResponse({"success": "Datacollection deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
