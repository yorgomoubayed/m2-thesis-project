"""
api application controllers to perform CRUD operations on the Storagehost model
"""

# Python imports
import json

# Django imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Models imports
from api.models.storagehost_model import StorageHost

@csrf_exempt
def indexStoragehost(request):

    """
    Get all storagehosts
    """

    if request.method=='GET':
        try:
            storagehosts=StorageHost.nodes.all()
            response=[]
            for storagehost in storagehosts :
                node=storagehost.serialize
                response.append(node)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"error": "Error occurred"}, safe=False)

@csrf_exempt
def showStoragehost(request):

    """
    Get one storagehost by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            storagehost=StorageHost.nodes.get(name=name)
            return JsonResponse(storagehost.serialize, safe=False)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def storeStoragehost(request):

    """
    Create one storagehost
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            storagehost=StorageHost(name=name)
            storagehost.save()
            return JsonResponse(storagehost.serialize)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def updateStoragehost(request):

    """
    Update one storagehost
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uuid=json_data['uuid']
        try:
            storagehost=StorageHost.nodes.get(uuid=uuid)
            storagehost.name=name
            storagehost.save()
            return JsonResponse(user.serialize, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroyStoragehost(request):

    """
    Delete one user by uuid
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            storagehost=StorageHost.nodes.get(name=name)
            storagehost.delete()
            return JsonResponse({"success": "Storagehost deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
