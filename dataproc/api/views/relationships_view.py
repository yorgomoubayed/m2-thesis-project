"""
api application controllers to create relationships between the nodes.
Functions a relative to the outbound relationships from the nodes.
"""

# Python imports
import json

# Django imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Models imports
from api.models.construct_model import Construct
from api.models.user_model import User
from api.models.storagehost_model import StorageHost
from api.models.computationhost_model import ComputationHost
from api.models.dataset_model import Dataset
from api.models.dpstep_model import DPStep
from api.models.datacollection_model import DataCollection
from api.models.ligand_model import Ligand

@csrf_exempt
def connectConstructUser(request):

	"""
	Create a relationship between a construct and a user
	"""

	if request.method=="PUT":
		json_data=json.loads(request.body)
		name=json_data["name"]
		uuid=json_data["uuid"]

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
			construct=Construct.nodes.get(uuid=uuid)
			storagehost=StorageHost.nodes.get(name=name)
			return JsonResponse({"Status": construct.has_storage_host.connect(storagehost)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)

@csrf_exempt
def connectConstructComputationhost(request):
	
	"""
	Create a relationship between a construct and a computationhost
	"""
	
	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			construct=Construct.nodes.get(uuid=uuid)
			computationhost=ComputationHost.nodes.get(name=name)
			return JsonResponse({"Status": construct.has_computation_host.connect(computationhost)}, safe=False)

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
			return JsonResponse({"Status": dataset.stored.connect(storagehost)}, safe=False)

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
			datacollection=DataCollection.nodes.get(uuid=uuid)
			dataset=Dataset.nodes.get(name=name)
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
			ligand=Ligand.nodes.get(uuid=uuid)
			dataset=Dataset.nodes.get(name=name)
			return JsonResponse({"Status": ligand.associated.connect(dataset)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)