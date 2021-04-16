"""
api application controllers to perform CRUD operations on the Ligand model
"""

# Import python and django libraries
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import models
from api.models.ligand_model import Ligand

# Define CRUD functions
@csrf_exempt
def indexLigand(request):

    """
    Get all ligands
    """

    if request.method=='GET':
        try:
            ligands=Ligand.nodes.all()
            response=[]
            for ligand in ligands :
                node=ligand.serialize
                response.append(node)
            return JsonResponse(response, safe=False)
        except:
            return JsonResponse({"error": "Error occurred"}, safe=False)

@csrf_exempt
def showLigand(request):

    """
    Get one ligand by name
    """

    if request.method=='GET':
        name=request.GET.get('name', ' ')
        try:
            ligand=Ligand.nodes.get(name=name)
            return JsonResponse(ligand.serialize, safe=False)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def storeLigand(request):

    """
    Create one ligand
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        name=json_data['name']
        try:
            ligand=Ligand(name=name)
            ligand.save()
            return JsonResponse(ligand.serialize)
        except :
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def updateLigand(request):

    """
    Update one ligand
    """

    if request.method=='PUT':
        json_data=json.loads(request.body)
        name=json_data['name']
        uuid=json_data['uuid']
        try:
            ligand=Ligand.nodes.get(uuid=uuid)
            ligand.name=name
            ligand.save()
            return JsonResponse(ligand.serialize, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)

@csrf_exempt
def destroyLigand(request):

    """
    Delete one ligand by uuid
    """

    if request.method=='DELETE':
        json_data=json.loads(request.body)
        uuid=json_data['uuid']
        try:
            ligand=Ligand.nodes.get(uuid=uuid)
            ligand.delete()
            return JsonResponse({"success": "Ligand deleted"}, safe=False)
        except:
            return JsonResponse({"error":"Error occurred"}, safe=False)
