# Python imports
import json
import logging
import sys

# Django imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Models imports
from api.models.pipedream_model import GPhLPipedream
from api.models.report_model import Report
from api.models.dpstep_model import DPStep
from api.models.ligandsfitting_model import LigandsFitting
from api.models.reductionscaling_model import ReductionScaling
from api.models.refinement_model import Refinement
from api.models.postrefinement_model import PostRefinement

# Activate logger
logger=logging.getLogger('dataproc')

@csrf_exempt
def storeProcInput(request):

    """
    Parse JSON data and call store functions for each model
    """

    if request.method=='POST':
        json_data=json.loads(request.body)

        try:
            # Register nodes
            storeParseReport(json_data)

            # Register relationships 
            # connectConstructUser(json_data_construct, json_data_user)

            return JsonResponse({"STATUS": "INPUT SUCCESSFULLY REGISTERED"})
        
        except :
            return JsonResponse({"STATUS":"ERROR OCCURRED"}, safe=False)

@csrf_exempt
def storeParseGPhLPipedream(data):

    """
    Creates nodes for each # with relative properties
    """

    try:
        gphl_pipedream=GPhLPipedream(command=data['command'], 
            jsonversion=data['jsonversion'],
            runby=data['runby'],
            runfrom=data['runfrom'],
            jobid=data['jobid'],
            output=data['output'],
            version=data['version'])
        gphl_pipedream.save()
        return gphl_pipedream.serialize
    
    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING DATASET"})

@csrf_exempt
def storeParseReport(data):

    """
    Creates nodes for each report with relative properties
    """

    try:
        logger.info(data)
        
        GPhL_pipedream=data['GPhL_pipedream']
        ligandsstatistics=data['ligandfitting']['ligands']['1']['validationstatistics']['ligandstatistics']['1']
        molprobity=data['ligandfitting']['ligands']['1']['validationstatistics']['molprobity']
        solutions=data['ligandfitting']['ligands']['1']['solutions']['1']
        postrefinement=data['ligandfitting']['ligands']['1']['postrefinement']['cycles']['2']

        report=Report(command=GPhL_pipedream['command'], 
            jsonversion=GPhL_pipedream['jsonversion'],
            runby=GPhL_pipedream['runby'],
            runfrom=GPhL_pipedream['runfrom'],
            jobid=GPhL_pipedream['jobid'],
            gphlpipedream_output=GPhL_pipedream['output'],
            version=GPhL_pipedream['version'],

            ligandomin=ligandsstatistics['ligandomin'],
            mogulzbond=ligandsstatistics['mogulzbond'],
            ligandbmin=ligandsstatistics['ligandbmin'],
            mogulring=ligandsstatistics['mogulring'],
            moguldihe=ligandsstatistics['moguldihe'],
            ligandbavg=ligandsstatistics['ligandbavg'],
            mogulangl=ligandsstatistics['mogulangl'],
            mogulbond=ligandsstatistics['mogulbond'],
            ligandbmax=ligandsstatistics['ligandbmax'],
            ligandid=ligandsstatistics['ligandid'],
            ligandomax=ligandsstatistics['ligandomax'],
            ligandcc=ligandsstatistics['ligandcc'],
            mogulzangl=ligandsstatistics['mogulzangl'],
            
            molprobitypercentile=molprobity['molprobitypercentile'],
            ramaoutlierpercent=molprobity['ramaoutlierpercent'],
            cbetadeviations=molprobity['cbetadeviations'],
            ramafavoredpercent=molprobity['ramafavoredpercent'],
            poorrotamers=molprobity['poorrotamers'],
            rmsbonds=molprobity['rmsbonds'],
            rmsangles=molprobity['rmsangles'],
            clashpercentile=molprobity['clashpercentile'],
            poorrotamerspercent=molprobity['poorrotamerspercent'],
            clashscore=molprobity['clashscore'],
            ramafavored=molprobity['ramafavored'],
            molprobityscore=molprobity['molprobityscore'],
            ramaoutliers=molprobity['ramaoutliers'],
            
            losecontacts=solutions['closecontacts'],
            chain=solutions['chain'],
            contactscore=solutions['contactscore'],
            ligandstrain=solutions['ligandstrain'],
            poorfit=solutions['poorfit'],
            output=solutions['output'],
            correlationcoefficient=solutions['correlationcoefficient'],
            rhofitscore=solutions['rhofitscore'])
            
            # WilsonB=postrefinement['WilsonB'],
            # Rfree=postrefinement['Rfree'],
            # MeanB=postrefinement['MeanB'],
            # type=postrefinement['type'],
            # step=postrefinement['step'],
            # RMSbonds=postrefinement['RMSbonds'],
            # RMSangles=postrefinement['RMSangles'],
            # R=postrefinement['R'],
            # WatersPresent=postrefinement['WatersPresent'],)
        
        report.save()
        return report.serialize
    
    except:
        print(sys.exc_info()[0])
        return ({"STATUS": "ERROR OCCURRED WHILE REGISTERING REPORT"})

