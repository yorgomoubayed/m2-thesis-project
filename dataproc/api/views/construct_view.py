"""
api application controllers to perform CRUD operations on the construct model
"""

# Import Python libraries
import json
import logging

# Import Django libraries
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import models
from api.models.construct_model import Construct

# Activate logger
logger = logging.getLogger('dataproc')
# logger.info('TEMPLATE')

# Define CRUD functions
@csrf_exempt
def indexConstruct(request):

    """
    Get all constructs
    """

    if request.method=='GET':
        try:
            constructs=Construct.nodes.all()
            response=[]
            for construct in constructs :
                node=construct.serialize
                response.append(node)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"Status": "ERROR OCCURRED"}, safe=False)

@csrf_exempt
def showConstruct(request):

    """
    Get one construct by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            construct=Construct.nodes.get(name=name)
            return JsonResponse(construct.serialize, safe=False)
        except :
            return JsonResponse({"Status": "ERROR OCCURRED"}, safe=False)

@csrf_exempt
def storeConstruct(request):

    """
    Create one construct
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            construct=Construct(name=name)
            construct.save()
            return JsonResponse(construct.serialize)
        except :
            return JsonResponse({"Status": "ERROR OCCURRED"}, safe=False)

@csrf_exempt
def updateConstruct(request):

    """
    Update one construct
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uuid=json_data['uuid']
        try:
            construct=Construct.nodes.get(uuid=uuid)
            construct.name=name
            construct.save()
            return JsonResponse(construct.serialize, safe=False)
        except:
            return JsonResponse({"Status": "ERROR OCCURRED"}, safe=False)

@csrf_exempt
def destroyConstruct(request):

    """
    Delete one construct by uuid
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        uuid=json_data['uuid']
        try:
            construct=Construct.nodes.get(uuid=uuid)
            construct.delete()
            return JsonResponse({"Status": "CONSTRUCT DELETED"}, safe=False)
        except:
            return JsonResponse({"Status": "ERROR OCCURRED"}, safe=False)
