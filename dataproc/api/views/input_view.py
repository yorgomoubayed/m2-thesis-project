# Import Django libraries
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import Python libraries
import json
import logging
import sys

# Import models
from api.models.dataset_model import Dataset
from api.models.storagehost_model import StorageHost
from api.models.computationhost_model import ComputationHost
from api.models.datacollection_model import DataCollection
from api.models.construct_model import Construct
from api.models.user_model import User
from api.models.ocf_model import OCF

# Activate logger
logger = logging.getLogger('dataproc')
#logger.info('TEMPLATE')

@csrf_exempt
def storeInput(request):

    """
    Parse JSON data and call store functions for each model
    """

    if request.method=='POST':
        json_data=json.loads(request.body)
        
        json_data_dataset=json_data['dataset']
        json_data_storagehost=json_data['storageHost']
        json_data_user=json_data['user']
        json_data_construct=json_data['construct']
        json_data_computationhost=json_data['computationHost']
        json_data_datacollection=json_data['dataCollection']
        # json_data_ocf=json_data['OCF']
        
        try:

            storeParseDataset(json_data_dataset)
            storeParseStorageHost(json_data_storagehost)
            storeParseUser(json_data_user)
            storeParseConstruct(json_data_construct)
            storeParseComputationHost(json_data_computationhost)
            storeParseDataCollection(json_data_datacollection)
            # storeParseOCF(json_data_ocf)

            return JsonResponse({"Status": "INPUT SUCCESSFULLY REGISTERED"})

        except :
            return JsonResponse({"Status":"ERROR OCCURRED"}, safe=False)

@csrf_exempt
def storeParseDataset(data):

    """
    Creates nodes for each dataset with relative properties
    """

    try:
        dataset=Dataset(uuid=data['uuid'],
            userUuid=data['userUuid'], 
            crystalUuid=data['crystalUuid'],
            currentPath=data['currentPath'],
            generationPath=data['generationPath'],
            fileTemplateName=data['fileTemplateName'],
            blStartingDate=data['blStartingDate'],
            beamlineName=data['beamlineName'],
            facilityName=data['facilityName'])
        dataset.save()
        return dataset.serialize
    
    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING DATASET"})

@csrf_exempt
def storeParseStorageHost(data):

    """
    Creates nodes for each storage host with relative properties
    """

    try:
        storagehost=StorageHost(ip=data['ip'],
            # uuid=data['uuid'],
            hostName=data['hostName'],
            friendlyName=data['friendlyName'],
            workingDirectory=data['workingDirectory']
            )
        storagehost.save()
        return storagehost.serialize
    
    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING STORAGE HOST"})

@csrf_exempt
def storeParseComputationHost(data):

    """
    Creates nodes for each computing host with relative properties
    """

    try:
        computationhost=ComputationHost(ip=data['ip'],
            uuid=data['uuid'],
            hostName=data['hostName'],
            friendlyName=data['friendlyName'],
            workingDirectory=data['workingDirectory']
            )
        computationhost.save()
        return computationhost.serialize
    
    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING COMPUTATION HOST"})

@csrf_exempt
def storeParseConstruct(data):

    """
    Creates nodes for each construct with relative properties
    """

    try:
        construct=Construct(uuid=data['uuid'],
            userUuid=data['userUuid'],
            name=data['name'])
        construct.save()
        return construct.serialize
    
    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING CONSTRUCT"})

@csrf_exempt
def storeParseUser(data):

    """
    Creates nodes for each user with relative properties
    """

    try:
        user=User(uuid=data['uuid'])
        user.save()
        return user.serialize
    
    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING USER"})

@csrf_exempt
def storeParseDataCollection(data):

    """
    Creates nodes for each data collection with relative properties
    """
    try:
        datacollection=DataCollection(uuid=data['uuid'],
            imagesNumber=data['imagesNumber'],
            flux=data['flux'],
            resolution=data['resolution'],
            wavelength=data['wavelength'],
            transmission=data['transmission'],
            exposureTime=data['exposureTime'],
            detectorDistance=data['detectorDistance'],
            beamlineName=data['beamlineName']
            )
        datacollection.save()
        return datacollection.serialize

    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING DATA COLLECTION"})

@csrf_exempt
def storeParseOCF(data):

    """
    Creates nodes for each ocf with relative properties
    """
    try:
        ocf=OCF(
            # uuid=data['uuid'],
            # userUuid=data['userUuid'],
            name=data['name'],
            pipedreamCommand=data['pipedreamCommand'],
            priority=data['priority'])

        for ocf in data:
            ocf.save()
            return ocf.serialize
        # ocf.save()
        # return ocf.serialize

    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING OCF"})
