"""
api application's URL configuration. "urlpatterns" lists routes URLs to views.
"""

# Import django libraries
from django.conf.urls import url
from django.urls import path

# Import CRUD functions from views modules
from api.views.autoPROC_view import *
from api.views.buster_view import *
from api.views.computinghost_view import *
from api.views.construct_view import *
from api.views.coordinates_view import *
from api.views.datacollection_view import *
from api.views.dataset_view import *
from api.views.dpstep_view import *
from api.views.ligand_view import *
from api.views.mmciffile_view import *
from api.views.mtzfile_view import *
from api.views.ocf_view import *
from api.views.pdbfile_view import *
from api.views.postrefinement_view import *
from api.views.reductionscaling_view import *
from api.views.reductionstructurefactors_view import *
from api.views.reference_view import *
from api.views.refinement_view import *
from api.views.report_view import *
from api.views.rhofit_view import * 
from api.views.scalepackfile_view import *
from api.views.statisticalreport_view import *
from api.views.storagehost_view import * 
from api.views.summaryhtml_view import *
from api.views.summaryout_view import *
from api.views.user_view import *
from api.views.relationships_view import *

# Define url patterns

urlpatterns = [
	
    # # autoPROC urlpatterns
    # path('indexautoPROC', indexautoPROC),
    # path('showautoPROC', showautoPROC),
    # path('storeautoPROC', storeautoPROC),
    # path('updateautoPROC', updateautoPROC),
    # path('destroyautoPROC', destroyautoPROC),

    # # buster urlpatterns
    # path('indexBuster', indexBuster),
    # path('showBuster', showBuster),
    # path('storeBuster', storeBuster),
    # path('updateBuster', updateBuster),
    # path('destroyBuster', destroyBuster),

    # computinghost urlpatterns
    path('indexComputinghost', indexComputinghost),
    path('showComputinghost', showComputinghost),
    path('storeComputinghost', storeComputinghost),
    path('updateComputinghost', updateComputinghost),
    path('destroyComputinghost', destroyComputinghost),

    # construct urlpatterns
    path('indexConstruct', indexConstruct),
    path('showConstruct', showConstruct),
    path('storeConstruct', storeConstruct),
    path('updateConstruct', updateConstruct),
    path('destroyConstruct', destroyConstruct),
    
    # # coordinates urlpatterns
    # path('indexCoordinates', indexCoordinates),
    # path('showCoordinates', showCoordinates),
    # path('storeCoordinates', storeCoordinates),
    # path('updateCoordinates', updateCoordinates),
    # path('destroyCoordinates', destroyCoordinates),

    # # datacollection urlpatterns
    # path('indexDatacollection', indexDatacollection),
    # path('showDatacollection', showDatacollection),
    # path('storeDatacollection', storeDatacollection),
    # path('updateDatacollection', updateDatacollection),
    # path('destroyDatacollection', destroyDatacollection),

    # # dataset urlpatterns
    # path('indexDataset', indexDataset),
    # path('showDataset', showDataset),
    # path('storeDataset', storeDataset),
    # path('updateDataset', updateDataset),
    # path('destroyDataset', destroyDataset),

    # # dpstep urlpatterns
    # path('indexDPstep', indexDPstep),
    # path('showDPstep', showDPstep),
    # path('storeDPstep', storeDPstep),
    # path('updateDPstep', updateDPstep),
    # path('destroyDPstep', destroyDPstep),

    # # ligand urlpatterns
    # path('indexLigand', indexLigand),
    # path('showLigand', showLigand),
    # path('storeLigand', storeLigand),
    # path('updateLigand', updateLigand),
    # path('destroyLigand', destroyLigand),

    # # ligandsfitting urlpatterns
    # path('indexLigandsfitting', indexLigandsfitting),
    # path('showLigandsfitting', showLigandsfitting),
    # path('storeLigandsfitting', storeLigandsfitting),
    # path('updateLigandsfitting', updateLigandsfitting),
    # path('destroyLigandsfitting', destroyLigandsfitting),

    # # mmciffile urlpatterns
    # path('indexmmciffile', indexmmciffile),
    # path('showmmciffile', showmmciffile),
    # path('storemmciffile', storemmciffile),
    # path('updatemmciffile', updatemmciffile),
    # path('destroymmciffile', destroymmciffile),

    # # mtzfile urlpatterns
    # path('indexMtzfile', indexMtzfile),
    # path('showMtzfile', showMtzfile),
    # path('storeMtzfile', storeMtzfile),
    # path('updateMtzfile', updateMtzfile),
    # path('destroyMtzfile', destroyMtzfile),

    # # ocf urlpatterns
    # path('indexOCF', indexOCF),
    # path('showOCF', showOCF),
    # path('storeOCF', storeOCF),
    # path('updateOCF', updateOCF),
    # path('destroyOCF', destroyOCF),

    # # pdbfile urlpatterns
    # path('indexPdbfile', indexPdbfile),
    # path('showPdbfile', showPdbfile),
    # path('storePdbfile', storePdbfile),
    # path('updatePdbfile', updatePdbfile),
    # path('destroyPdbfile', destroyPdbfile),

    # # postrefinement urlpatterns
    # path('indexPostrefinement', indexPostrefinement),
    # path('showPostrefinement', showPostrefinement),
    # path('storePostrefinement', storePostrefinement),
    # path('updatePostrefinement', updatePostrefinement),
    # path('destroyPostrefinement', destroyPostrefinement),

    # # reductionscaling urlpatterns
    # path('indexReductionscaling', indexReductionscaling),
    # path('showReductionscaling', showReductionscaling),
    # path('storeReductionscaling', storeReductionscaling),
    # path('updateReductionscaling', updateReductionscaling),
    # path('destroyReductionscaling', destroyReductionscaling),

    # # reductionstructurefactors urlpatterns
    # path('indexReductionstructurefactors', indexReductionstructurefactors),
    # path('showReductionstructurefactors', showReductionstructurefactors),
    # path('storeReductionstructurefactors', storeReductionstructurefactors),
    # path('updateReductionstructurefactors', updateReductionstructurefactors),
    # path('destroyReductionstructurefactors', destroyReductionstructurefactors),

    # # reference urlpatterns
    # path('indexReference', indexReference),
    # path('showReference', showReference),
    # path('storeReference', storeReference),
    # path('updateReference', updateReference),
    # path('destroyReference', destroyReference),

    # # refinement urlpatterns
    # path('indexRefinement', indexRefinement),
    # path('showRefinement', showRefinement),
    # path('storeRefinement', storeRefinement),
    # path('updateRefinement', updateRefinement),
    # path('destroyRefinement', destroyRefinement),
    
    # # report urlpatterns
    # path('indexReport', indexReport),
    # path('showReport', showReport),
    # path('storeReport', storeReport),
    # path('updateReport', updateReport),
    # path('destroyReport', destroyReport),

    # # rhofit urlpatterns
    # path('indexRhofit', indexRhofit),
    # path('showRhofit', showRhofit),
    # path('storRhofit', storeRhofit),
    # path('updateRhofit', updateRhofit),
    # path('destroyRhofit', destroyRhofit),

    # # scalepackfile urlpatterns
    # path('indexScalepackfile', indexScalepackfile),
    # path('showScalepackfile', showScalepackfile),
    # path('storeScalepackfile', storeScalepackfile),
    # path('updateScalepackfile', updateScalepackfile),
    # path('destroyScalepackfile', destroyScalepackfile),

    # # statisticalreport urlpatterns
    # path('indexStatisticalreport', indexStatisticalreport),
    # path('showStatisticalreport', showStatisticalreport),
    # path('storeStatisticalreport', storeStatisticalreport),
    # path('updateStatisticalreport', updateStatisticalreport),
    # path('destroyStatisticalreport', destroyStatisticalreport),

    # storagehost urlpatterns
    path('indexStoragehost', indexStoragehost),
    path('showStoragehost', showStoragehost),
    path('storeStoragehost', storeStoragehost),
    path('updateStoragehost', updateStoragehost),
    path('destroyStoragehost', destroyStoragehost),

    # # summaryhtml urlpatterns
    # path('indexSummaryhtml', indexSummaryhtml),
    # path('showSummaryhtml', showSummaryhtml),
    # path('storeSummaryhtml', storeSummaryhtml),
    # path('updateSummaryhtml', updateSummaryhtml),
    # path('destroySummaryhtml', destroySummaryhtml),

    # # summaryout urlpatterns
    # path('indexSummaryout', indexSummaryout),
    # path('showSummaryout', showSummaryout),
    # path('storeSummaryout', storeSummaryout),
    # path('updateSummaryout', updateSummaryout),
    # path('destroySummaryout', destroySummaryout),

    # user urlpatterns
    path('indexUser', indexUser),
    path('showUser', showUser),
    path('storeUser', storeUser),
    path('updateUser', updateUser),
    path('destroyUser', destroyUser),

    # relationships urlspatterns
    path('connectConstructUser', connectConstructUser),
    path('connectConstructStoragehost', connectConstructStoragehost),
    path('connectConstructComputinghost', connectConstructComputinghost),
    path('connectDatasetConstruct', connectDatasetConstruct),
    path('connectDatasetDPStep', connectDatasetDPStep),
    path('connectDatasetStoragehost', connectDatasetStoragehost),
    path('connectDatacollectionDataset', connectDatacollectionDataset),
    path('connectLigandDataset', connectLigandDataset),
]
