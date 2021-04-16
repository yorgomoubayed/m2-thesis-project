"""
api application controllers to create relationships between the nodes
"""

# Import python and django libraries
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Import models
from api.models import *

# Define CRUD methods

@csrf_exempt
def connectConstructUser(request):

	"""
	Create a relationship between a construct and a user
	"""

	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			construct=Construct.nodes.get(name=name)
			user=User.nodes.get(uuid=uuid)
			return JsonResponse({"Status": construct.has_user.connect(user)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)

@csrf_exempt
def connectConstructStoragehost(request):
	
	"""
	Create a relationship between a construct and a storagehost
	"""
	
	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			construct=Construct.nodes.get(name=name)
			storagehost=StorageHost.nodes.get(uuid=uuid)
			return JsonResponse({"Status": construct.has_storage_host.connect(storagehost)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)

@csrf_exempt
def connectConstructComputinghost(request):
	"""
	Create a relationship between a construct and a computinghost
	"""
	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			construct=Construct.nodes.get(name=name)
			computinghost=ComputingHost.nodes.get(uuid=uuid)
			return JsonResponse({"Status": construct.has_computing_host.connect(computinghost)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)

@csrf_exempt
def connectDatasetConstruct(request):
	
	"""
	Create a relationship between a dataset and a construct
	"""

	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			dataset=Dataset.nodes.get(name=name)
			construct=Construct.nodes.get(uuid=uuid)
			return JsonResponse({"Status": dataset.belongs.connect(construct)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)

@csrf_exempt
def connectDatasetDPStep(request):

	"""
	Create a relationship between a dataset and a dpstep
	"""

	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			dataset=Dataset.nodes.get(name=name)
			dpstep=DPStep.nodes.get(uuid=uuid)
			return JsonResponse({"Status": dataset.input_of.connect(dpstep)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)

@csrf_exempt
def connectDatasetStoragehost(request):

	"""
	Create a relationship between a dataset and a storagehost
	"""

	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			dataset=Dataset.nodes.get(name=name)
			storagehost=StorageHost.nodes.get(uuid=uuid)
			return JsonResponse({"Status": dataset.has_storage_host.connect(storagehost)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)

@csrf_exempt
def connectDatacollectionDataset(request):
	
	"""
	Create a relationship between a datacollection and a dataset
	"""
	
	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			datacollection=DataCollection.nodes.get(name=name)
			dataset=Dataset.nodes.get(uuid=uuid)
			return JsonResponse({"Status": datacollection.generates.connect(dataset)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)

@csrf_exempt
def connectLigandDataset(request):
	
	"""
	Create a relationship between a ligand and a dataset
	"""
	
	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			ligand=Ligand.nodes.get(name=name)
			dataset=Dataset.nodes.get(uuid=uuid)
			return JsonResponse({"Status": ligand.associated.connect(dataset)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)