# @csrf_exempt
# def connectDPStepReport(data1, data2):

#     """
#     Create a relationship between a dpstep and a report
#     """
    
#     try:
#         dpstep=DPStep.nodes.get(name=data1["uuid"])
#         report=Report.nodes.get(uuid=data2["name"])
#         return JsonResponse({"STATUS": dpstep.generates_report.connect(report)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO REPORT"}, safe=False)

# @csrf_exempt
# def connectDPStepRefinement(data1, data2):
    
#     """
#     Create a relationship between a dpstep and a refinement node
    
#     try:
#         dpstep=DPStep.nodes.get(name=data1["uuid"])
#         refinement=Refinement.nodes.get(uuid=data2["uuid"])
#         return JsonResponse({"STATUS": dpstep.is_refinement.connect(refinement)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO REFINEMENT"}, safe=False)

# @csrf_exempt
# def connectDPStepPostRefinement(data1, data2):
    
#     """
#     Create a relationship between a dpstep and a postrefinement node
#     """

#     try:
#         dpstep=DPStep.nodes.get(uuid=data1["uuid"])
#         postrefinment=PostRefinement.nodes.get(uuid=data2["uuid"])
#         return JsonResponse({"STATUS": dpstep.is_postrefinement.connect(postrefinement)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO POST-REFINEMENT"}, safe=False)

# @csrf_exempt
# def connectDPStepLigandsFitting(data1, data2):
    
#     """
#     Create a relationship between a dpstep and a ligandsfitting node
#     """

#     try:
#         dpstep=DPStep.nodes.get(uuid=data1["uuid"])
#         ligandsfitting=LigandsFitting.nodes.get(uuid=data2["uuid"])
#         return JsonResponse({"STATUS": dataset.belongs.connect(construct)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO LIGANDS FITTING NODE"}, safe=False)

# @csrf_exempt
# def connectDPStepReductionScaling(data1, data2):

#     """
#     Create a relationship between a dpstep and a reductionscaling node
#     """

#     try:
#         dpstep=DPStep.nodes.get(uuid=data1["uuid"])
#         reductionscaling=StorageHost.nodes.get(uuid=data2["uuid"])
#         return JsonResponse({"Status": dpstep.is_reductionscaling.connect(reductionscaling)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO REDUCTION SACLING NODE"}, safe=False)

# @csrf_exempt
# def connectDPStepautoPROC(data1, data2):
    
#     """
#     Create a relationship between a dpstep and an autoRPOC node
#     """

#     try:
#         dpstep=DPStep.nodes.get(uuid=data1["uuid"])
#         autoproc=autoPROC.nodes.get(uuid=data2["uuid"])
#         return JsonResponse({"STATUS": dpstep.with_autoproc.connect(autoproc)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO AUTOPROC NODE"}, safe=False)

# @csrf_exempt
# def connectDPStepRhofit(data1, data2):
    
#     """
#     Create a relationship between a dpstep and a rhofit node
#     """

#     try:
#         dpstep=DPStep.nodes.get(uuid=data1["uuid"])
#         rhofit=Rhofit.nodes.get(uuid=data2["uuid"])

#         return JsonResponse({"STATUS": dpstep.with_rhofit.connect(rhofit)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO RHOFIT NODE"}, safe=False)

# @csrf_exempt
# def connectDPStepBuster(data1, data2):
    
#     """
#     Create a relationship between a dpstep and a buster node
#     """

#     try:
#         dpstep=DPStep.nodes.get(uuid=data1["uuid"])
#         buster=Buster.nodes.get(uuid=data2["uuid"])

#         return JsonResponse({"STATUS": dpstep.wiht_buster.connect(buster)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO BUSTER NODE"}, safe=False)

# @csrf_exempt
# def connectDPStepPipedream(data1, data2):
    
#     """
#     Create a relationship between a dpstep and a pipedream node
#     """

#     try:
#         dpstep=DPStep.nodes.get(uuid=data1["uuid"])
#         pipedream=GPhLPipedream.nodes.get(uuid=data2["uuid"])

#         return JsonResponse({"STATUS": dpstep.with_pipedream.connect(pipedream)}, safe=False)

#     except:
#         return JsonResponse({"STATUS": "ERROR OCCURRED WHILE CONNECTING DPSTEP TO PIPEDREAM NODE"}, safe=False)

