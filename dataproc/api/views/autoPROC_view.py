# """
# api application controllers to perform CRUD operations on the User model
# """

# # Python imports
# import json

# Django imports
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# # Models imports
# from api.models.autoPROC_model import autoPROC

# @csrf_exempt
# def indexautoPROC(request):

#     """
#     Get all datasets
#     """

#     if request.method=='GET':
#         try:
#             datasets=Dataset.nodes.all()
#             response=[]
#             for dataset in datasets :
#                 node=dataset.serialize
#                 response.append(node)
#             return JsonResponse(response, safe=False)
#         except:
#             return JsonResponse({"error": "Error occurred"}, safe=False)

# @csrf_exempt
# def showDataset(request):

#     """
#     Get one dataset by name
#     """

#     if request.method=='GET':
#         name=request.GET.get('name', ' ')
#         try:
#             dataset=Dataset.nodes.get(name=name)
#             return JsonResponse(dataset.serialize, safe=False)
#         except :
#             return JsonResponse({"error":"Error occurred"}, safe=False)

# @csrf_exempt
# def storeDataset(request):

#     """
#     Create one dataset
#     """

#     if request.method=='POST':
#         json_data=json.loads(request.body)
#         name=json_data['name']
#         try:
#             dataset=Dataset(name=name)
#             dataset.save()
#             return JsonResponse(dataset.serialize)
#         except :
#             return JsonResponse({"error":"Error occurred"}, safe=False)

# @csrf_exempt
# def updateDataset(request):

#     """
#     Update one dataset
#     """

#     if request.method=='PUT':
#         json_data=json.loads(request.body)
#         name=json_data['name']
#         uuid=json_data['uuid']
#         try:
#             dataset=Dataset.nodes.get(uuid=uuid)
#             dataset.name=name
#             dataset.save()
#             return JsonResponse(dataset.serialize, safe=False)
#         except:
#             return JsonResponse({"error":"Error occurred"}, safe=False)

# @csrf_exempt
# def destroyDataset(request):

#     """
#     Delete one dataset by uuid
#     """

#     if request.method=='DELETE':
#         json_data=json.loads(request.body)
#         uuid=json_data['uuid']
#         try:
#             dataset=Dataset.nodes.get(uuid=uuid)
#             dataset.delete()
#             return JsonResponse({"success": "Dataset deleted"}, safe=False)
#         except:
#             return JsonResponse({"error":"Error occurred"}, safe=False)
