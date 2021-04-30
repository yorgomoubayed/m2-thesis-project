"""
api application controllers to perform CRUD operations on the user model
"""

# Python imports
import json

# Django imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Models imports
from api.models.user_model import User

@csrf_exempt
def indexUser(request):

    """
    Get all users
    """

    if request.method=='GET':
        try:
            users=User.nodes.all()
            response=[]
            for user in users :
                node=user.serialize
                response.append(node)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"error": "Error occurred"}, safe=False)

@csrf_exempt
def showUser(request):

    """
    Get one user by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            user=User.nodes.get(name=name)
            return JsonResponse(user.serialize, safe=False)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def storeUser(request):

    """
    Create one user
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            user=User(name=name)
            user.save()
            return JsonResponse(user.serialize)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def updateUser(request):

    """
    Update one user
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uuid=json_data['uuid']
        try:
            user=User.nodes.get(uuid=uuid)
            user.name=name
            user.save()
            return JsonResponse(user.serialize, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroyUser(request):

    """
    Delete one user by uuid
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        uuid=json_data['uuid']
        try:
            user=User.nodes.get(uuid=uuid)
            user.delete()
            return JsonResponse({"success": "User deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
