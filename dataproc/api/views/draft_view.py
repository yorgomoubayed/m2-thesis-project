@csrf_exempt
def storeParseDataset(data):

    """
    Creates nodes for each dataset with relative properties
    """

    try:
        logger.info('CHECK FUNCTION')
        Dataset.create_or_update(uuid=data['uuid'],
            userUuid=data['userUuid'], 
            crystalUuid=data['crystalUuid'],
            currentPath=data['currentPath'],
            generationPath=data['generationPath'],
            fileTemplateName=data['fileTemplateName'],
            blStartingDate=data['blStartingDate'],
            beamlineName=data['beamlineName'],
            facilityName=data['facilityName'])
        logger.info('CREATE OR UPDATE')

#         # dataset.save()

#         # if dataset == None:
#         #     datasetNew = Dataset(uuid=data['uuid'],
#         #         userUuid=data['userUuid'], 
#         #         crystalUuid=data['crystalUuid'],
#         #         currentPath=data['currentPath'],
#         #         generationPath=data['generationPath'],
#         #         fileTemplateName=data['fileTemplateName'],
#         #         blStartingDate=data['blStartingDate'],
#         #         beamlineName=data['beamlineName'],
#         #         facilityName=data['facilityName'])

#         #     datasetNew.save()
        return JsonResponse({"Status": "INPUT REGISTERED"})
        logger.info('RETURN')

    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING DATASET"})