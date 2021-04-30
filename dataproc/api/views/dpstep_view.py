"""
api application controllers to perform CRUD operations on the User model
"""

# Python imports
import json

# Django imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Models imports
from api.models.dpstep_model import DPStep

@csrf_exempt
def indexDPStep(request):

    """
    Get all dpsteps
    """

    if request.method=='GET':
        try:
            dpsteps=DPStep.nodes.all()
            response=[]
            for dpstep in dpsteps :
                node=dpstep.serialize
                response.append(node)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"error": "Error occurred"}, safe=False)

@csrf_exempt
def showDPStep(request):

    """
    Get one dpstep by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            dpstep=DPStep.nodes.get(name=name)
            return JsonResponse(dpstep.serialize, safe=False)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def storeDPStep(request):

    """
    Create one dpstep
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            dpstep=DPStep(name=name)
            dpstep.save()
            return JsonResponse(dpstep.serialize)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def updateDPStep(request):

    """
    Update one dpstep
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uuid=json_data['uuid']
        try:
            dpstep=DPStep.nodes.get(uuid=uuid)
            dpstep.name=name
            dpstep.save()
            return JsonResponse(dpstep.serialize, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroyDPStep(request):

    """
    Delete one dpstep by uuid
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        uuid=json_data['uuid']
        try:
            dpstep=DPStep.nodes.get(uuid=uuid)
            dpstep.delete()
            return JsonResponse({"success": "DPStep deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
