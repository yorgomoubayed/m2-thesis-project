# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

# Models imports
from api.models.dataset_model import Dataset

class Ligand(StructuredNode):

	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
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
	ramafavoredpercent=IntegerProperty()
	poorrotamers=IntegerProperty()
	rmsbonds=IntegerProperty()
	rmsangles=IntegerProperty()
	clashpercentile=StringProperty()
	poorrotamerspercent=IntegerProperty()
	clashscore=IntegerProperty()
	ramafavored=StringProperty()
	molprobityscore=IntegerProperty()
	ramaoutlier=StringProperty()

	# Relationships
	associated=RelationshipTo(Dataset, 'ASSOCIATED')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {

		'ligand_node_properties': {
		'uuid': self.uuid,
		'ligandomin': self.ligandomin,
		'mogulzbond': self.mogulzbond,
		'ligandbmin': self.ligandbmin,
		'mogulring': self.mogulring,
		'moguldihe': self.moguldihe,
		'ligandbavg': self.ligandbavg,
		'mogulangl': self.mogulangl,
		'mogulbond': self.mogulangl,
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
		'ramaoutlier': self.ramaoutlier,
		}
		},
