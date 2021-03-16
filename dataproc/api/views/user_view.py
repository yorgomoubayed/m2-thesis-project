"""
api application controllers to perform CRUD operations on the User model
"""

# Import python and django libraries
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import models
from api.models.user_model import User

# Define CRUD functions
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
                obj= {
                    "uuid": user.uuid,
                    "name": user.name,
                }
                response.append(obj)
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
            return JsonResponse({"uuid": user.uuid, "name": user.name}, safe=False)
            # return JsonResponse({user}, safe=False)
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
            return JsonResponse({"uuid": user.uuid})
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
            return JsonResponse({"uuid": user.uuid, "name": name}, safe=False)
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
