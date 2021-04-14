# """
# api application controllers to perform CRUD operations on the Construct model
# """

# # Import python and django libraries
# import json
# # import logging
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# # Import models
# from api.models.construct_model import Construct

# # logger = logging.getLogger('dataproc')
# # logger.info("IN SHOW SAVE")

# # Define CRUD functions
# @csrf_exempt
# def indexConstruct(request):

#     """
#     Get all constructs
#     """

#     if request.method=='GET':
#         try:
#             constructs=Construct.nodes.all()
#             response=[]
#             for construct in constructs :
#                 obj= {
#                     "uuid": construct.uuid,
#                     "name": construct.name,
#                 }
#                 response.append(obj)
#             # response=json.dumps(constructs.__porperties__)
#             return JsonResponse(response, safe=False)
#             # return response
#         except:
#             return JsonResponse({"error": "Error occurred"}, safe=False)

# @csrf_exempt
# def showConstruct(request):

#     """
#     Get one construct by name
#     """

#     if request.method=='GET':
#         name=request.GET.get('name', ' ')

#         try:
#             construct=Construct.nodes.get(name=name)
#             return JsonResponse(construct.serialize, safe=False) 
#         except :
#             return JsonResponse({"error":"Error occurred"}, safe=False)

# @csrf_exempt
# def storeConstruct(request):

#     """
#     Create one construct
#     """

#     if request.method=='POST':
#         json_data=json.loads(request.body)
#         name=json_data['name']
#         try:
#             construct=Construct(name=name)
#             construct.save()
#             return JsonResponse({"uuid": construct.uuid})
#         except :
#             return JsonResponse({"error":"Error occurred"}, safe=False)

# @csrf_exempt
# def updateConstruct(request):

#     """
#     Update one construct
#     """

#     if request.method=='PUT':
#         json_data=json.loads(request.body)
#         name=json_data['name']
#         uuid=json_data['uuid']
#         try:
#             construct=Construct.nodes.get(uuid=uuid)
#             construct.name=name
#             construct.save()
#             return JsonResponse({"uuid": construct.uuid, "name": name}, safe=False)
#         except:
#             return JsonResponse({"error":"Error occurred"}, safe=False)

# @csrf_exempt
# def destroyConstruct(request):

#     """
#     Delete one construct by uuid
#     """

#     if request.method=='DELETE':
#         json_data=json.loads(request.body)
#         uuid=json_data['uuid']
#         try:
#             construct=Construct.nodes.get(uuid=uuid)
#             construct.delete()
#             return JsonResponse({"success": "Construct deleted"}, safe=False)
#         except:
#             return JsonResponse({"error":"Error occurred"}, safe=False)

"""
api application controllers to perform CRUD operations on the User model
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
                    "uuid": construct.uuid,
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
            # return JsonResponse({"uuid": user.uuid, "name": user.name}, safe=False)
            # return JsonResponse({user}, safe=False)
            return JsonResponse(construct.serialize, safe=False)
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
            return JsonResponse({"uuid": construct.uuid})
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
        uuid=json_data['uuid']
        try:
            construct=Construct.nodes.get(uuid=uuid)
            construct.name=name
            construct.save()
            return JsonResponse({"uuid": construct.uuid, "name": name}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroyConstruct(request):

    """
    Delete one construct by uuid
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        uuid=json_data['uuid']
        try:
            user=User.nodes.get(uuid=uuid)
            user.delete()
            return JsonResponse({"success": "Construct deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
