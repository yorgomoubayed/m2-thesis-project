# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

# Models imports
from api.models.statisticalreport_model import StatisticalReport
from api.models.summaryout_model import SummaryOut
from api.models.summaryhtml_model import SummaryHtml

class Report(StructuredNode):
	
	'''
	Defines node properties and relationships
	Provides data serializer
	'''

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	
	# GPhL_pipedream report properties
	command=StringProperty(max_length=700)
	jsonversion=StringProperty(max_length=700)
	runby=StringProperty(max_length=700)
	runfrom=StringProperty(max_length=700)
	jobid=StringProperty(unique_index=True, default=uuid4)
	gphlpipedream_output=StringProperty(max_length=700)
	version=StringProperty(max_length=700)

	# Ligands fitting (Rhofit) report properties
	ligandomin=StringProperty()
	mogulzbond=StringProperty()
	ligandbmin=StringProperty()
	mogulring=StringProperty()
	moguldihe=StringProperty()
	ligandbavg=StringProperty()
	mogulangl=StringProperty()
	mogulbond=StringProperty()
	ligandbmax=StringProperty()
	ligandid=StringProperty()
	ligandomax=StringProperty()
	ligandcc=StringProperty()
	mogulzangl=StringProperty()
	molprobitypercentile=StringProperty()
	ramaoutlierpercent=StringProperty()
	cbetadeviations=StringProperty()
	ramafavoredpercent=StringProperty()
	poorrotamers=IntegerProperty()
	rmsbonds=IntegerProperty()
	rmsangles=IntegerProperty()
	clashpercentile=StringProperty()
	poorrotamerspercent=IntegerProperty()
	clashscore=IntegerProperty()
	ramafavored=StringProperty()
	molprobityscore=IntegerProperty()
	ramaoutliers=StringProperty()
	closecontacts=StringProperty()
	chain=StringProperty()
	contactscore=StringProperty()
	ligandstrain=StringProperty()
	poorfit=StringProperty()
	output=StringProperty()
	correlationcoefficient=StringProperty()
	rhofitscore=StringProperty()
	
	# Refinement/Post-refinement report properties
	WilsonB=StringProperty()
	Rfree=IntegerProperty()
	MeanB=StringProperty()
	type=StringProperty()
	step=StringProperty()
	RMSbonds=IntegerProperty()
	RMSangles=IntegerProperty()
	R=IntegerProperty()
	WatersPresent=StringProperty()
	selectedmodel=StringProperty()
	refinementprotocol=StringProperty()
	
	# AutoPROC report properties (includes AutoProcscaling, AutoProcScalingStatistics and AutoProc (cf pipdream_summary.json))
	recordTimeStamp=StringProperty()
	resolutionEllipsoidAxis13=StringProperty()
	resolutionEllipsoidAxis33=StringProperty()
	resolutionEllipsoidAxis23=StringProperty()
	resolutionEllipsoidValue2=StringProperty()
	resolutionEllipsoidAxis21=StringProperty()
	resolutionEllipsoidAxis31=StringProperty()
	resolutionEllipsoidAxis22=StringProperty()
	resolutionEllipsoidAxis32=StringProperty()
	resolutionEllipsoidValue3=StringProperty()
	resolutionEllipsoidAxis12=StringProperty()
	resolutionEllipsoidValue1=StringProperty()
	resolutionEllipsoidAxis11=StringProperty()
	multiplicity=StringProperty()
	resolutionLimitLow=StringProperty()
	rMeasWithinIPlusIMinus=StringProperty()
	DanoOverSigDano=StringProperty()
	completenessSpherical=StringProperty()
	nTotalUniqueObservations=StringProperty()
	rMerge=StringProperty()
	rPimWithinIPlusIMinus=StringProperty()
	anomalousCompletenessEllipsoidal=StringProperty()
	nTotalObservations=StringProperty()
	completenessEllipsoidal=StringProperty()
	anomalousCompleteness=StringProperty()
	anomalousMultiplicity=StringProperty()
	resolutionLimitHigh=StringProperty()
	completeness=StringProperty()
	ccHalf=StringProperty()
	rPimAllIPlusIMinus=StringProperty()
	meanIOverSigI=StringProperty()
	anomalousCompletenessSpherical=StringProperty()
	ccAnomalous=StringProperty()
	rMeasAllIPlusIMinus=StringProperty()
	refinedCell_beta=StringProperty()
	refinedCell_b=StringProperty()
	wavelength=StringProperty()
	refinedCell_a=StringProperty()
	refinedCell_alpha=StringProperty()
	spaceGroup=StringProperty()
	refinedCell_c=StringProperty()
	refinedCell_gamma=StringProperty()

	 # Relationships
	is_statisticalreport=RelationshipTo(StatisticalReport, 'IS')
	is_summaryout=RelationshipTo(SummaryOut, 'IS')
	is_summaryhtml=RelationshipTo(SummaryHtml, 'IS')

	@property
	def serialize(self):

		'''
		Serializer for node properties
		'''
		
		return {
		'node_properties': {

		# GPhL_pipedream report properties
		'command': self.command,
		'jsonversion': self.jsonversion,
		'runby': self.runby,
		'runfrom': self.runfrom,
		'jobid': self.jobid,
		'gphlpipedream_output': self.gphlpipedream_output,
		'version': self.version,
		
		# Ligands fitting (Rhofit) report properties
		'ligandomin': self.ligandomin,
		'mogulzbond': self. mogulzbond,
		'ligandbmin': self.ligandbmin,
		'mogulring': self.mogulring,
		'moguldihe': self.moguldihe,
		'ligandbavg': self.ligandbavg,
		'mogulangl': self.mogulangl,
		'mogulbond': self.mogulbond,
		'ligandbmax': self.ligandbmax,
		'ligandid': self.ligandid,
		'ligandomax': self.ligandomax,
		'ligandcc': self.ligandcc,
		'mogulzangl': self.mogulzangl,
		'molprobitypercentile': self.molprobitypercentile,
		'ramaoutlierpercent': self.ramaoutlierpercent,
		'cbetadeviations': self.cbetadeviations,
		'ramafavoredpercent': self.ramafavoredpercent,
		'poorrotamers': self.poorrotamers,
		'rmsbonds': self.rmsbonds,
		'rmsangles': self.rmsangles,
		'clashpercentile': self.clashpercentile,
		'poorrotamerspercent': self.poorrotamerspercent,
		'clashscore': self.clashscore,
		'ramafavored': self.ramafavored,
		'molprobityscore': self.molprobityscore,
		'ramaoutliers': self.ramaoutlers,
		'closecontacts': self.closecontacts,
		'chain': self.chain,
		'contactscore': self.contactscore,
		'ligandstrain': self.ligandstrain,
		'poorfit': self.poorfit,
		'output': self.output,
		'correlationcoefficient': self.correlationcoefficient,
		'rhofitscore': self.rhofitscore,
		
		# Refinement/Post-refinement report properties
		'WilsonB': self.WilsonB,
		'Rfree': self.Rfree,
		'MeanB': self.MeanB,
		'type': self.type,
		'step': self.step,
		'RMSbonds': self.RMSbonds,
		'RMSangles': self.RMSangles,
		'R': self.R,
		'WatersPresent': self.WatersPresent,
		'selectedmodel': self.selectedmodel,
		'refinementprotocol': self.refinementprotocol,

		# AutoPROC report properties (includes AutoProcscaling, AutoProcScalingStatistics and AutoProc (cf pipdream_summary.json))
		'recordTimeStamp': self.recordTimeStamp,
		'resolutionEllipsoidAxis13': self.resolutionEllipsoidAxis13,
		'resolutionEllipsoidAxis33': self.resolutionEllipsoidAxis33,
		'resolutionEllipsoidAxis23': self.resolutionEllipsoidAxis23,
		'resolutionEllipsoidValue2': self.resolutionEllipsoidValue2,
		'resolutionEllipsoidAxis21': self.resolutionEllipsoidAxis21,
		'resolutionEllipsoidAxis31': self.resolutionEllipsoidAxis31,
		'resolutionEllipsoidAxis22': self.resolutionEllipsoidAxis22,
		'resolutionEllipsoidAxis32': self.resolutionEllipsoidAxis32,
		'resolutionEllipsoidValue3': self.resolutionEllipsoidValue3,
		'resolutionEllipsoidAxis12': self.resolutionEllipsoidAxis12,
		'resolutionEllipsoidValue1': self.resolutionEllipsoidValue1,
		'resolutionEllipsoidAxis11': self.resolutionEllipsoidAxis11,
		'multiplicity': self.multiplicity,
		'resolutionLimitLow': self.resolutionLimitLow,
		'rMeasWithinIPlusIMinus': self.rMeasWithinIPlusIMinus,
		'DanoOverSigDano': self.DanoOverSigDano,
		'completenessSpherical': self.completenessSpherical,
		'nTotalUniqueObservations': self.nTotalUniqueObservations,
		'rMerge': self.rMerge,
		'rPimWithinIPlusIMinus': self.rPimWithinIPlusIMinus,
		'anomalousCompletenessEllipsoidal': self.anomalousCompletenessEllipsoidal,
		'nTotalObservations': self.nTotalObservations,
		'completenessEllipsoidal': self.completenessEllipsoidal,
		'anomalousCompleteness': self.anomalousCompleteness,
		'anomalousMultiplicity': self.anomalousMultiplicity,
		'resolutionLimitHigh': self.resolutionLimitHigh,
		'completeness': self.completeness,
		'ccHalf': self.ccHalf,
		'rPimAllIPlusIMinus': self.rPimAllIPlusIMinus,
		'meanIOverSigI': self.meanIOverSigI,
		'anomalousCompletenessSpherical': self.anomalousCompletenessSpherical,
		'ccAnomalous': self.ccAnomalous,
		'rMeasAllIPlusIMinus': self.rMeasAllIPlusIMinus,
		'refinedCell_beta': self.refinedCell_beta,
		'refinedCell_b': self.refinedCell_b,
		'wavelength': self.wavelength,
		'refinedCell_a': self.refinedCell_a,
		'refinedCell_alpha': self.refinedCell_alpha,
		'spaceGroup': self.spaceGroup,
		'refinedCell_c': self.refinedCell_c,
		'refinedCell_gamma': self.refinedCell_gamma,
		},
		}
