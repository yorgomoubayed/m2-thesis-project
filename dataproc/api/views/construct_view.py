"""
api application controllers to perform CRUD operations on the Construct model
"""

# Import python and django libraries
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import models
from api.models.construct_model import Construct

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
                obj= {
                    "uid": construct.uid,
                    "name": construct.name,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"error": "Error occurred"}, safe=False)

@csrf_exempt
def showConstruct(request):

    """
    Get one construct by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            construct=Construct.nodes.get(name=name)
            return JsonResponse({"uid": construct.uid, "name": construct.name}, safe=False)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

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
            return JsonResponse({"uid": construct.uid})
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def updateConstruct(request):

    """
    Update one construct
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uid=json_data['uid']
        try:
            construct=Construct.nodes.get(uid=uid)
            construct.name=name
            construct.save()
            return JsonResponse({"uid": construct.uid, "name": name}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroyConstruct(request):

    """
    Delete one construct by uid
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        uid=json_data['uid']
        try:
            construct=Construct.nodes.get(uid=uid)
            construct.delete()
            return JsonResponse({"success": "Construct deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
